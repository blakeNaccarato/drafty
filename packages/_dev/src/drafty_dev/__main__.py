"""Command-line interface."""

from cappa.base import command, invoke
from cappa.subcommand import Subcommands

from drafty_dev.cli import ElevatePyrightWarnings


@command(invoke="drafty_dev.tools.add_change")
class AddChange:
    """Add change."""


@command(invoke="drafty_dev.tools.get_actions")
class GetActions:
    """Get actions used by this repository."""


@command(invoke="drafty_dev.tools.sync_local_dev_configs")
class SyncLocalDevConfigs:
    """Synchronize local dev configs."""


@command()
class Dev:
    """Dev tools."""

    commands: Subcommands[
        AddChange | GetActions | SyncLocalDevConfigs | ElevatePyrightWarnings
    ]


def main():
    """CLI entry-point."""
    invoke(Dev)


if __name__ == "__main__":
    main()
