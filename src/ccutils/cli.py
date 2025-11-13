"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Command-line interface for CCUtils: Cookiecutter automation utilities.

Provides commands to:
  - extract: Clone a Cookiecutter template repo, clean
    its cookiecutter.json of Jinja placeholders, and save locally.
  - run: Render a Cookiecutter template using a pre-supplied JSON config file.
"""

import typer

from .commands import add_docs, extract, list as list_cmds, run
from .core.config import ensure_config
from .core.logger import setup_logging
from .core.models import CLIConfig

app = typer.Typer(help="CCUtils: Cookiecutter automation utilities")


@app.callback()
def main(verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose logging")) -> None:
    """
    Main CLI entrypoint for ccutils:
    Initialize configuration and logging for all subcommands.
    """
    # Ensure config exists and load it
    config: CLIConfig = ensure_config()

    # Prefer CLI flag, fallback to config file setting
    verbose_mode: bool = verbose if verbose else config.verbose

    logger = setup_logging(config, verbose_mode)

    logger.debug("Verbose mode enabled.")
    logger.debug(f"Loaded configuration: {config}")

   # Store config in Typer context for subcommands to access
    typer.get_app_dir("ccutils")
    typer.get_current_context().obj = {"config": config, "verbose": verbose_mode} # type: ignore[attr-defined]

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
# Entry point
# -----------------------------
if __name__ == "__main__":
    app()
