---
title: ccutils.core.bash
layout: default
nav_order: 2
parent: api
---
ccutils.core.bash
=================

<a id="module-ccutils.core.bash"></a>

cc-utils Package

Descriptons: Bash commands ported to python.

### Functions

| [`clean`](#ccutils.core.bash.clean)()   | Remove \_shared_hooks directory.                       |
|-----------------------------------------|--------------------------------------------------------|
| [`make`](#ccutils.core.bash.make)(cmd)  | Run a make target inside post-gen, exiting on failure. |
| [`tree`](#ccutils.core.bash.tree)()     | Run tree cmd inside the post-gen.                      |

### ccutils.core.bash.clean() → None

Remove \_shared_hooks directory.

### ccutils.core.bash.make(cmd: str) → None

Run a make target inside post-gen, exiting on failure.

### ccutils.core.bash.tree() → None

Run tree cmd inside the post-gen.
