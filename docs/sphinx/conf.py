"""Sphinx Configuration

© All rights reserved. Jared Cook

See the LICENSE.TXT file for more details.

Author: Jared Cook
Description: Configuration file for the Sphinx documentation builder.
  For the full list of built-in configuration values, see the documentation:
  https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

#Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from pathlib import Path
import re

# -- Path setup --------------------------------------------------------------

# Add the source directory to sys.path so Sphinx can find your package
sys.path.insert(0, os.path.abspath("../../src"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "ccutils"
copyright = "2025, Jared Cook"
author = "Jared Cook"
release = "0.1.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Mock imports that aren't available in your environment
autodoc_mock_imports = []

# Extensions: MyST for Markdown + autodoc for docstrings
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",   # Supports Google/NumPy style docstrings
    "sphinx.ext.viewcode",   # Adds links to source code
    "sphinx.ext.autosummary",    
]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]

autosummary_generate = True

# Source file suffixes: support both .rst and .md
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# Templates and exclusions
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

# Optional: show class members by default in the sidebar
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}


smartquotes = False


def clean_module_docstring(app, what, name, obj, options, lines):
    """
    Skip module docstrings. Remove the '© All rights reserved'
    and author/license lines from module docstrings. Only modifies
    module-level docstrings.
    """
    if what == "module":
        # Remove lines that match the boilerplate
        cleaned_lines = [
            line for line in lines
            if not re.match(r"© All rights reserved|See the LICENSE|Author:", line)
        ]
        lines[:] = cleaned_lines  # update the docstring lines in place

from sphinx.application import Sphinx

def add_yaml_front_matter(app: Sphinx, docname, source):
    """
    Prepend YAML front-matter to every generated Markdown page.
    """

    if app.builder.name != "markdown":
        return

    relative_to_src = Path(docname)
    # Adjust for 'index' having 0 parents but being at depth 0
    depth = len(relative_to_src.parents) - (1 if docname != 'index' else 0) 

    parent_dir = relative_to_src.parent.name 
    if parent_dir == "":
        parent_page_title = f"{project}" # Top level page
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

def setup(app):
    app.connect("autodoc-process-docstring", clean_module_docstring)
    app.connect("source-read", add_yaml_front_matter)
