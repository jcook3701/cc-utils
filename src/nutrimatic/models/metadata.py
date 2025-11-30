"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

from collections.abc import Mapping
from importlib.metadata import PackageNotFoundError, metadata
from typing import cast

from pydantic import BaseModel


class Metadata(BaseModel):
    """
    metadata type.

    Attributes:
        version: (str).
        author: (str).
        license: (str).
        copyright: (str).
    """

    version: str = ""
    author: str = ""
    license: str = ""

    @property
    def copyright(self) -> str:
        return f"2025 {self.author}"

    @classmethod
    def from_package(cls, package_name: str = "nutri-matic") -> "Metadata":
        """
        Create Metadata from the installed package metadata.

        Falls back to defaults if the package is not found.
        """
        try:
            pkg_meta = metadata(package_name)
            pkg_meta_dict = cast(Mapping[str, str], pkg_meta)

            return cls(
                version=pkg_meta_dict.get("Version", "0.1.0"),
                author=pkg_meta_dict.get("Author", "Jared Cook"),
                license=pkg_meta_dict.get("License", "MIT"),
            )
        except PackageNotFoundError:
            return DEFAULT_METADATA


DEFAULT_METADATA = Metadata(version="0.1.0", author="Jared Cook", license="MIT")
