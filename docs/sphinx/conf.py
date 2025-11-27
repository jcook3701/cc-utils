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

from sphinx.application import Sphinx

from ccutils.build import clean_module_docstring, add_yaml_front_matter, skip_dupes

# -- Path setup --------------------------------------------------------------

# Add the source directory to sys.path so Sphinx can find your package
sys.path.insert(0, os.path.abspath("../../src"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "cc-utils"
copyright = "2025, Jared Cook"
author = "Jared Cook"
release = "0.1.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Mock imports that aren't available in your environment
autodoc_mock_imports = []

# Extensions: MyST for Markdown + autodoc for docstrings
extensions = [
    "sphinx_markdown_builder",
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

numpydoc_class_members_toctree = False
autosummary_generate = True
autodoc_member_order = 'bysource'
# 2. Tell Sphinx where to write generated stubs (usually a hidden directory to avoid conflicts)
# You might need to add 'ext.autodoc' and 'ext.autosummary' to your extensions list
autosummary_generate = True
autosummary_generate_dir = '_autosummary_generated'

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


def setup(app: Sphinx):
    app.connect("autodoc-skip-member", skip_dupes)
    app.connect("autodoc-process-docstring", clean_module_docstring)
    app.connect("source-read", add_yaml_front_matter)