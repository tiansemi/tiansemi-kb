from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CRED_DIR = Path(
    r"C:\Users\MOULO Oholo Jean\OneDrive - Institut National Polytechnique Félix HOUPHOUËT-BOIGNY - INP-HB\PROJETS\TS\cred"
)
LINKEDIN_UGC_ENDPOINT = "https://api.linkedin.com/v2/ugcPosts"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def read_secret(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Secret file not found: {path}")
    return path.read_text(encoding="utf-8-sig").strip()


def mask_secret(value: str, visible: int = 6) -> str:
    if len(value) <= visible * 2:
        return "***"
    return f"{value[:visible]}...{value[-visible:]}"


def parse_frontmatter(markdown: str) -> tuple[dict[str, object], str]:
    text = markdown.lstrip("\ufeff")
    if not text.startswith("---\n"):
        return {}, text.strip()

    end = text.find("\n---", 4)
    if end == -1:
        return {}, text.strip()

    raw_frontmatter = text[4:end].strip().splitlines()
    body = text[end + 5 :].strip()
    data: dict[str, object] = {}
    current_key: str | None = None

    for line in raw_frontmatter:
        stripped = line.strip()
        if stripped.startswith("- ") and current_key:
            existing = data.get(current_key)
            if not isinstance(existing, list):
                existing = []
                data[current_key] = existing
            existing.append(stripped[2:].strip().strip('"\''))
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        current_key = key.strip()
        value = value.strip()
        if value == "":
            data[current_key] = ""
        elif value.startswith("[") and value.endswith("]"):
            data[current_key] = []
        else:
            data[current_key] = value.strip('"\'')

    return data, body


def markdown_to_linkedin_text(body: str) -> str:
    lines = []
    for line in body.splitlines():
        stripped = line.strip()
        if stripped == "# LinkedIn Post":
            continue
        if stripped.startswith("---"):
            continue
        lines.append(line.rstrip())

    text = "\n".join(lines).strip()
    while "\n\n\n" in text:
        text = text.replace("\n\n\n", "\n\n")
    return text


def find_latest_linkedin_draft(root: Path) -> Path:
    search_root = root / "03 Content" / "Social Media" / "Huawei" / "HCIA-Datacom"
    candidates = list(search_root.rglob("linkedin-post.md"))
    if not candidates:
        raise FileNotFoundError(f"No linkedin-post.md found under {search_root}")
    return max(candidates, key=lambda path: path.stat().st_mtime)


def linkedin_payload(
    *,
    person_urn: str,
    text: str,
    source_url: str,
    title: str,
    description: str,
    visibility: str,
    text_only: bool,
) -> dict[str, object]:
    share_content: dict[str, object] = {
        "shareCommentary": {"text": text},
        "shareMediaCategory": "NONE",
    }

    if source_url and not text_only:
        share_content["shareMediaCategory"] = "ARTICLE"
        share_content["media"] = [
            {
                "status": "READY",
                "originalUrl": source_url,
                "title": {"text": title[:200]},
                "description": {"text": description[:256]},
            }
        ]

    return {
        "author": person_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": share_content,
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": visibility,
        },
    }


def publish_to_linkedin(payload: dict[str, object], token: str) -> tuple[int, str, str]:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = Request(
        LINKEDIN_UGC_ENDPOINT,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0",
        },
    )

    try:
        with urlopen(request, timeout=30) as response:
            status = response.status
            response_body = response.read().decode("utf-8", errors="replace")
            post_id = response.headers.get("X-RestLi-Id", "")
            return status, post_id, response_body
    except HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"LinkedIn API error {exc.code}: {error_body}") from exc
    except URLError as exc:
        raise RuntimeError(f"LinkedIn network error: {exc.reason}") from exc


def write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Publish or dry-run a LinkedIn post from a TSOS linkedin-post.md draft."
    )
    parser.add_argument(
        "draft",
        nargs="?",
        type=Path,
        help="Path to linkedin-post.md. Defaults to the latest Huawei HCIA-Datacom draft.",
    )
    parser.add_argument(
        "--cred-dir",
        type=Path,
        default=Path(os.environ.get("TSOS_CRED_DIR", DEFAULT_CRED_DIR)),
        help="Directory containing linkedin_access_token.txt and linkedin_person_urn.txt.",
    )
    parser.add_argument(
        "--visibility",
        choices=["PUBLIC", "CONNECTIONS"],
        default="PUBLIC",
        help="LinkedIn network visibility for the post.",
    )
    parser.add_argument(
        "--text-only",
        action="store_true",
        help="Publish as text only instead of attaching the source URL as an article.",
    )
    parser.add_argument(
        "--payload-out",
        type=Path,
        help="Optional path where the JSON payload should be saved.",
    )
    parser.add_argument(
        "--publish",
        action="store_true",
        help="Actually publish to LinkedIn. Without this flag, only a dry-run is performed.",
    )
    parser.add_argument(
        "--allow-non-person-author",
        action="store_true",
        help="Allow publishing when the author URN is not urn:li:person:*. Use only if your app/token is configured for organization posting.",
    )
    args = parser.parse_args()

    draft = args.draft or find_latest_linkedin_draft(ROOT)
    if not draft.is_absolute():
        draft = (ROOT / draft).resolve()

    cred_dir = args.cred_dir
    token_path = cred_dir / "linkedin_access_token.txt"
    person_urn_path = cred_dir / "linkedin_person_urn.txt"

    token = read_secret(token_path)
    person_urn = read_secret(person_urn_path)
    meta, body = parse_frontmatter(read_text(draft))
    post_text = markdown_to_linkedin_text(body)
    source_url = str(meta.get("source_url", "")).strip()
    title = "TianSemi HCIA-Datacom"
    description = "Ressource TianSemi pour progresser en Huawei HCIA-Datacom."

    author_is_person = person_urn.startswith("urn:li:person:")
    if not author_is_person:
        print(
            "WARNING: linkedin_person_urn.txt does not contain a member URN "
            "(expected urn:li:person:*)."
        )
        print(
            "Current value looks like an organization/company author. "
            "Dry-run is allowed, but publishing requires --allow-non-person-author."
        )
        if args.publish and not args.allow_non_person_author:
            raise SystemExit(
                "Refusing to publish with a non-person author URN. "
                "Use --allow-non-person-author only after confirming LinkedIn organization permissions."
            )

    payload = linkedin_payload(
        person_urn=person_urn,
        text=post_text,
        source_url=source_url,
        title=title,
        description=description,
        visibility=args.visibility,
        text_only=args.text_only,
    )

    if args.payload_out:
        out = args.payload_out if args.payload_out.is_absolute() else (ROOT / args.payload_out)
        write_json(out, payload)
        print(f"Payload saved: {out}")

    print("LinkedIn publisher")
    print(f"Mode: {'PUBLISH' if args.publish else 'DRY-RUN'}")
    print(f"Draft: {draft}")
    print(f"Credential directory: {cred_dir}")
    print(f"Author URN: {person_urn}")
    print(f"Access token: {mask_secret(token)}")
    print(f"Visibility: {args.visibility}")
    print(f"Share media category: {payload['specificContent']['com.linkedin.ugc.ShareContent']['shareMediaCategory']}")
    print(f"Source URL: {source_url or '(none)'}")
    print("\n--- Post text preview ---\n")
    print(post_text)
    print("\n--- End preview ---")

    if not args.publish:
        print("\nDry-run only. Add --publish to create the LinkedIn post.")
        return 0

    status, post_id, response_body = publish_to_linkedin(payload, token)
    print(f"\nPublished to LinkedIn. HTTP status: {status}")
    if post_id:
        print(f"LinkedIn post id: {post_id}")
    if response_body:
        print(response_body)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())



