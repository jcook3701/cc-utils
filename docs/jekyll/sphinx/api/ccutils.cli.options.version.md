---
title: ccutils.cli.options.version
layout: default
nav_order: 2
parent: api
---
ccutils.cli.options.version
===========================

<a id="module-ccutils.cli.options.version"></a>

cc-utils Package

### Functions

| [`version_mode`](#ccutils.cli.options.version.version_mode)(version)   | Handle the --version / -V flag.   |
|------------------------------------------------------------------------|-----------------------------------|

### ccutils.cli.options.version.version_mode(version: bool) → None

Handle the --version / -V flag.

When the version flag is provided, this function prints package metadata
(version, author, license) and exits the application immediately.
