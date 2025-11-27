---
title: ccutils.models.config
layout: default
nav_order: 2
parent: api
---
ccutils.models.config
=====================

<a id="module-ccutils.models.config"></a>

cc-utils Package

Description: CLI Configuration model.

Configuration file location: ~/.config/cc-utils/config.yml

### Classes

| [`CLIConfig`](#ccutils.models.config.CLIConfig)(\*[, github, ga_tracking, ...])   | Represents user CLI configuration for cc-utils.   |
|-----------------------------------------------------------------------------------|---------------------------------------------------|

### *class* ccutils.models.config.CLIConfig(, github: [GitHubAccount](ccutils.models.github.md#ccutils.models.github.GitHubAccount) | None = None, ga_tracking: str | None = None, accounts: [Accounts](ccutils.models.accounts.md#ccutils.models.accounts.Accounts) | None = None, default_template_branch: str = 'main', cache_dir: Path = PosixPath('/home/jcook/.cache/cc-utils'), log_file: Path = PosixPath('/home/jcook/.cc-utils/cc-utlis.log'), verbose: bool = False)

Bases: `BaseModel`

Represents user CLI configuration for cc-utils.

#### github

(GitHubAccount) GitHub users/org personal info.

* **Type:**
  [ccutils.models.github.GitHubAccount](ccutils.models.github.md#ccutils.models.github.GitHubAccount) | None

#### ga_tracking

(str) Google Analytics Tracking number.

* **Type:**
  str | None

#### accounts

(Accounts) User accounts.

* **Type:**
  [ccutils.models.accounts.Accounts](ccutils.models.accounts.md#ccutils.models.accounts.Accounts) | None

#### default_template_branch

(str)

* **Type:**
  str

#### cache_dir

(Path) cc-utils cache directory.

* **Type:**
  pathlib.Path

#### log_file

(Path) cc-utils log file.

* **Type:**
  pathlib.Path

#### verbose

(bool) cc-utils verbose mode.

* **Type:**
  bool

#### github *: [GitHubAccount](ccutils.models.github.md#ccutils.models.github.GitHubAccount) | None*

#### ga_tracking *: str | None*

#### accounts *: [Accounts](ccutils.models.accounts.md#ccutils.models.accounts.Accounts) | None*

#### default_template_branch *: str*

#### cache_dir *: Path*

#### log_file *: Path*

#### verbose *: bool*

#### *property* log_dir *: Path*
