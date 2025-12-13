---
title: nutrimatic.hooks.post_gen_logic.auto_vars
layout: default
nav_order: 2
parent: api
---
nutrimatic.hooks.post_gen_logic.auto_vars
============================================

<a id="module-nutrimatic.hooks.post_gen_logic.auto_vars"></a>

nutri-matic Package

### Functions

| [`replace_placeholders_in_dir`](#nutrimatic.hooks.post_gen_logic.auto_vars.replace_placeholders_in_dir)(replacements[, path])   | Walk through every file in the newly generated project directory and replace placeholders in all files.   |
|---------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [`replace_placeholders_in_file`](#nutrimatic.hooks.post_gen_logic.auto_vars.replace_placeholders_in_file)(filepath, ...)        | Reads a file, replaces the placeholder, and writes it back.                                               |

### nutrimatic.hooks.post_gen_logic.auto_vars.replace_placeholders_in_file(filepath, replacements)

Reads a file, replaces the placeholder, and writes it back.

* **Return type:**
  `None`

### nutrimatic.hooks.post_gen_logic.auto_vars.replace_placeholders_in_dir(replacements, path=PosixPath('/home/jcook/Documents/git_repo/nutri-matic/docs/sphinx'))

Walk through every file in the newly generated project directory
and replace placeholders in all files.

* **Return type:**
  `None`
