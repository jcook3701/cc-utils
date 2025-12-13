---
title: nutrimatic.build
layout: default
nav_order: 2
parent: api
---
nutrimatic.build
================

<a id="module-nutrimatic.build"></a>

nutri-matic Package

Description: Initialization of Build Utilities

### nutrimatic.build.add_front_matter_to_dir(directory, extensions, project=None)

Walk a directory recursively, adding front matter to all valid extensions.
Returns the number of files modified.

* **Return type:**
  `int`

### nutrimatic.build.add_front_matter_to_file(file_path, extensions, depth, project=None)

Add YAML front matter to a single file.
Returns True if modified, False if skipped.

* **Return type:**
  `bool`

### nutrimatic.build.add_yaml_front_matter(app, docname, source)

Prepend YAML front-matter to every generated Markdown page.

* **Return type:**
  `None`

### nutrimatic.build.build_front_matter(file_path, extensions, depth, project)

Builds front matter for a file.

* **Parameters:**
  * **file_path** (*Path*) -- \_description_
  * **project** (*str* *|* *None* *,* *optional*) -- \_description_. Defaults to None.
* **Returns:**
  Returns front matter as a string.
* **Return type:**
  str

### nutrimatic.build.clean_module_docstring(app, what, name, obj, options, lines)

Skip module docstrings. Remove the '© All rights reserved'
and author/license lines from module docstrings. Only modifies
module-level docstrings.

* **Return type:**
  `None`

### nutrimatic.build.compute_folder_depth(file_path)

* **Return type:**
  `int`

### nutrimatic.build.readme_generator(jekyll_dir, output_file, readme_gen_dir, jekyll_build_cmd)

\_summary_

* **Parameters:**
  * **jekyll_dir** (*Path*) -- \_description_
  * **output_file** (*Path*) -- \_description_
  * **readme_gen_dir** (*Path*) -- \_description_
  * **jekyll_build_cmd** (*str*) -- \_description_
* **Return type:**
  `None`

### nutrimatic.build.skip_dupes(app, what, name, obj, skip, options)

Skip all Pydantic internal attributes

* **Return type:**
  `bool`

### Modules

| [`ansible`](nutrimatic.build.ansible.md#module-nutrimatic.build.ansible)                               | nutri-matic Package   |
|--------------------------------------------------------------------------------------------------------|-----------------------|
| [`readme`](nutrimatic.build.readme.md#module-nutrimatic.build.readme)                                  | nutri-matic Package   |
| [`sphinx`](nutrimatic.build.sphinx.md#module-nutrimatic.build.sphinx)                                  | nutri-matic Package   |
| [`yaml_front_matter`](nutrimatic.build.yaml_front_matter.md#module-nutrimatic.build.yaml_front_matter) | nutri-matic Package   |
