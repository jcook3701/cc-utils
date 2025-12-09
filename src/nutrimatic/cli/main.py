"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Command-line interface Cookiecutter automation utilities.

Provides commands to:
  - extract: Clone a Cookiecutter template repo, clean
    its cookiecutter.json of Jinja placeholders, and save locally.
  - run: Render a Cookiecutter template using a pre-supplied JSON config file.
"""

import typer

from nutrimatic.cli.build import app as build_app
from nutrimatic.cli.config import app as config_app
from nutrimatic.cli.templates import app as template_app
from nutrimatic.core.config import ensure_config
from nutrimatic.models import CLIConfig

from .commands.nmutils import add_docs, extract, list as list_cmds, run
from .options import verbose_mode, version_mode

app = typer.Typer(help="Nutri-Matic: Cookiecutter automation utilities")


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose logging."
    ),
    version: bool = typer.Option(
        None,
        "--version",
        "-V",
        callback=version_mode,
        help="Show the Nutri-Matic version.",
    ),
) -> None:
    """
    Main CLI entrypoint for nutri-matic Cookiecutter utilities:
    Initialize configuration and logging for all subcommands.
    """
    # Ensure config exists and load it
    cfg: CLIConfig = ensure_config()

    # Attach shared objects to context
    ctx.obj = verbose_mode(cfg, verbose)


# -----------------------------
# Register commands
# -----------------------------
# nm-util commands:
# -----------------------------
app.command()(add_docs)
app.command()(extract)
app.add_typer(list_cmds.app, name="list")
app.command()(run)
# -----------------------------
# nm-config commands:
# -----------------------------
app.add_typer(config_app, name="config")
# -----------------------------
# nm-build commands:
# -----------------------------
app.add_typer(build_app, name="build")
# -----------------------------
# nm-templates commands:
# -----------------------------
app.add_typer(template_app, name="template")

# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    app()
