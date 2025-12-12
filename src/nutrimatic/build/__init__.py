"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Initialization of Build Utilities
"""

# from .ansible
from .readme import readme_generator
from .sphinx import add_yaml_front_matter, clean_module_docstring, skip_dupes
from .yaml_front_matter import (
    add_front_matter_to_dir,
    add_front_matter_to_file,
    build_front_matter,
    compute_folder_depth,
)

__all__ = [
    "add_front_matter_to_dir",
    "add_front_matter_to_file",
    "add_yaml_front_matter",
    "build_front_matter",
    "clean_module_docstring",
    "compute_folder_depth",
    "readme_generator",
    "skip_dupes",
]
