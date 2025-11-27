---
title: ccutils.core.github
layout: default
nav_order: 2
parent: api
---
ccutils.core.github
===================

<a id="module-ccutils.core.github"></a>

cc-utils Package

Description: Github API Core

### Functions

| [`fetch_config`](#ccutils.core.github.fetch_config)(repo_url)        | Fetch cookiecutter.json from a GitHub repo, trying both main and master branches.   |
|----------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [`fetch_namespace`](#ccutils.core.github.fetch_namespace)(namespace) | Fetch all repositories in a namespace and their configs.                            |

### ccutils.core.github.fetch_config(repo_url: str) → [ConfigData](ccutils.models.template.md#ccutils.models.template.ConfigData) | None

Fetch cookiecutter.json from a GitHub repo,
trying both main and master branches.

### ccutils.core.github.fetch_namespace(namespace: str) → [Namespace](ccutils.models.template.md#ccutils.models.template.Namespace)

Fetch all repositories in a namespace and their configs.
