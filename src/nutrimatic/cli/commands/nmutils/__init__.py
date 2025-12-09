"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

from .docs import add_docs
from .extract import extract
from .list import list_namespace
from .run import run

__all__ = [
    "add_docs",
    "extract",
    "list_namespace",
    "run",
]
