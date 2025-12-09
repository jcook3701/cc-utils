"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: YAML front matter injector.  Intended to be used with
ansible autodocs output.
"""

from pathlib import Path

import typer

from nutrimatic.build.yaml_front_matter import add_front_matter_to_dir

app = typer.Typer(
    help="Add YAML front matter to markdown/YAML files recursively.",
    add_completion=False,
)


def add_yaml_front_matter(
    ctx: typer.Context,
    directory: Path = typer.Argument(
        ..., exists=True, file_okay=False, help="Directory to scan"
    ),
    ext: list[str] = typer.Option(
        ["yml", "yaml", "md"],
        "--ext",
        "-e",
        help="File extensions to modify. Repeatable.",
    ),
    project: str = typer.Option(
        None,
        "--project",
        help="Project or top-level name used for top parent pages.",
    ),
) -> None:
    """
    Add YAML front matter to all files in DIRECTORY matching extensions.
    """
    _ = ctx.obj["logger"]
    _ = ctx.obj["cfg"]

    extensions = {e.lower() for e in ext}

    modified = add_front_matter_to_dir(directory, extensions, project)

    typer.echo(f"✅ Added YAML front matter to {modified} file(s) under {directory}")
