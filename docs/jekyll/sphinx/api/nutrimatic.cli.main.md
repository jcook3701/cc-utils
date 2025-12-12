---
title: nutrimatic.cli
layout: default
nav_order: 2
parent: api
---
nutrimatic.cli.main
===================

<a id="module-nutrimatic.cli.main"></a>

nutri-matic Package

Description: Command-line interface Cookiecutter automation utilities.

Provides commands to:
: - extract: Clone a Cookiecutter template repo, clean
    its cookiecutter.json of Jinja placeholders, and save locally.
  - run: Render a Cookiecutter template using a pre-supplied JSON config file.

### Functions

| [`main`](#nutrimatic.cli.main.main)(ctx[, verbose, version])   | Main CLI entrypoint for nutri-matic Cookiecutter utilities: Initialize configuration and logging for all subcommands.   |
|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|

### nutrimatic.cli.main.main(ctx, verbose=<typer.models.OptionInfo object>, version=<typer.models.OptionInfo object>)

Main CLI entrypoint for nutri-matic Cookiecutter utilities:
Initialize configuration and logging for all subcommands.

* **Return type:**
  `None`
