"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

import typer

from ccutils.core.github import fetch_namespace
from ccutils.models import Namespace

app = typer.Typer(help="List available cookiecutter templates under a namespace.")


def list_namespace(
    ctx: typer.Context,
    namespace: str = typer.Argument(
        ..., help="GitHub username or organization to search for templates"
    ),
) -> None:
    """List all available cookiecutter templates in a GitHub namespace."""
    logger = ctx.obj["logger"]
    # cfg = ctx.obj["cfg"] NOTE: Need to differentiate between this and cookiecutter.json configuration file.

    ns: Namespace = fetch_namespace(namespace)
    if not ns.templates:
        logger.warning(f"No templates found under '{namespace}'")
        return

    logger.info(f"Templates under {namespace}:\n")
    for template in ns.templates:
        cfg = template.config
        logger.info(
            f"- {template.repo.name}: {cfg.description if cfg else 'No description'} by {cfg.author if cfg else 'Unknown'}"
        )
