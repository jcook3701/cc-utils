"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Command-line interface for ccutils.ccutils: Cookiecutter automation utilities.

Provides commands to:
  - extract: Clone a Cookiecutter template repo, clean
    its cookiecutter.json of Jinja placeholders, and save locally.
  - run: Render a Cookiecutter template using a pre-supplied JSON config file.
"""

from dataclasses import replace

import typer

from ccutils.cli.build import app as build_app
from ccutils.cli.config import app as config_app
from ccutils.core.config import ensure_config
from ccutils.core.logger import setup_logging
from ccutils.models import CLIConfig

from .commands import add_docs, extract, list as list_cmds, run, show_config

app = typer.Typer(help="CCUtils: Cookiecutter automation utilities")


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose logging"
    ),
) -> None:
    """
    Main CLI entrypoint for ccutils:
    Initialize configuration and logging for all subcommands.
    """
    # Ensure config exists and load it
    cfg: CLIConfig = ensure_config()

    # Override verbosity if CLI flag provided
    if verbose:
        cfg = replace(cfg, verbose=True)

    logger = setup_logging(cfg)

    logger.debug("Verbose mode enabled.")
    logger.debug(f"Loaded configuration: {cfg}")

    # Attach shared objects to context
    ctx.obj = {"cfg": cfg, "logger": logger}


# -----------------------------
# Register commands
# -----------------------------
# Docs command
# -----------------------------
app.command()(add_docs)
# -----------------------------
# Extract command
# -----------------------------
app.command()(extract)
# -----------------------------
# List commands
# -----------------------------
app.add_typer(list_cmds.app, name="list")
# -----------------------------
# Run command
# -----------------------------
app.command()(run)
# -----------------------------
# Config command:
# -----------------------------
app.add_typer(config_app, name="config")
# -----------------------------
# Build commands
# -----------------------------
app.add_typer(build_app, name="build")

# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    app()
