"""Command-line interface."""

from drafty_pipeline.cli import Pipeline
from drafty_pipeline.parser import invoke


def main():
    """CLI entry-point."""
    invoke(Pipeline)


if __name__ == "__main__":
    main()
