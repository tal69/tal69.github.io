#!/usr/bin/env python3
"""
Mirror PDFs and the profile photo from the old Wix site into this repo, then
rewrite _data/publications.yml to point at the local copies.

Run from the repo root:

    python3 scripts/mirror_assets.py

Re-runnable: skips files that already exist.
"""

from __future__ import annotations

import hashlib
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

REPO       = Path(__file__).resolve().parent.parent
PDF_DIR    = REPO / "assets" / "pdf"
IMG_DIR    = REPO / "assets" / "img"
PUBS_FILE  = REPO / "_data" / "publications.yml"

# Wix serves uploaded files from two hosts:
#   - static.wixstatic.com/...                            (older media)
#   - <subdomain>.sites.tau.ac.il/_files/{ugd,archives}/  (custom domains)
ASSET_URL_RE = re.compile(
    r"https://"                                   # scheme
    r"(?:static\.wixstatic\.com/[^\s\"<>)]+"      # wix CDN
    r"|[\w.-]+/_files/[^\s\"<>)]+)"               # any host serving /_files/
    r"\.(?:pdf|doc|docx|zip|rar)",                # asset extensions
    flags=re.IGNORECASE,
)

# The profile photo (cropped, 547 px high) from the Wix home page.
PROFILE_PHOTO = ("https://static.wixstatic.com/media/"
                 "e6d0a7_591e4da4686940a9ac418e171d419d93~mv2.jpg/v1/crop/"
                 "x_0,y_72,w_1478,h_2078/fill/w_778,h_1094,al_c,q_85/"
                 "talraviv.jpg")


def download(url: str, dest: Path) -> bool:
    """Download `url` to `dest`. Return True if a download happened."""
    if dest.exists() and dest.stat().st_size > 0:
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    print(f"  fetch  {url}")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as r, open(dest, "wb") as f:
        f.write(r.read())
    print(f"   -> {dest.relative_to(REPO)}  ({dest.stat().st_size:,} B)")
    return True


def local_name_for(url: str) -> str:
    """Pick a stable local filename for a remote asset URL."""
    parsed = urllib.parse.urlparse(url)
    base   = os.path.basename(parsed.path)
    # Wix CDN paths are like /media/f40624_<hash>.pdf — already unique.
    # Fall back to a hash if we ever encounter a colliding name.
    if base and base.lower().endswith((".pdf", ".doc", ".docx", ".zip", ".rar")):
        return base
    digest = hashlib.sha1(url.encode()).hexdigest()[:12]
    ext    = os.path.splitext(base)[1] or ".bin"
    return f"{digest}{ext}"


def mirror_pdfs(text: str) -> tuple[str, int, int]:
    """Replace Wix PDF/doc/zip URLs in `text` with local paths after download."""
    new_text   = text
    fetched    = 0
    skipped    = 0
    seen: dict[str, str] = {}  # url -> local web path
    for match in ASSET_URL_RE.findall(text):
        if match in seen:
            local = seen[match]
        else:
            name  = local_name_for(match)
            dest  = PDF_DIR / name
            try:
                if download(match, dest):
                    fetched += 1
                else:
                    skipped += 1
                local = f"/assets/pdf/{name}"
            except Exception as exc:
                print(f"  !! failed: {match}\n     {exc}")
                continue
            seen[match] = local
        new_text = new_text.replace(match, local)
    return new_text, fetched, skipped


def main() -> int:
    print(f"Repo root: {REPO}")

    # 1. profile photo
    try:
        download(PROFILE_PHOTO, IMG_DIR / "profile.jpg")
    except Exception as exc:
        print(f"  !! profile photo failed: {exc}")

    # 2. publication PDFs (rewrite YAML)
    if not PUBS_FILE.exists():
        print(f"!! {PUBS_FILE} not found; skipping PDF mirroring.")
        return 1

    original  = PUBS_FILE.read_text(encoding="utf-8")
    updated, fetched, skipped = mirror_pdfs(original)
    if updated != original:
        backup = PUBS_FILE.with_suffix(".yml.bak")
        if not backup.exists():
            backup.write_text(original, encoding="utf-8")
            print(f"  backup written to {backup.relative_to(REPO)}")
        PUBS_FILE.write_text(updated, encoding="utf-8")
        print(f"  rewrote {PUBS_FILE.relative_to(REPO)} "
              f"({fetched} new, {skipped} already on disk)")
    else:
        print("  nothing to rewrite in publications.yml")

    return 0


if __name__ == "__main__":
    sys.exit(main())
