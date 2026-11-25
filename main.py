"""News-image entry for make.fun bounty news-image-20261125.

Copies the bundled entry.png (a newspaper front page summing up Wednesday
25 November 2026) to /output/entry.png. Before copying it checks the source
is a real JPEG (magic bytes FF D8 FF), and after copying it confirms the
destination exists and matches the source byte-for-byte in size, so a
corrupt source or a truncated write fails loudly instead of shipping a bad
image. Deterministic: the same input bytes produce the same output bytes on
every run. No network, no randomness, no arguments. Python 3.13 standard
library only.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


JPEG_MAGIC = b"\xff\xd8\xff"


def main():
    with open(SRC, "rb") as f:
        magic = f.read(3)
    if magic != JPEG_MAGIC:
        raise ValueError(
            f"entry.png is not a JPEG (magic bytes {magic.hex()}, "
            "expected ffd8ff)"
        )
    src_size = os.path.getsize(SRC)
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    dst_size = os.path.getsize(DST)
    if dst_size != src_size:
        raise ValueError(
            f"copied entry.png is {dst_size} bytes, expected {src_size}"
        )


if __name__ == "__main__":
    main()
