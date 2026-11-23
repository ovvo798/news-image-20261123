#!/usr/bin/env python3
"""Write the competition entry image to entry.png.

Simplest correct program: copy the repo-held entry.png to
/output/entry.png, or to $MAKEFUN_OUTPUT_DIR/entry.png when that
environment variable is set. Deterministic (byte-identical on
every run), no network access, no extra dependencies (Python 3
standard library). After copying, the written file's byte size is
checked against the source and a mismatch raises an error.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DEFAULT_OUTPUT_DIR = "/output"


def output_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    return os.path.join(out_dir, "entry.png")


def main():
    dst = output_path()
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(SRC, dst)
    src_size = os.path.getsize(SRC)
    dst_size = os.path.getsize(dst)
    if dst_size != src_size:
        raise RuntimeError(
            "size mismatch after copy: source %d bytes, wrote %d bytes to %s"
            % (src_size, dst_size, dst)
        )
    print("Wrote " + dst + " (%d bytes)" % dst_size)


if __name__ == "__main__":
    main()
