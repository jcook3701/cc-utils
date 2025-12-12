---
title: nutrimatic.build
layout: default
nav_order: 2
parent: api
---
nutrimatic.build.yaml_front_matter
====================================

<a id="module-nutrimatic.build.yaml_front_matter"></a>

nutri-matic Package

### Functions

| [`add_front_matter_to_dir`](#nutrimatic.build.yaml_front_matter.add_front_matter_to_dir)(directory, extensions)     | Walk a directory recursively, adding front matter to all valid extensions.   |
|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| [`add_front_matter_to_file`](#nutrimatic.build.yaml_front_matter.add_front_matter_to_file)(file_path, depth[, ...]) | Add YAML front matter to a single file.                                      |
| [`build_front_matter`](#nutrimatic.build.yaml_front_matter.build_front_matter)(file_path, depth, project)           | Builds front matter for a file.                                              |
| [`compute_folder_depth`](#nutrimatic.build.yaml_front_matter.compute_folder_depth)(file_path)                       |                                                                              |

### nutrimatic.build.yaml_front_matter.compute_folder_depth(file_path)

* **Return type:**
  `int`

### nutrimatic.build.yaml_front_matter.build_front_matter(file_path, depth, project)

Builds front matter for a file.

* **Parameters:**
  * **file_path** (*Path*) -- \_description_
  * **project** (*str* *|* *None* *,* *optional*) -- \_description_. Defaults to None.
* **Returns:**
  Returns front matter as a string.
* **Return type:**
  str

### nutrimatic.build.yaml_front_matter.add_front_matter_to_file(file_path, depth, project=None)

Add YAML front matter to a single file.
Returns True if modified, False if skipped.

* **Return type:**
  `bool`

### nutrimatic.build.yaml_front_matter.add_front_matter_to_dir(directory, extensions, project=None)

Walk a directory recursively, adding front matter to all valid extensions.
Returns the number of files modified.

* **Return type:**
  `int`
