"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: These functions are intended to be imported directly into Sphinx conf.py
and used in setup function.
"""

import os
import re

from pathlib import Path
from typing import Any
from sphinx.application import Sphinx


def clean_module_docstring(
        app: Sphinx,
        what: str,
        name: str,
        obj: Any,
        options: Any,
        lines: list[str],
) -> None:
    """
    Skip module docstrings. Remove the '© All rights reserved'
    and author/license lines from module docstrings. Only modifies
    module-level docstrings.
    """
    if what == "module":
        # Remove lines that match the boilerplate
        cleaned_lines = [
            line for line in lines
            if not re.match(r"^\s*(© All rights reserved|See the LICENSE|Author:)", line)
        ]
        lines[:] = cleaned_lines  # update the docstring lines in place


def add_yaml_front_matter(
        app: Sphinx,
        docname: str,
        source: list[str]
) -> None:
    """
    Prepend YAML front-matter to every generated Markdown page.
    """
    project_name = getattr(app.config, "project", "unknown_project")

    if app.builder.name != "markdown":
        return

    relative_to_src = Path(docname)
    # Adjust for 'index' having 0 parents but being at depth 0
    depth = len(relative_to_src.parents) - (1 if docname != 'index' else 0) 


    parent_dir = relative_to_src.parent.name 
    if parent_dir == "":
        parent_page_title = f"{project_name}" # Top level page
    else:
        # Assuming parent page title matches the directory name or an 'index'/'README' file in that dir
        # The exact value might depend on your theme's navigation logic.
        parent_page_title = parent_dir # Use a human-readable version

    
    # Force ASCII hyphens
    fm_lines = [
        "---",
        f"title: {os.path.basename(docname)}",
        "layout: default",
        f"nav_order: {depth + 1}",
        f"parent: {parent_page_title}", 
        "---\n",
    ]
    fm = "\n".join(fm_lines)
    # Replace any stray Unicode em dashes, just in case
    fm = fm.replace("—", "---")
    
    source[0] = fm + source[0]  # source is a list of one string


def skip_dupes(
        app: Sphinx,
        what: str,
        name: str,
        obj: Any,
        skip: bool,
        options: Any
) -> bool:
    # Skip all Pydantic internal attributes
    if name.startswith("__pydantic") or name.startswith("_") or name in {
        "model_config",
        "model_fields",
        "model_validator",
        "model_post_init",
    }:
        return True
    return skip




