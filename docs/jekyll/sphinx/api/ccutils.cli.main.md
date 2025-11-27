---
title: ccutils.cli.main
layout: default
nav_order: 2
parent: api
---
ccutils.cli.main
================

<a id="module-ccutils.cli.main"></a>

cc-utils Package

Description: Command-line interface for ccutils.ccutils: Cookiecutter automation utilities.

Provides commands to:
: - extract: Clone a Cookiecutter template repo, clean
    its cookiecutter.json of Jinja placeholders, and save locally.
  - run: Render a Cookiecutter template using a pre-supplied JSON config file.

### Functions

| [`main`](#ccutils.cli.main.main)(ctx[, verbose, version])   | Main CLI entrypoint for cc-utils: Initialize configuration and logging for all subcommands.   |
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------|

### ccutils.cli.main.main(ctx: ~typer.models.Context, verbose: bool = <typer.models.OptionInfo object>, version: bool = <typer.models.OptionInfo object>) → None

Main CLI entrypoint for cc-utils:
Initialize configuration and logging for all subcommands.
