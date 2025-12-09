"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

from .ansible import generate_ansible_dirs
from .auto_vars import replace_placeholders_in_dir
from .docs import generate_docs_templates

__all__ = [
    "generate_ansible_dirs",
    "generate_docs_templates",
    "replace_placeholders_in_dir",
]
