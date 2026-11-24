"""Copy the shipped meme image next to this program into the output directory.

Reads ``meme.png`` from the directory containing this program file and writes
the exact same bytes to ``entry.png`` inside ``MAKEFUN_OUTPUT_DIR`` (or
``/output`` when that environment variable is unset or empty). Creates the
output directory if needed and exits 0 on success.
"""

import os
import sys


def main():
    program_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(program_dir, "meme.png")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as error:
        print(f"error: cannot create output directory {output_dir!r}: {error}", file=sys.stderr)
        return 1

    with open(source_path, "rb") as source:
        data = source.read()

    with open(os.path.join(output_dir, "entry.png"), "wb") as destination:
        destination.write(data)

    return 0


if __name__ == "__main__":
    sys.exit(main())
