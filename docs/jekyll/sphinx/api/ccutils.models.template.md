---
title: ccutils.models.template
layout: default
nav_order: 2
parent: api
---
ccutils.models.template
=======================

<a id="module-ccutils.models.template"></a>

ccutils Package

Description: Template Models:
(TemplateRepo, Namespace, ConfigData)

### Classes

| [`ConfigData`](#ccutils.models.template.ConfigData)(\*, project_name, author, version, ...)   | Metadata from a cookiecutter template project's config.json   |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| [`Namespace`](#ccutils.models.template.Namespace)(\*, templates, created_at)                  | A GitHub user/org containing templates                        |
| [`TemplateRepo`](#ccutils.models.template.TemplateRepo)(\*, repo[, config])                   | A cookiecutter template repo                                  |

### *class* ccutils.models.template.ConfigData(\*, project_name: str, author: str, version: str, description: str, variables: dict[str, ~typing.Any] = <factory>)

Bases: `BaseModel`

Metadata from a cookiecutter template project's config.json

#### project_name

Cookiecutter

* **Type:**
  str

#### author

Cookiecutter

* **Type:**
  str

#### version

Cookiecutter template version.

* **Type:**
  str

#### description

Cookiecutter project discription.

* **Type:**
  str

#### variables

Cookiecutter project variables.

* **Type:**
  dict[str, Any]

#### project_name *: str*

#### author *: str*

#### version *: str*

#### description *: str*

#### variables *: dict[str, Any]*

### *class* ccutils.models.template.TemplateRepo(, repo: [GitHubRepo](ccutils.models.github.md#ccutils.models.github.GitHubRepo), config: [ConfigData](#ccutils.models.template.ConfigData) | None = None)

Bases: `BaseModel`

A cookiecutter template repo

#### repo

(GitHubRepo) GitHub repository information.

* **Type:**
  [ccutils.models.github.GitHubRepo](ccutils.models.github.md#ccutils.models.github.GitHubRepo)

#### config

(ConfigData) Metadata from a cookiecutter template.

* **Type:**
  [ccutils.models.template.ConfigData](#ccutils.models.template.ConfigData) | None

#### repo *: [GitHubRepo](ccutils.models.github.md#ccutils.models.github.GitHubRepo)*

#### config *: [ConfigData](#ccutils.models.template.ConfigData) | None*

### *class* ccutils.models.template.Namespace(\*, templates: list[~ccutils.models.template.TemplateRepo] = <factory>, created_at: ~datetime.datetime = <factory>)

Bases: `BaseModel`

A GitHub user/org containing templates

#### templates

(list[TemplateRepo]) List of GitHub namespace/organization template repositories.

* **Type:**
  list[[ccutils.models.template.TemplateRepo](#ccutils.models.template.TemplateRepo)]

#### templates *: list[[TemplateRepo](#ccutils.models.template.TemplateRepo)]*

#### created_at *: datetime*
