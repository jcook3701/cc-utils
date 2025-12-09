"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Command-line interface for Cookiecutter build automation utilities.
"""

import typer

from nutrimatic.core.config import ensure_config
from nutrimatic.models import CLIConfig

from .commands.nmbuild import add_yaml_front_matter, build_readme
from .options import verbose_mode

app = typer.Typer(help="Cookiecutter build automation utilities.")


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose logging"
    ),
) -> None:
    """
    Main CLI entrypoint for nutri-matic build:
    Initialize configuration and logging for all subcommands.
    """
    # Ensure config exists and load it
    cfg: CLIConfig = ensure_config()

    # Attach shared objects to context
    ctx.obj = verbose_mode(cfg, verbose)


# -----------------------------
# Register commands:
# -----------------------------
# nm-build Command:
# -----------------------------
app.command(name="readme")(build_readme)
app.command()(add_yaml_front_matter)
# -----------------------------


# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    app()
