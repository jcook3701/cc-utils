---
title: nutrimatic.models.ccmeta
layout: default
nav_order: 2
parent: api
---
nutrimatic.models.ccmeta
========================

<a id="module-nutrimatic.models.ccmeta"></a>

nutri-matic Package

### Classes

| [`CCMeta`](#nutrimatic.models.ccmeta.CCMeta)(\*\*data)   | Root model for ccmeta.toml.   |
|----------------------------------------------------------|-------------------------------|

### *class* nutrimatic.models.ccmeta.CCMeta(\*\*data)

Bases: `BaseModel`

Root model for ccmeta.toml.
Adjust fields as needed to match your ccmeta.toml structure.

#### template *: [`CCTemplate`](nutrimatic.models.cctemplate.md#nutrimatic.models.cctemplate.CCTemplate)*

#### tags *: `list`[`str`]*

#### features *: `list`[`str`]*

#### extra *: `dict`[`str`, `object`]*

#### *class* Config

Bases: `object`

#### extra *= 'allow'*
