---
title: nutrimatic.core
layout: default
nav_order: 2
parent: api
---
nutrimatic.core.github
======================

<a id="module-nutrimatic.core.github"></a>

nutri-matic Package

Description: Github API Core

### Functions

| [`fetch_config`](#nutrimatic.core.github.fetch_config)(repo_url)        | Fetch cookiecutter.json from a GitHub repo, trying both main and master branches.   |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [`fetch_namespace`](#nutrimatic.core.github.fetch_namespace)(namespace) | Fetch all repositories in a namespace and their configs.                            |

### nutrimatic.core.github.fetch_config(repo_url)

Fetch cookiecutter.json from a GitHub repo,
trying both main and master branches.

* **Return type:**
  [`ConfigData`](nutrimatic.models.template.md#nutrimatic.models.template.ConfigData) | `None`

### nutrimatic.core.github.fetch_namespace(namespace)

Fetch all repositories in a namespace and their configs.

* **Return type:**
  [`Namespace`](nutrimatic.models.template.md#nutrimatic.models.template.Namespace)
