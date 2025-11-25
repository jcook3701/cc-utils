"""cc-utils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

import typer
from pathlib import Path
from ccutils.templates.cc_templates import generate_readme, generate_makefile


def generate(
    repo: str = typer.Argument(
        ...,
        help="Path to the template repository to generate README.md and Makefile for",
    )
) -> None:
    """
    Generate README.md and Makefile for a cc-template project.
    """
    repo_dir = Path(repo).resolve()
    generate_readme(repo_dir)
    generate_makefile(repo_dir)
    typer.echo(f"Generated README.md and Makefile for {repo_dir.name}")
