"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Cookiecutter commands for automating project templates.
"""

from .docs import add_docs
from .extract import extract
from .list import list_namespace
from .readme import build_readme
from .run import run
from .yaml_front_matter import add_yaml_front_matter

__all__ = [
    "add_docs",
    "add_yaml_front_matter",
    "build_readme",
    "extract",
    "list_namespace",
    "run",
]
