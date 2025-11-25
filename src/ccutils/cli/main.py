"""cc-utils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Command-line interface for ccutils.ccutils: Cookiecutter automation utilities.

Provides commands to:
  - extract: Clone a Cookiecutter template repo, clean
    its cookiecutter.json of Jinja placeholders, and save locally.
  - run: Render a Cookiecutter template using a pre-supplied JSON config file.
"""

import typer

from ccutils.cli.build import app as build_app
from ccutils.cli.config import app as config_app
from ccutils.cli.templates import app as template_app
from ccutils.core.config import ensure_config
from ccutils.models import CLIConfig

from .commands.ccutils import add_docs, extract, list as list_cmds, run
from .options import verbose_mode, version_mode

app = typer.Typer(help="CC-Utils: Cookiecutter automation utilities")


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
        help="Show the cc-utils version.",
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
# cc-util commands:
# -----------------------------
app.command()(add_docs)
app.command()(extract)
app.add_typer(list_cmds.app, name="list")
app.command()(run)
# -----------------------------
# cc-config commands:
# -----------------------------
app.add_typer(config_app, name="config")
# -----------------------------
# cc-build commands:
# -----------------------------
app.add_typer(build_app, name="build")
# -----------------------------
# cc-templates commands:
# -----------------------------
app.add_typer(template_app, name="template")

# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    app()
