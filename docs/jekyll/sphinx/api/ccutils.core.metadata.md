---
title: ccutils.core.metadata
layout: default
nav_order: 2
parent: api
---
ccutils.core.metadata
=====================

<a id="module-ccutils.core.metadata"></a>

cc-utils Package

Description: Cookiecutter utilities for automating project templates.

### Functions

| [`init_metadata`](#ccutils.core.metadata.init_metadata)()   | Populate module-level metadata such as `__version__`, `__author__`, and `__license__` based on the installed package metadata.   |
|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|

### ccutils.core.metadata.init_metadata() → None

Populate module-level metadata such as `__version__`, `__author__`,
and `__license__` based on the installed package metadata.

This function attempts to read metadata from the installed distribution
using `importlib.metadata.metadata()`. If the package is not installed
(e.g., during development or when running from source), it falls back to
reasonable defaults defined inside the function.

The values are written into this module's global namespace so they may be
imported from `ccutils` directly:

```default
>>> from ccutils import __version__, __author__
>>> print(__version__)
0.3.1
```

This keeps the module metadata centralized and consistent with the
package information defined in `pyproject.toml`.
