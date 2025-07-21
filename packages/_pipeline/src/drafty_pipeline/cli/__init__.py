"""Command-line interface."""

from __future__ import annotations

from dataclasses import dataclass

from cappa.base import command
from cappa.subcommand import Subcommands
from pipeline_helper.sync_dvc import SyncDvc

from drafty_pipeline.stages.example import Example


@dataclass
class Stage:
    """Run a pipeline stage."""

    commands: Subcommands[Example]


@command(name="drafty-pipeline")
class Pipeline:
    """Run the research data pipeline."""

    commands: Subcommands[SyncDvc | Stage]
