"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

from pathlib import Path
from pydantic import BaseModel

from importlib.metadata import PackageNotFoundError, metadata


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
    def from_package(cls, package_name: str = "ccutils") -> "Metadata":
        """
        Create Metadata from the installed package metadata.

        Falls back to defaults if the package is not found.
        """
        try:
            pkg_meta = metadata(package_name)
            return cls(
                version=pkg_meta.get("Version", "0.1.0"),
                author=pkg_meta.get("Author", "Jared Cook"),
                license=pkg_meta.get("License", "MIT"),
            )
        except PackageNotFoundError:
            return DEFAULT_METADATA



DEFAULT_METADATA = Metadata(
    version="0.1.0",
    author="Jared Cook",
    license="MIT"
)