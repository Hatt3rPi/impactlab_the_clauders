"""Wrapper conveniente: `python tools/deep-research/run.py <slug>`."""
from client import main
import sys

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
