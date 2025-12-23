---
title: nutrimatic.core.bash
layout: default
nav_order: 2
parent: api
---
nutrimatic.core.bash
====================

<a id="module-nutrimatic.core.bash"></a>

nutri-matic Package

Description: Bash commands ported to python.

### Functions

| [`clean`](#nutrimatic.core.bash.clean)()                 | Remove \_shared_hooks directory.                       |
|----------------------------------------------------------|--------------------------------------------------------|
| [`make`](#nutrimatic.core.bash.make)(cmd, \*[, verbose]) | Run a make target inside post-gen, exiting on failure. |
| [`tree`](#nutrimatic.core.bash.tree)()                   | Run tree cmd inside the post-gen.                      |

### nutrimatic.core.bash.clean()

Remove \_shared_hooks directory.

* **Return type:**
  `None`

### nutrimatic.core.bash.make(cmd, , verbose=False)

Run a make target inside post-gen, exiting on failure.

* **Return type:**
  `None`

### nutrimatic.core.bash.tree()

Run tree cmd inside the post-gen.

* **Return type:**
  `None`
