"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Cookiecutter utilities for automating project templates.
"""

from collections.abc import Mapping
from importlib.metadata import PackageNotFoundError, metadata
from typing import cast


def init_metadata() -> None:
    """
    Populate module-level metadata such as ``__version__``, ``__author__``,
    and ``__license__`` based on the installed package metadata.

    This function attempts to read metadata from the installed distribution
    using :func:`importlib.metadata.metadata`. If the package is not installed
    (e.g., during development or when running from source), it falls back to
    reasonable defaults defined inside the function.

    The values are written into this module's global namespace so they may be
    imported from ``ccutils`` directly::

        >>> from ccutils import __version__, __author__
        >>> print(__version__)
        0.3.1

    This keeps the module metadata centralized and consistent with the
    package information defined in ``pyproject.toml``.
    """
    try:
        pkg_meta = metadata("ccutils")
        pkg_meta_dict = cast(Mapping[str, str], pkg_meta)

        version = pkg_meta_dict.get("Version", "0.1.0")
        author = pkg_meta_dict.get("Author", "Unknown")
        _license = pkg_meta_dict.get("License", "Unknown")

    except PackageNotFoundError:
        version = "0.1.0"
        author = "Jared Cook"
        _license = "MIT"

    _copyright = "2025 Jared Cook"

    # Write values back into module-level variables
    globals()["__version__"] = version
    globals()["__author__"] = author
    globals()["__license__"] = _license
    globals()["__copyright__"] = _copyright
