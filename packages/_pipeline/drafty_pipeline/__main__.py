"""Command-line interface."""

from cappa import invoke

from drafty_pipeline.cli import Pipeline


def main():
    """CLI entry-point."""
    invoke(Pipeline)


if __name__ == "__main__":
    main()
