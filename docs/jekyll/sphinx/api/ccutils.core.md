---
title: ccutils.core
layout: default
nav_order: 2
parent: api
---
ccutils.core
============

<a id="module-ccutils.core"></a>

cc-utils Package

Description: Core Imports.

### ccutils.core.clean() → None

Remove \_shared_hooks directory.

### ccutils.core.ensure_config() → [CLIConfig](ccutils.models.config.md#ccutils.models.config.CLIConfig)

Ensure the config exists and return a validated singleton CLIConfig instance.

### ccutils.core.fetch_namespace(namespace: str) → [Namespace](ccutils.models.template.md#ccutils.models.template.Namespace)

Fetch all repositories in a namespace and their configs.

### ccutils.core.make(cmd: str) → None

Run a make target inside post-gen, exiting on failure.

### ccutils.core.setup_logging(cfg: [CLIConfig](ccutils.models.config.md#ccutils.models.config.CLIConfig), log_to_file: bool = True) → Logger

Configure and return the main ccutils logger.

Can be called at CLI startup, or once globally from config.

### ccutils.core.tree() → None

Run tree cmd inside the post-gen.

### Modules

| [`bash`](ccutils.core.bash.md#module-ccutils.core.bash)             | cc-utils Package   |
|---------------------------------------------------------------------|--------------------|
| [`config`](ccutils.core.config.md#module-ccutils.core.config)       | cc-utils Package   |
| [`github`](ccutils.core.github.md#module-ccutils.core.github)       | cc-utils Package   |
| [`logger`](ccutils.core.logger.md#module-ccutils.core.logger)       | cc-utils Package   |
| [`metadata`](ccutils.core.metadata.md#module-ccutils.core.metadata) | cc-utils Package   |
| [`parser`](ccutils.core.parser.md#module-ccutils.core.parser)       | cc-utils Package   |
| [`template`](ccutils.core.template.md#module-ccutils.core.template) | cc-utils Package   |
