#!/usr/bin/env python3
"""Write the make.fun entry ("Obviously") to <output dir>/entry.txt.

The output directory is $MAKEFUN_OUTPUT_DIR when set and non-empty,
otherwise the literal directory /output. The file is UTF-8 text and the
entry is followed by exactly one trailing newline.
"""
import os

ENTRY = "Obviously"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(output_dir, exist_ok=True)

with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as fh:
    fh.write(ENTRY + "\n")
