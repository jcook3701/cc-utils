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

| [`find_templates`](#nutrimatic.ccmeta.parser.find_templates)(base_dir)   | Return all template directories containing ccmeta.toml.   |
|--------------------------------------------------------------------------|-----------------------------------------------------------|
| [`load_ccmeta`](#nutrimatic.ccmeta.parser.load_ccmeta)(path)             | Load a ccmeta.toml file.                                  |

### nutrimatic.ccmeta.parser.load_ccmeta(path)

Load a ccmeta.toml file.

* **Return type:**
  `dict`[`str`, `Any`]

### nutrimatic.ccmeta.parser.find_templates(base_dir)

Return all template directories containing ccmeta.toml.

* **Return type:**
  `list`[`Path`]
