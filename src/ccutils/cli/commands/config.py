"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description:
"""

import json
import yaml
import typer
from ccutils.core.config import ensure_config


def show_config(
    ctx: typer.Context,
    format: str = typer.Option(
        "json", "--format", "-f", help="Output format: json or yaml"
    )
):
    """
    Print the current CLI configuration to the screen.
    """
    logger = ctx.obj["logger"]
    cfg = ctx.obj["cfg"]

    if format.lower() in {"yaml", "yml"}:
        typer.echo(
            yaml.safe_dump(cfg.model_dump(mode="json", by_alias=True), sort_keys=False)
        )
    else:
        # Default JSON
        typer.echo(
            cfg.model_dump_json(
                indent=4, fallback=lambda x: str(x) if hasattr(x, "__str__") else x
            )
        )
