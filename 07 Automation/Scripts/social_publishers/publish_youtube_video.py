from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CRED_DIR = Path(
    r"C:\Users\MOULO Oholo Jean\OneDrive - Institut National Polytechnique Félix HOUPHOUËT-BOIGNY - INP-HB\PROJETS\TS\cred"
)
YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
VALID_PRIVACY = {"private", "unlisted", "public"}


def require_google_libs():
    try:
        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request
        from googleapiclient.discovery import build
        from googleapiclient.errors import HttpError
        from googleapiclient.http import MediaFileUpload
    except ImportError as exc:
        raise SystemExit(
            "Missing YouTube upload dependencies. Install them with:\n"
            "python -m pip install google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2\n"
            f"Original error: {exc}"
        )
    return Credentials, Request, build, HttpError, MediaFileUpload


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


def body_without_heading(markdown: str, heading: str) -> str:
    _, body = parse_frontmatter(markdown)
    lines = []
    for line in body.splitlines():
        if line.strip() == heading:
            continue
        lines.append(line.rstrip())
    text = "\n".join(lines).strip()
    return re.sub(r"\n{3,}", "\n\n", text)


def load_metadata(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(read_text(path))


def resolve_pack_path(pack_dir: Path, value: str | None) -> Path | None:
    if not value:
        return None
    path = Path(value)
    if not path.is_absolute():
        path = pack_dir / path
    return path.resolve()


def load_description(pack_dir: Path, metadata: dict[str, object]) -> str:
    description_file = resolve_pack_path(pack_dir, str(metadata.get("description_file") or ""))
    if description_file and description_file.exists():
        return body_without_heading(read_text(description_file), "# YouTube Description")
    return str(metadata.get("description") or "").strip()


def build_video_resource(metadata: dict[str, object], description: str) -> dict[str, object]:
    privacy = str(metadata.get("privacyStatus") or "unlisted")
    if privacy not in VALID_PRIVACY:
        raise ValueError(f"privacyStatus invalide: {privacy}. Valeurs: {sorted(VALID_PRIVACY)}")
    tags = metadata.get("tags") or []
    if not isinstance(tags, list):
        tags = [str(tags)]
    made_for_kids = bool(metadata.get("madeForKids", False))
    return {
        "snippet": {
            "title": str(metadata.get("title") or "TianSemi video"),
            "description": description,
            "tags": [str(tag) for tag in tags],
            "categoryId": str(metadata.get("categoryId") or "27"),
            "defaultLanguage": str(metadata.get("language") or "fr"),
            "defaultAudioLanguage": str(metadata.get("language") or "fr"),
        },
        "status": {
            "privacyStatus": privacy,
            "selfDeclaredMadeForKids": made_for_kids,
        },
    }


def get_youtube_service(cred_dir: Path):
    Credentials, Request, build, _, _ = require_google_libs()
    token_file = cred_dir / "youtube_token.json"
    client_file = cred_dir / "youtube_oauth_client.json"
    if not token_file.exists():
        raise FileNotFoundError(f"Token YouTube introuvable: {token_file}")
    if not client_file.exists():
        raise FileNotFoundError(f"OAuth client YouTube introuvable: {client_file}")
    creds = Credentials.from_authorized_user_file(str(token_file), scopes=[YOUTUBE_UPLOAD_SCOPE])
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        token_file.write_text(creds.to_json(), encoding="utf-8")
    if not creds.valid:
        raise RuntimeError("Credentials YouTube invalides. Regenerer youtube_token.json avec le scope youtube.upload.")
    return build("youtube", "v3", credentials=creds)


def upload_video(youtube, video_file: Path, body: dict[str, object]):
    _, _, _, _, MediaFileUpload = require_google_libs()
    media = MediaFileUpload(str(video_file), chunksize=-1, resumable=True)
    request_obj = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media,
    )
    response = None
    while response is None:
        status, response = request_obj.next_chunk()
        if status:
            print(f"UPLOAD_PROGRESS {int(status.progress() * 100)}%")
    return response


def upload_thumbnail(youtube, video_id: str, thumbnail_file: Path):
    _, _, _, _, MediaFileUpload = require_google_libs()
    media = MediaFileUpload(str(thumbnail_file), resumable=False)
    return youtube.thumbnails().set(videoId=video_id, media_body=media).execute()


def write_result(pack_dir: Path, result: dict[str, object]) -> Path:
    path = pack_dir / "youtube-publish-result.json"
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Publish a TSOS YouTube video from a social pack metadata file.")
    parser.add_argument("metadata", type=Path, help="Path to youtube-metadata.json")
    parser.add_argument("--cred-dir", type=Path, default=Path(os.environ.get("TSOS_CRED_DIR", DEFAULT_CRED_DIR)))
    parser.add_argument("--video-file", type=Path, help="Video file to upload. Overrides metadata.video_file.")
    parser.add_argument("--thumbnail-file", type=Path, help="Thumbnail file. Overrides metadata.thumbnail_file.")
    parser.add_argument("--privacy-status", choices=sorted(VALID_PRIVACY), help="Override privacyStatus.")
    parser.add_argument("--publish", action="store_true", help="Actually upload. Without this flag, dry-run only.")
    args = parser.parse_args()

    metadata_path = args.metadata.resolve()
    pack_dir = metadata_path.parent
    metadata = load_metadata(metadata_path)
    if args.privacy_status:
        metadata["privacyStatus"] = args.privacy_status

    description = load_description(pack_dir, metadata)
    body = build_video_resource(metadata, description)

    video_file = args.video_file.resolve() if args.video_file else resolve_pack_path(pack_dir, str(metadata.get("video_file") or ""))
    thumbnail_file = args.thumbnail_file.resolve() if args.thumbnail_file else resolve_pack_path(pack_dir, str(metadata.get("thumbnail_file") or ""))

    preview = {
        "mode": "dry-run" if not args.publish else "publish",
        "metadata": str(metadata_path),
        "video_file": str(video_file) if video_file else None,
        "thumbnail_file": str(thumbnail_file) if thumbnail_file else None,
        "body": body,
        "credential_files_present": {
            "youtube_oauth_client.json": (args.cred_dir / "youtube_oauth_client.json").exists(),
            "youtube_token.json": (args.cred_dir / "youtube_token.json").exists(),
        },
    }

    if not args.publish:
        print(json.dumps(preview, ensure_ascii=False, indent=2))
        return 0

    if not video_file or not video_file.exists():
        raise FileNotFoundError("Fichier video requis pour publier. Fournir --video-file ou metadata.video_file.")

    youtube = get_youtube_service(args.cred_dir)
    response = upload_video(youtube, video_file, body)
    video_id = response.get("id")
    thumbnail_response = None
    if thumbnail_file and thumbnail_file.exists() and video_id:
        thumbnail_response = upload_thumbnail(youtube, video_id, thumbnail_file)

    result = {
        "platform": "YouTube",
        "published_at": datetime.now(timezone.utc).isoformat(),
        "ok": bool(video_id),
        "video_id": video_id,
        "youtube_url": f"https://www.youtube.com/watch?v={video_id}" if video_id else None,
        "privacyStatus": body["status"]["privacyStatus"],
        "thumbnail_uploaded": thumbnail_response is not None,
        "api_response": response,
    }
    result_path = write_result(pack_dir, result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print(f"RESULT {result_path}")
    return 0 if video_id else 1


if __name__ == "__main__":
    raise SystemExit(main())
