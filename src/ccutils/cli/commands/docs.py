"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description:
"""

import os
import shutil
import tempfile
from pathlib import Path

import typer
from cookiecutter.main import cookiecutter


def add_docs(
    ctx: typer.Context,
    target_dir: str = typer.Argument(..., help="Path to existing project"),
    template_repo: str = typer.Option(
        "git@github.com:jcook3701/github-docs-cookiecutter.git",
        help="GitHub docs template repo",
    ),
    branch: str = typer.Option("main", help="Branch of the template repo"),
    force: bool = typer.Option(False, help="Overwrite existing files if they exist"),
) -> None:
    """
    Pull all files from the cookiecutter template into ./docs/<target_dir>
    in the target project root.
    """
    logger = ctx.obj["logger"]
    cfg = ctx.obj["cfg"]

    # Create a temp dir to render template
    with tempfile.TemporaryDirectory() as tmpdir:
        typer.echo(f"Running {template_repo} cookiecutter... {tmpdir} ...")
        cookiecutter(template_repo, checkout=branch, no_input=True, output_dir=tmpdir)

        # Find the rendered template folder (the first directory in tmpdir)
        rendered_path = Path(tmpdir)

        for root, _dirs, files in os.walk(rendered_path):
            rel_path = Path(root).relative_to(rendered_path)
            dest_root = Path(target_dir) / rel_path

            dest_root.mkdir(parents=True, exist_ok=True)

            for f in files:
                src = Path(root) / f
                dest = dest_root / f
                if not dest.exists() or force:
                    shutil.copy2(src, dest)
                    typer.echo(f"Added: {dest}")
                else:
                    typer.echo(f"Skipped: {dest} (exists)")
