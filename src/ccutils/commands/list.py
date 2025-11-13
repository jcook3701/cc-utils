"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

import typer

from ccutils.core import Namespace
from ccutils.core.github import fetch_namespace

app = typer.Typer(help="List available cookiecutter templates under a namespace.")


@app.command("namespace")
def list_namespace(
        namespace: str = typer.Argument(..., help="GitHub username or organization to search for templates"),
) -> None:
    """List all available cookiecutter templates in a GitHub namespace."""
    ns: Namespace = fetch_namespace(namespace)
    if not ns.templates:
        typer.echo(f"No templates found under '{namespace}'")
        return

    typer.echo(f"Templates under {namespace}:\n")
    for template in ns.templates:
        cfg = template.config
        typer.echo(
            f"- {template.repo.name}: {cfg.description if cfg else 'No description'} by {cfg.author if cfg else 'Unknown'}"
        )
