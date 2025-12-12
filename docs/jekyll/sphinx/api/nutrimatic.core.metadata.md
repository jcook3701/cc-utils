---
title: nutrimatic.core
layout: default
nav_order: 2
parent: api
---
nutrimatic.core.metadata
========================

<a id="module-nutrimatic.core.metadata"></a>

nutri-matic Package

### Functions

| [`init_metadata`](#nutrimatic.core.metadata.init_metadata)()   | Populate module-level metadata such as `__version__`, `__author__`, and `__license__` based on the installed package metadata.   |
|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|

### nutrimatic.core.metadata.init_metadata()

Populate module-level metadata such as `__version__`, `__author__`,
and `__license__` based on the installed package metadata.

This function attempts to read metadata from the installed distribution
using `importlib.metadata.metadata()`. If the package is not installed
(e.g., during development or when running from source), it falls back to
reasonable defaults defined inside the function.

The values are written into this module's global namespace so they may be
imported from `nutri-matic` directly:

```default
>>> from nutrimatic import __version__, __author__
>>> print(__version__)
0.3.1
```

This keeps the module metadata centralized and consistent with the
package information defined in `pyproject.toml`.

* **Return type:**
  `None`
