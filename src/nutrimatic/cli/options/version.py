"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

import typer

import nutrimatic


def version_mode(version: bool) -> None:
    """
    Handle the --version / -V flag.

    When the version flag is provided, this function prints package metadata
    (version, author, license) and exits the application immediately.
    """
    if version:
        typer.echo(f"{nutrimatic.__package__} {nutrimatic.__version__}")
        typer.echo(f"Author: {nutrimatic.__author__}")
        typer.echo(f"License: {nutrimatic.__license__}")
        raise typer.Exit()
