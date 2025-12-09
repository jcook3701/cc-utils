"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

from nutrimatic.models.metadata import Metadata

_md = Metadata.from_package("nutri-matic")

__version__ = _md.version
__author__ = _md.author
__license__ = _md.license
__copyright__ = _md.copyright

__all__ = [
    "__author__",
    "__copyright__",
    "__license__",
    "__version__",
]
