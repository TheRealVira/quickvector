"""Module provides functionality to quickly vectorize images."""
import argparse
import os
from pathlib import Path
from svgtrace import trace

parser = argparse.ArgumentParser(
    "quickvector",
    description="A script to vectorize your images.",
    epilog="And that's how you'd use quickvector.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument("--source", help="Source file.", required=True)
parser.add_argument(
    "--color",
    default=False,
    action=argparse.BooleanOptionalAction,
    help="If defined, exports svg in colors.",
)

args = parser.parse_args()


if __name__ == "__main__":
    infile = os.path.abspath(args.source)
    filename = Path(infile).stem
    outfile = os.path.abspath(f"./out/{filename}.svg")

    print("Tracing...")
    print(args.color)
    path = trace(infile, not args.color)

    print(f"Saving {infile} to {outfile} ...")
    Path(outfile).write_text(path, encoding="utf-8")

    print("Done!")
