"""cc-utils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: handles extracting and cleaning cookiecutter.json

This module provides functions to:
  - Clone a Cookiecutter template repository from GitHub.
  - Extract the `cookiecutter.json` configuration file.
  - Remove Jinja placeholders from the config.
  - Save a cleaned version locally for use in automated template rendering.
"""

import json
import re
import tempfile
from pathlib import Path

import typer
from git import Repo  # Requires GitPython


def extract(
    ctx: typer.Context,
    repo: str = typer.Argument(
        ..., help="GitHub repo URL of the cookiecutter template"
    ),
    branch: str = typer.Option("main", help="Branch to use"),
    output: str = typer.Option("clean_cookiecutter.json", help="Output JSON file path"),
) -> None:
    """
    Clone a repo, extract cookiecutter.json, remove Jinja placeholders, save locally.
    """
    _ = ctx.obj["logger"]
    _ = ctx.obj["cfg"]

    with tempfile.TemporaryDirectory() as tmpdir:
        typer.echo(f"Cloning {repo} into {tmpdir} ...")
        Repo.clone_from(repo, tmpdir, branch=branch, depth=1)

        config_path = Path(tmpdir) / "cookiecutter.json"
        if not config_path.exists():
            typer.echo(f"Error: No cookiecutter.json found in {repo}", err=True)
            raise typer.Exit(code=1)

        with open(config_path) as f:
            data: dict[str, object] = json.load(f)

        cleaned_data: dict[str, object] = {
            k: v
            for k, v in data.items()
            if not (isinstance(v, str) and re.search(r"{{\s*cookiecutter", v))
        }

        output_path = Path(output)
        with open(output_path, "w") as f:
            json.dump(cleaned_data, f, indent=4)

        typer.echo(f"Saved cleaned config to {output_path}")
