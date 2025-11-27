---
title: ccutils.models.cctemplate
layout: default
nav_order: 2
parent: api
---
ccutils.models.cctemplate
=========================

<a id="module-ccutils.models.cctemplate"></a>

cc-utils Package

### Classes

| [`CCTemplate`](#ccutils.models.cctemplate.CCTemplate)(\*, name, description, path, ...)         | A single template defined in ccmeta.toml.        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------|
| [`CCTemplateVariable`](#ccutils.models.cctemplate.CCTemplateVariable)(\*, name[, default, ...]) | Represents a single cookiecutter input variable. |

### *class* ccutils.models.cctemplate.CCTemplateVariable(, name: str, default: str | None = None, description: str | None = None)

Bases: `BaseModel`

Represents a single cookiecutter input variable.

#### name *: str*

#### default *: str | None*

#### description *: str | None*

### *class* ccutils.models.cctemplate.CCTemplate(\*, name: str, description: str | None = None, path: ~pathlib.Path, language: str | None = None, license: str | None = 'MIT', version: str | None = '0.1.0', maintainer: str | None = None, project_type: str | None = None, variables: list[~ccutils.models.cctemplate.CCTemplateVariable] = <factory>, tags: list[str] = <factory>, features: list[str] = <factory>, \*\*extra_data: ~typing.Any)

Bases: `BaseModel`

A single template defined in ccmeta.toml.

#### name *: str*

#### description *: str | None*

#### path *: Path*

#### language *: str | None*

#### license *: str | None*

#### version *: str | None*

#### maintainer *: str | None*

#### project_type *: str | None*

#### variables *: list[[CCTemplateVariable](#ccutils.models.cctemplate.CCTemplateVariable)]*

#### tags *: list[str]*

#### features *: list[str]*

#### *class* Config

Bases: `object`

#### extra *= 'allow'*
