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

from ccutils.commands import add_docs, extract, list as list_cmds, run

app = typer.Typer(help="CCUtils: Cookiecutter automation utilities")

# -----------------------------
# Docs command
# -----------------------------
app.command()(add_docs)

# -----------------------------
# Extract command
# -----------------------------
app.command()(extract)

# -----------------------------
# List command
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
