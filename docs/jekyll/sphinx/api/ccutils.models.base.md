---
title: ccutils.models.base
layout: default
nav_order: 2
parent: api
---
ccutils.models.base
===================

<a id="module-ccutils.models.base"></a>

cc-utils Package

Description: cc-utils Base model for cc-utils project models.

### Classes

| [`CcutilsBaseModel`](#ccutils.models.base.CcutilsBaseModel)(\*args, \*\*kwargs)   | Base class providing common (de)serialization helpers.   |
|-----------------------------------------------------------------------------------|----------------------------------------------------------|

### *class* ccutils.models.base.CcutilsBaseModel(\*args, \*\*kwargs)

Bases: `object`

Base class providing common (de)serialization helpers.

#### to_dict() → dict[str, Any]

Recursively convert a dataclass instance to a dict.

#### *classmethod* from_dict(data: dict[str, Any]) → T

Instantiate a dataclass from a dict. Supports nested dataclasses.
