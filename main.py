#!/usr/bin/env python3
"""Entry for the make.fun bounty "Sum up 21 November's world news in one image".

Copies the bundled news.png to /output/entry.png. The program uses no
network and is fully deterministic: running it any number of times
produces byte-identical output.

The output directory defaults to /output and can be overridden with the
ENTRY_OUTPUT_DIR environment variable (used only for local testing).
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    source = Path(__file__).resolve().parent / "news.png"
    output_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, output_dir / "entry.png")


if __name__ == "__main__":
    main()
