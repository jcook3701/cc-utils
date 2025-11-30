---
title: nutrimatic.models.base
layout: default
nav_order: 2
parent: api
---
nutrimatic.models.base
======================

<a id="module-nutrimatic.models.base"></a>

nutri-matic Package

Description: Base model for project models.

### Classes

| [`CcutilsBaseModel`](#nutrimatic.models.base.CcutilsBaseModel)()   | Base class providing common (de)serialization helpers.   |
|--------------------------------------------------------------------|----------------------------------------------------------|

### *class* nutrimatic.models.base.CcutilsBaseModel

Bases: `object`

Base class providing common (de)serialization helpers.

#### to_dict()

Recursively convert a dataclass instance to a dict.

* **Return type:**
  `dict`[`str`, `Any`]

#### *classmethod* from_dict(data)

Instantiate a dataclass from a dict. Supports nested dataclasses.

* **Return type:**
  `TypeVar`(`T`, bound= CcutilsBaseModel)
