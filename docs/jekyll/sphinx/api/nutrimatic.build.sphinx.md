---
title: nutrimatic.build.sphinx
layout: default
nav_order: 2
parent: api
---
nutrimatic.build.sphinx
=======================

<a id="module-nutrimatic.build.sphinx"></a>

nutri-matic Package

Description: These functions are intended to be imported directly into Sphinx conf.py
and used in setup function.

### Functions

| [`add_yaml_front_matter`](#nutrimatic.build.sphinx.add_yaml_front_matter)(app, docname, source)        | Prepend YAML front-matter to every generated Markdown page.   |
|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| [`clean_module_docstring`](#nutrimatic.build.sphinx.clean_module_docstring)(app, what, name, obj, ...) | Skip module docstrings.                                       |
| [`skip_dupes`](#nutrimatic.build.sphinx.skip_dupes)(app, what, name, obj, skip, options)               | Skip all Pydantic internal attributes                         |

### nutrimatic.build.sphinx.clean_module_docstring(app, what, name, obj, options, lines)

Skip module docstrings. Remove the '© All rights reserved'
and author/license lines from module docstrings. Only modifies
module-level docstrings.

* **Return type:**
  `None`

### nutrimatic.build.sphinx.add_yaml_front_matter(app, docname, source)

Prepend YAML front-matter to every generated Markdown page.

* **Return type:**
  `None`

### nutrimatic.build.sphinx.skip_dupes(app, what, name, obj, skip, options)

Skip all Pydantic internal attributes

* **Return type:**
  `bool`
