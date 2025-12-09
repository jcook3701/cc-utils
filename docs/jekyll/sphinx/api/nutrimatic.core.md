---
title: nutrimatic.core
layout: default
nav_order: 2
parent: api
---
nutrimatic.core
===============

<a id="module-nutrimatic.core"></a>

nutri-matic Package

Description: Core Imports.

### nutrimatic.core.clean()

Remove \_shared_hooks directory.

* **Return type:**
  `None`

### nutrimatic.core.ensure_config()

Ensure the config exists and return a validated singleton CLIConfig instance.

* **Return type:**
  [`CLIConfig`](nutrimatic.models.config.md#nutrimatic.models.config.CLIConfig)

### nutrimatic.core.fetch_namespace(namespace)

Fetch all repositories in a namespace and their configs.

* **Return type:**
  [`Namespace`](nutrimatic.models.template.md#nutrimatic.models.template.Namespace)

### nutrimatic.core.make(cmd)

Run a make target inside post-gen, exiting on failure.

* **Return type:**
  `None`

### nutrimatic.core.setup_logging(cfg, log_to_file=True)

Configure and return the main nutri-matic logger.

Can be called at CLI startup, or once globally from config.

* **Return type:**
  `Logger`

### nutrimatic.core.tree()

Run tree cmd inside the post-gen.

* **Return type:**
  `None`

### Modules

| [`bash`](nutrimatic.core.bash.md#module-nutrimatic.core.bash)             | nutri-matic Package   |
|---------------------------------------------------------------------------|-----------------------|
| [`config`](nutrimatic.core.config.md#module-nutrimatic.core.config)       | nutri-matic Package   |
| [`github`](nutrimatic.core.github.md#module-nutrimatic.core.github)       | nutri-matic Package   |
| [`logger`](nutrimatic.core.logger.md#module-nutrimatic.core.logger)       | nutri-matic Package   |
| [`metadata`](nutrimatic.core.metadata.md#module-nutrimatic.core.metadata) | nutri-matic Package   |
| [`parser`](nutrimatic.core.parser.md#module-nutrimatic.core.parser)       | nutri-matic Package   |
| [`template`](nutrimatic.core.template.md#module-nutrimatic.core.template) | nutri-matic Package   |
