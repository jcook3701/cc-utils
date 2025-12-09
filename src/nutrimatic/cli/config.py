"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Command-line interface for Cookiecutter configuration utilities.
"""

import typer

from nutrimatic.core.config import ensure_config
from nutrimatic.models import CLIConfig

from .commands.nmconfig import show_config
from .options import verbose_mode

app = typer.Typer(help="nutri-matic configuration tools.")


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose logging"
    ),
) -> None:
    """
    Main CLI entrypoint for nutri-matic configuration:
    Initialize configuration and logging for all subcommands.
    """
    # Ensure config exists and load it
    cfg: CLIConfig = ensure_config()

    # Attach shared objects to context
    ctx.obj = verbose_mode(cfg, verbose)


# -----------------------------
# Register commands
# -----------------------------
# nm-config commands:
# -----------------------------
app.command(name="show")(show_config)
# -----------------------------


# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    app()
