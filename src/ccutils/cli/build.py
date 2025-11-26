"""cc-utils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Command-line interface for ccutils.build: Cookiecutter build automation utilities.
"""

import typer

from ccutils.core.config import ensure_config
from ccutils.models import CLIConfig

from .commands.ccbuild import add_yaml_front_matter, build_readme
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
    Main CLI entrypoint for cc-utils:
    Initialize configuration and logging for all subcommands.
    """
    # Ensure config exists and load it
    cfg: CLIConfig = ensure_config()

    # Attach shared objects to context
    ctx.obj = verbose_mode(cfg, verbose)


# -----------------------------
# Register commands:
# -----------------------------
# cc-build Command:
# -----------------------------
app.command(name="readme")(build_readme)
app.command()(add_yaml_front_matter)
# -----------------------------


# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    app()
