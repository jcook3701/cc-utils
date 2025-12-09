"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Command-line interface for Cookiecutter template utilities.
"""

import typer

from nutrimatic.core.config import ensure_config
from nutrimatic.models import CLIConfig

from .commands.nmtemplates import generate
from .options import verbose_mode

app = typer.Typer(help="nm-templates tools.")


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose logging"
    ),
) -> None:
    """
    Main CLI entrypoint for nutri-matic templates:
    Initialize configuration and logging for all subcommands.
    """
    # Ensure config exists and load it
    cfg: CLIConfig = ensure_config()

    # Attach shared objects to context
    ctx.obj = verbose_mode(cfg, verbose)


# -----------------------------
# Register commands
# -----------------------------
# nm-templates commands:
# -----------------------------
app.command()(generate)
# -----------------------------


# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    app()
