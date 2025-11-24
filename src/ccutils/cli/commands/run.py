"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: handles running a cookiecutter template with a given JSON

This module provides functions to:
  - Render a Cookiecutter template from a repository.
  - Use a JSON configuration file to supply template context.
  - Optionally specify a branch and output directory for the rendered project.
"""

import json

import typer
from cookiecutter.main import cookiecutter


def run(
    ctx: typer.Context,
    template: str = typer.Argument(..., help="Cookiecutter template repo URL"),
    config: str = typer.Argument(..., help="Path to JSON config file"),
    branch: str = typer.Option(None, help="Branch to use in template repo"),
    output_dir: str = typer.Option(".", help="Directory to render template into"),
) -> None:
    """
    Run a cookiecutter template using a pre-supplied JSON config.
    """
    logger = ctx.obj["logger"]
    cfg = ctx.obj["cfg"]

    with open(config) as f:
        extra_context = json.load(f)

    cookiecutter(
        template,
        checkout=branch,
        no_input=True,
        extra_context=extra_context,
        output_dir=output_dir,
    )

    typer.echo(f"Template {template} rendered successfully in {output_dir}")
