"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Command-line interface for ccutils.config: Cookiecutter configuration utilities.
"""
from dataclasses import replace

import typer

from ccutils.core.config import ensure_config
from ccutils.core.logger import setup_logging
from ccutils.models import CLIConfig

from .commands import show_config

app = typer.Typer(help="ccutils configuration tools.")


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
# Config commands:
# -----------------------------
app.command(name="show")(show_config)
# -----------------------------

# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    app()
