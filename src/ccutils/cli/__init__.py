"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Cookiecutter utilities for automating project templates.
"""

from ccutils.core.metadata import init_metadata

from .main import app

init_metadata()

__all__ = ["app"]
