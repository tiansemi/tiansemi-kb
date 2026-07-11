from __future__ import annotations

import argparse
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib import request, error, parse

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CRED_DIR = Path(
    r"C:\Users\MOULO Oholo Jean\OneDrive - Institut National Polytechnique Félix HOUPHOUËT-BOIGNY - INP-HB\PROJETS\TS\cred"
)
LINKEDIN_POSTS_URL = "https://api.linkedin.com/rest/posts"
LINKEDIN_INTROSPECT_URL = "https://www.linkedin.com/oauth/v2/introspectToken"
LINKEDIN_VERSION = "202606"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig").strip()


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    text = text.lstrip("\ufeff")
    if not text.startswith("---\n"):
        return {}, text.strip()
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text.strip()
    raw = text[4:end].splitlines()
    body = text[end + 5 :].strip()
    meta: dict[str, str] = {}
    for line in raw:
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"\'')
    return meta, body


def extract_post_text(markdown: str) -> str:
    _, body = parse_frontmatter(markdown)
    lines = []
    for line in body.splitlines():
        if line.strip() == "# LinkedIn Post":
            continue
        lines.append(line.rstrip())
    text = "\n".join(lines).strip()
    text = re.sub(r"\n{3,}", "\n\n", text)
    if not text:
        raise ValueError("Draft LinkedIn vide apres extraction.")
    return text


def load_secret(path: Path, label: str) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Fichier requis manquant pour {label}: {path}")
    value = read_text(path)
    if not value:
        raise ValueError(f"Fichier vide pour {label}: {path}")
    return value


def load_yaml_value(path: Path, key: str) -> str | None:
    if not path.exists():
        return None
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        current_key, value = line.split(":", 1)
        if current_key.strip() == key:
            return value.strip().strip('"\'')
    return None


def build_payload(author_urn: str, post_text: str) -> dict[str, object]:
    return {
        "author": author_urn,
        "commentary": post_text,
        "visibility": "PUBLIC",
        "distribution": {
            "feedDistribution": "MAIN_FEED",
            "targetEntities": [],
            "thirdPartyDistributionChannels": [],
        },
        "lifecycleState": "PUBLISHED",
        "isReshareDisabledByAuthor": False,
    }


def introspect_token(cred_dir: Path, token: str) -> dict[str, object] | None:
    auth_yaml = cred_dir / "linkedin_auth_keys.yaml"
    client_id = load_yaml_value(auth_yaml, "client_id")
    client_secret = load_yaml_value(auth_yaml, "client_secret")
    if not client_id or not client_secret:
        return None
    body = parse.urlencode({"client_id": client_id, "client_secret": client_secret, "token": token}).encode()
    req = request.Request(
        LINKEDIN_INTROSPECT_URL,
        data=body,
        method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    try:
        with request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception:
        return None


def post_to_linkedin(token: str, payload: dict[str, object]) -> dict[str, object]:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = request.Request(
        LINKEDIN_POSTS_URL,
        data=data,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "LinkedIn-Version": LINKEDIN_VERSION,
            "X-Restli-Protocol-Version": "2.0.0",
        },
    )
    try:
        with request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            return {
                "ok": 200 <= resp.status < 300,
                "status": resp.status,
                "headers": dict(resp.headers.items()),
                "body": body,
            }
    except error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        return {
            "ok": False,
            "status": exc.code,
            "headers": dict(exc.headers.items()),
            "body": body,
        }


def linkedin_url_from_id(post_id: str | None) -> str | None:
    if not post_id:
        return None
    return f"https://www.linkedin.com/feed/update/{post_id}/"


def write_result(draft: Path, result: dict[str, object]) -> Path:
    result_path = draft.parent / "linkedin-publish-result.json"
    result_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Publish a TSOS LinkedIn draft as a LinkedIn organization/page post.")
    parser.add_argument("draft", type=Path, help="Path to linkedin-post.md")
    parser.add_argument("--cred-dir", type=Path, default=Path(os.environ.get("TSOS_CRED_DIR", DEFAULT_CRED_DIR)))
    parser.add_argument("--organization-urn", default=os.environ.get("LINKEDIN_ORGANIZATION_URN"))
    parser.add_argument("--publish", action="store_true", help="Actually publish. Without this flag, dry-run only.")
    parser.add_argument("--check-token", action="store_true", help="Show non-secret token metadata such as active status and scopes.")
    args = parser.parse_args()

    draft = args.draft.resolve()
    if not draft.exists():
        raise FileNotFoundError(draft)

    token = load_secret(args.cred_dir / "linkedin_access_token.txt", "LinkedIn access token")
    organization_urn = args.organization_urn
    if not organization_urn:
        organization_urn = load_secret(args.cred_dir / "linkedin_organization_urn.txt", "LinkedIn organization URN")
    if not organization_urn.startswith("urn:li:organization:"):
        raise ValueError("L'URN organisation doit ressembler a urn:li:organization:123456")

    markdown = read_text(draft)
    meta, _ = parse_frontmatter(markdown)
    post_text = extract_post_text(markdown)
    payload = build_payload(organization_urn, post_text)
    token_info = introspect_token(args.cred_dir, token)

    if args.check_token:
        public_token_info = None
        if token_info:
            public_token_info = {
                "active": token_info.get("active"),
                "scope": token_info.get("scope"),
                "expires_at": token_info.get("expires_at"),
            }
        print(json.dumps(public_token_info, ensure_ascii=False, indent=2))
        return 0

    if not args.publish:
        preview = {
            "mode": "dry-run",
            "author": organization_urn,
            "draft": str(draft),
            "source_url": meta.get("source_url"),
            "text_length": len(post_text),
            "token_scope": token_info.get("scope") if token_info else None,
            "required_scope_for_organization": "w_organization_social",
            "payload": payload,
        }
        print(json.dumps(preview, ensure_ascii=False, indent=2))
        return 0

    api_result = post_to_linkedin(token, payload)
    headers = api_result.get("headers", {})
    post_id = headers.get("x-restli-id") if isinstance(headers, dict) else None
    result = {
        "platform": "LinkedIn",
        "publisher": "organization",
        "organization_urn": organization_urn,
        "draft": draft.relative_to(ROOT).as_posix() if draft.is_relative_to(ROOT) else str(draft),
        "source_url": meta.get("source_url"),
        "published_at": datetime.now(timezone.utc).isoformat(),
        "ok": api_result["ok"],
        "status": api_result["status"],
        "token_scope": token_info.get("scope") if token_info else None,
        "required_scope_for_organization": "w_organization_social",
        "post_id": post_id,
        "linkedin_url": linkedin_url_from_id(post_id),
        "api_body": api_result.get("body", ""),
    }
    result_path = write_result(draft, result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print(f"RESULT {result_path}")
    return 0 if api_result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
