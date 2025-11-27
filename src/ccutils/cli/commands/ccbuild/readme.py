"""cc-utils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Project README generation.
"""

import shutil
import subprocess
from pathlib import Path

import typer

from ccutils.build.readme import _write_front_matter


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

    typer.echo("🔨 Building ./README.md 📘 with Jekyll...")

    # Ensure temp build directory exists
    readme_gen_dir.mkdir(parents=True, exist_ok=True)

    # Copy _config.yml and Gemfile
    shutil.copy(jekyll_dir / "_config.yml", readme_gen_dir / "_config.yml")
    shutil.copy(jekyll_dir / "Gemfile", readme_gen_dir / "Gemfile")

    # Write tmp README.md (front matter + comment + content)
    tmp_readme = readme_gen_dir / "README.md"
    source_readme = jekyll_dir / "README.md"
    _write_front_matter(tmp_readme, source_readme, jekyll_dir)

    # Run Jekyll build
    subprocess.run(jekyll_build_cmd, shell=True, check=True, cwd=readme_gen_dir)

    # Copy result back to project
    shutil.copy(readme_gen_dir / "_site/README.md", output_file)

    # Cleanup
    shutil.rmtree(readme_gen_dir)
    typer.echo("🧹 Cleaning README.md build artifacts...")
    typer.echo("✅ README.md auto generation complete!")
