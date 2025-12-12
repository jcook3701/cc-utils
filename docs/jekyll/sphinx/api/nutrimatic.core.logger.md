---
title: nutrimatic.core
layout: default
nav_order: 2
parent: api
---
nutrimatic.core.logger
======================

<a id="module-nutrimatic.core.logger"></a>

nutri-matic Package

Description: Project logger.

### Functions

| [`TyperHandler`](#nutrimatic.core.logger.TyperHandler)([stream])             | Custom handler that routes log messages to typer.echo().   |
|------------------------------------------------------------------------------|------------------------------------------------------------|
| [`setup_logging`](#nutrimatic.core.logger.setup_logging)(cfg[, log_to_file]) | Configure and return the main nutri-matic logger.          |

### nutrimatic.core.logger.TyperHandler(stream: TextIO | None = None) → None

Custom handler that routes log messages to typer.echo().

### nutrimatic.core.logger.setup_logging(cfg, log_to_file=True)

Configure and return the main nutri-matic logger.

Can be called at CLI startup, or once globally from config.

* **Return type:**
  `Logger`
