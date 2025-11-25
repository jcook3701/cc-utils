"""cc-utils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Command-line interface for ccutils.template: Cookiecutter configuration utilities.
"""

import typer

from ccutils.core.config import ensure_config
from ccutils.models import CLIConfig

from .commands.cctemplates import generate
from .options import verbose_mode

app = typer.Typer(help="cc-templates tools.")


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose logging"
    ),
) -> None:
    """
    Main CLI entrypoint for cc-utils:
    Initialize configuration and logging for all subcommands.
    """
    # Ensure config exists and load it
    cfg: CLIConfig = ensure_config()

    # Attach shared objects to context
    ctx.obj = verbose_mode(cfg, verbose)


# -----------------------------
# Register commands
# -----------------------------
# cctemplates commands:
# -----------------------------
app.command()(generate)
# -----------------------------


# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    app()
