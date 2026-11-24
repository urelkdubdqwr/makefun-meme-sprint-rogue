import os
import sys


def main():
    program_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(program_dir, "meme.png")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)

    with open(source_path, "rb") as source:
        data = source.read()

    with open(os.path.join(output_dir, "entry.png"), "wb") as destination:
        destination.write(data)

    return 0


if __name__ == "__main__":
    sys.exit(main())
