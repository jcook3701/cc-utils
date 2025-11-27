---
title: ccutils.models.ccmeta
layout: default
nav_order: 2
parent: api
---
ccutils.models.ccmeta
=====================

<a id="module-ccutils.models.ccmeta"></a>

cc-utils Package

### Classes

| [`CCMeta`](#ccutils.models.ccmeta.CCMeta)(\*, template, tags, features, extra, ...)   | Root model for ccmeta.toml.   |
|---------------------------------------------------------------------------------------|-------------------------------|

### *class* ccutils.models.ccmeta.CCMeta(\*, template: ~ccutils.models.cctemplate.CCTemplate, tags: list[str] = <factory>, features: list[str] = <factory>, extra: dict[str, object] = <factory>, \*\*extra_data: ~typing.Any)

Bases: `BaseModel`

Root model for ccmeta.toml.
Adjust fields as needed to match your ccmeta.toml structure.

#### template *: [CCTemplate](ccutils.models.cctemplate.md#ccutils.models.cctemplate.CCTemplate)*

#### tags *: list[str]*

#### features *: list[str]*

#### extra *: dict[str, object]*

#### *class* Config

Bases: `object`

#### extra *= 'allow'*
