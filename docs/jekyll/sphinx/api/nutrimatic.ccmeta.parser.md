---
title: nutrimatic.ccmeta.parser
layout: default
nav_order: 2
parent: api
---
nutrimatic.ccmeta.parser
========================

<a id="module-nutrimatic.ccmeta.parser"></a>

nutri-matic Package

### Functions

| [`find_templates`](#nutrimatic.ccmeta.parser.find_templates)(base_dir)   | Return all template directories containing teabag.toml or tea.toml or pyproject.toml.   |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [`load_teabag`](#nutrimatic.ccmeta.parser.load_teabag)(path)             | Load a teabag.toml file.                                                                |

### nutrimatic.ccmeta.parser.load_teabag(path)

Load a teabag.toml file.

* **Return type:**
  `dict`[`str`, `Any`]

### nutrimatic.ccmeta.parser.find_templates(base_dir)

Return all template directories containing teabag.toml or tea.toml or pyproject.toml.

* **Return type:**
  `list`[`Path`]
