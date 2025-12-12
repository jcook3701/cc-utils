"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Project README generation.
"""

from pathlib import Path

import typer

from nutrimatic.build.readme import readme_generator


def build_readme(
    ctx: typer.Context,
    jekyll_dir: Path = typer.Argument(..., help="Path to the Jekyll docs directory"),
    output_file: Path = typer.Argument(..., help="Final README.md output file path"),
    readme_gen_dir: Path = typer.Option(
        Path("./docs/.tmp_readme"),
        "--tmp-dir",
        "-t",
        help="Temporary directory to generate README.md",
    ),
    jekyll_build_cmd: str = typer.Option(
        "jekyll build",
        "--jekyll-cmd",
        "-c",
        help="Jekyll build command to execute",
    ),
) -> None:
    """
    Build README.md using Jekyll exactly like the Makefile target.
    """
    _ = ctx.obj["logger"]
    _ = ctx.obj["cfg"]

    typer.echo("🔨 Building ./README.md 📚 with Jekyll...")
    readme_generator(jekyll_dir, output_file, readme_gen_dir, jekyll_build_cmd)
    typer.echo("🧹 Cleaning README.md build artifacts...")
    typer.echo("✅ README.md auto generation complete!")
