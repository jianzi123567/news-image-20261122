#!/usr/bin/env python3
"""news-image-20261122: emit the bundled 22 November 2026 news image.

The repository ships entry.png, a 1024x1024 JPEG summing up the day's
world news. This program copies those bytes to the output directory.
It performs no network access, reads no clock and uses no randomness,
so repeated runs always write identical bytes.
"""

import os
from pathlib import Path

ENTRY = "entry.png"
LIMIT = 1_048_576


def load_entry():
    """Read the bundled image and check it is a small JPEG or PNG."""
    path = Path(__file__).resolve().parent / ENTRY
    try:
        data = path.read_bytes()
    except FileNotFoundError:
        raise SystemExit(f"{ENTRY} is missing from the repository")
    if not data:
        raise SystemExit(f"{ENTRY} is empty")
    if len(data) > LIMIT:
        raise SystemExit(f"{ENTRY} is over the 1 MiB limit")
    jpeg = data[:2] == b"\xff\xd8"
    png = data[:8] == b"\x89PNG\r\n\x1a\n"
    if not jpeg and not png:
        raise SystemExit(f"{ENTRY} is not a JPEG or PNG image")
    return data


def main():
    data = load_entry()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / ENTRY
    target.write_bytes(data)
    if target.read_bytes() != data:
        raise SystemExit("output copy does not match the source")
    print(f"wrote {target} ({len(data)} bytes)")


if __name__ == "__main__":
    main()
