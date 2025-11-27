---
title: ccutils.ccmeta.parser
layout: default
nav_order: 2
parent: api
---
ccutils.ccmeta.parser
=====================

<a id="module-ccutils.ccmeta.parser"></a>

cc-utils Package

### Functions

| [`find_templates`](#ccutils.ccmeta.parser.find_templates)(base_dir)   | Return all template directories containing ccmeta.toml.   |
|-----------------------------------------------------------------------|-----------------------------------------------------------|
| [`load_ccmeta`](#ccutils.ccmeta.parser.load_ccmeta)(path)             | Load a ccmeta.toml file.                                  |

### ccutils.ccmeta.parser.load_ccmeta(path: Path) → dict[str, Any]

Load a ccmeta.toml file.

### ccutils.ccmeta.parser.find_templates(base_dir: Path) → list[Path]

Return all template directories containing ccmeta.toml.
