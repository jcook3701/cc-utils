---
title: ccutils.cli.options
layout: default
nav_order: 2
parent: api
---
ccutils.cli.options
===================

<a id="module-ccutils.cli.options"></a>

cc-utils Package

### ccutils.cli.options.verbose_mode(cfg: [CLIConfig](ccutils.models.config.md#ccutils.models.config.CLIConfig), verbose: bool) → Any

Handle the --verbose / -v flag.

Override verbosity if CLI flag provided

### ccutils.cli.options.version_mode(version: bool) → None

Handle the --version / -V flag.

When the version flag is provided, this function prints package metadata
(version, author, license) and exits the application immediately.

### Modules

| [`verbose`](ccutils.cli.options.verbose.md#module-ccutils.cli.options.verbose)   | cc-utils Package   |
|----------------------------------------------------------------------------------|--------------------|
| [`version`](ccutils.cli.options.version.md#module-ccutils.cli.options.version)   | cc-utils Package   |
