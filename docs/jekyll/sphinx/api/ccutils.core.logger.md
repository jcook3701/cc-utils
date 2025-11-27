---
title: ccutils.core.logger
layout: default
nav_order: 2
parent: api
---
ccutils.core.logger
===================

<a id="module-ccutils.core.logger"></a>

cc-utils Package

Description: cc-utils project logger.

### Functions

| [`TyperHandler`](#ccutils.core.logger.TyperHandler)([stream])             | Custom handler that routes log messages to typer.echo().   |
|---------------------------------------------------------------------------|------------------------------------------------------------|
| [`setup_logging`](#ccutils.core.logger.setup_logging)(cfg[, log_to_file]) | Configure and return the main ccutils logger.              |

### ccutils.core.logger.TyperHandler(stream: TextIO | None = None) → None

Custom handler that routes log messages to typer.echo().

### ccutils.core.logger.setup_logging(cfg: [CLIConfig](ccutils.models.config.md#ccutils.models.config.CLIConfig), log_to_file: bool = True) → Logger

Configure and return the main ccutils logger.

Can be called at CLI startup, or once globally from config.
