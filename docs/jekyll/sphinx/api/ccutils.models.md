---
title: ccutils.models
layout: default
nav_order: 2
parent: api
---
ccutils.models
==============

<a id="module-ccutils.models"></a>

cc-utils Package

Description: Init python models (types)

### *class* ccutils.models.Accounts(, github_username: str = '', twitter_username: str = '', linkedin_usercode: str = '', buymeacoffee_username: str = '')

Bases: `BaseModel`

Represents user accounts.

#### github_username

GitHub username of the account.

* **Type:**
  str

#### twitter_username

Twitter handle.

* **Type:**
  str

#### linkedin_usercode

LinkedIn user code.

* **Type:**
  str

#### buymeacoffee_username

BuyMeACoffee username.

* **Type:**
  str

#### github_username *: str*

#### twitter_username *: str*

#### linkedin_usercode *: str*

#### buymeacoffee_username *: str*

### *class* ccutils.models.CCMeta(\*, template: ~ccutils.models.cctemplate.CCTemplate, tags: list[str] = <factory>, features: list[str] = <factory>, extra: dict[str, object] = <factory>, \*\*extra_data: ~typing.Any)

Bases: `BaseModel`

Root model for ccmeta.toml.
Adjust fields as needed to match your ccmeta.toml structure.

#### *class* Config

Bases: `object`

#### extra *= 'allow'*

#### template *: [CCTemplate](ccutils.models.cctemplate.md#ccutils.models.cctemplate.CCTemplate)*

#### tags *: list[str]*

#### features *: list[str]*

#### extra *: dict[str, object]*

### *class* ccutils.models.CCTemplate(\*, name: str, description: str | None = None, path: ~pathlib.Path, language: str | None = None, license: str | None = 'MIT', version: str | None = '0.1.0', maintainer: str | None = None, project_type: str | None = None, variables: list[~ccutils.models.cctemplate.CCTemplateVariable] = <factory>, tags: list[str] = <factory>, features: list[str] = <factory>, \*\*extra_data: ~typing.Any)

Bases: `BaseModel`

A single template defined in ccmeta.toml.

#### *class* Config

Bases: `object`

#### extra *= 'allow'*

#### name *: str*

#### description *: str | None*

#### path *: Path*

#### language *: str | None*

#### license *: str | None*

#### version *: str | None*

#### maintainer *: str | None*

#### project_type *: str | None*

#### variables *: list[[CCTemplateVariable](ccutils.models.cctemplate.md#ccutils.models.cctemplate.CCTemplateVariable)]*

#### tags *: list[str]*

#### features *: list[str]*

### *class* ccutils.models.CCTemplateVariable(, name: str, default: str | None = None, description: str | None = None)

Bases: `BaseModel`

Represents a single cookiecutter input variable.

#### name *: str*

#### default *: str | None*

#### description *: str | None*

### *class* ccutils.models.CLIConfig(, github: [GitHubAccount](ccutils.models.github.md#ccutils.models.github.GitHubAccount) | None = None, ga_tracking: str | None = None, accounts: [Accounts](ccutils.models.accounts.md#ccutils.models.accounts.Accounts) | None = None, default_template_branch: str = 'main', cache_dir: Path = PosixPath('/home/jcook/.cache/cc-utils'), log_file: Path = PosixPath('/home/jcook/.cc-utils/cc-utlis.log'), verbose: bool = False)

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

#### *property* log_dir *: Path*

#### github *: [GitHubAccount](ccutils.models.github.md#ccutils.models.github.GitHubAccount) | None*

#### ga_tracking *: str | None*

#### accounts *: [Accounts](ccutils.models.accounts.md#ccutils.models.accounts.Accounts) | None*

#### default_template_branch *: str*

#### cache_dir *: Path*

#### log_file *: Path*

#### verbose *: bool*

### *class* ccutils.models.ConfigData(\*, project_name: str, author: str, version: str, description: str, variables: dict[str, ~typing.Any] = <factory>)

Bases: `BaseModel`

Metadata from a cookiecutter template project's config.json

#### project_name

Cookiecutter

* **Type:**
  str

#### author

Cookiecutter

* **Type:**
  str

#### version

Cookiecutter template version.

* **Type:**
  str

#### description

Cookiecutter project discription.

* **Type:**
  str

#### variables

Cookiecutter project variables.

* **Type:**
  dict[str, Any]

#### project_name *: str*

#### author *: str*

#### version *: str*

#### description *: str*

#### variables *: dict[str, Any]*

### *class* ccutils.models.GitHubAccount(, user: str = '', namespace: str = '', email: str = '', auth: [GitHubAuth](ccutils.models.github.md#ccutils.models.github.GitHubAuth) = GitHubAuth(auth_type='ssh', token=None, ssh_key_path=PosixPath('~/.ssh/id_rsa')))

Bases: `BaseModel`

GitHub users/org personal info

#### user

(str) GitHub username.

* **Type:**
  str

#### namespace

(str) GitHub organization or namespace; often same as user.

* **Type:**
  str

#### email

(str) GitHub account email.

* **Type:**
  str

#### auth

(GitHubAuth) Authentication configuration for GitHub access.

* **Type:**
  [ccutils.models.github.GitHubAuth](ccutils.models.github.md#ccutils.models.github.GitHubAuth)

#### user *: str*

#### namespace *: str*

#### email *: str*

#### auth *: [GitHubAuth](ccutils.models.github.md#ccutils.models.github.GitHubAuth)*

### *class* ccutils.models.GitHubAuth(, auth_type: Literal['token', 'ssh'] = 'ssh', token: str | None = None, ssh_key_path: Path | None = PosixPath('~/.ssh/id_rsa'))

Bases: `BaseModel`

GitHub authentication types.

#### auth_type

Type of authentication method.

* **Type:**
  Literal['token', 'ssh']

#### token

GitHub personal access token, if using token authentication.

* **Type:**
  str | None

#### ssh_key_path

Path to SSH private key, if using SSH authentication.

* **Type:**
  Path | None

#### auth_type *: Literal['token', 'ssh']*

#### token *: str | None*

#### ssh_key_path *: Path | None*

### *class* ccutils.models.GitHubRepo(, owner: str = '', namespace: str = '', name: str = '', full_name: str = '', description: str = '', url: str = '', html_url: str = '', ssh_url: str = '', clone_url: str = '', is_template: bool = False)

Bases: `BaseModel`

Represents a GitHub repository within a namespace.

#### owner

(str) GitHub repository owner.

* **Type:**
  str

#### namespace

(str) GitHub organization or namespace; often same as user.

* **Type:**
  str

#### name

(str) GitHub repository name.

* **Type:**
  str

#### full_name

(str) GitHub owner fullname.

* **Type:**
  str

#### description

GitHub repository description.

* **Type:**
  str

#### url

(str) GitHub repository url.

* **Type:**
  str

#### html_url

(str).

* **Type:**
  str

#### ssh_url

(str).

* **Type:**
  str

#### clone_url

(str).

* **Type:**
  str

#### is_template

(bool).

* **Type:**
  bool

#### owner *: str*

#### namespace *: str*

#### name *: str*

#### full_name *: str*

#### description *: str*

#### url *: str*

#### html_url *: str*

#### ssh_url *: str*

#### clone_url *: str*

#### is_template *: bool*

### *class* ccutils.models.Metadata(, version: str = '', author: str = '', license: str = '')

Bases: `BaseModel`

metadata type.

#### version

(str).

* **Type:**
  str

#### author

(str).

* **Type:**
  str

#### license

(str).

* **Type:**
  str

#### copyright

(str).

#### *property* copyright *: str*

#### *classmethod* from_package(package_name: str = 'cc-utils') → [Metadata](ccutils.models.metadata.md#ccutils.models.metadata.Metadata)

Create Metadata from the installed package metadata.

Falls back to defaults if the package is not found.

#### version *: str*

#### author *: str*

#### license *: str*

### *class* ccutils.models.Namespace(\*, templates: list[~ccutils.models.template.TemplateRepo] = <factory>, created_at: ~datetime.datetime = <factory>)

Bases: `BaseModel`

A GitHub user/org containing templates

#### templates

(list[TemplateRepo]) List of GitHub namespace/organization template repositories.

* **Type:**
  list[[ccutils.models.template.TemplateRepo](ccutils.models.template.md#ccutils.models.template.TemplateRepo)]

#### templates *: list[[TemplateRepo](ccutils.models.template.md#ccutils.models.template.TemplateRepo)]*

#### created_at *: datetime*

### *class* ccutils.models.TemplateRepo(, repo: [GitHubRepo](ccutils.models.github.md#ccutils.models.github.GitHubRepo), config: [ConfigData](ccutils.models.template.md#ccutils.models.template.ConfigData) | None = None)

Bases: `BaseModel`

A cookiecutter template repo

#### repo

(GitHubRepo) GitHub repository information.

* **Type:**
  [ccutils.models.github.GitHubRepo](ccutils.models.github.md#ccutils.models.github.GitHubRepo)

#### config

(ConfigData) Metadata from a cookiecutter template.

* **Type:**
  [ccutils.models.template.ConfigData](ccutils.models.template.md#ccutils.models.template.ConfigData) | None

#### repo *: [GitHubRepo](ccutils.models.github.md#ccutils.models.github.GitHubRepo)*

#### config *: [ConfigData](ccutils.models.template.md#ccutils.models.template.ConfigData) | None*

### Modules

| [`accounts`](ccutils.models.accounts.md#module-ccutils.models.accounts)       | cc-utils Package   |
|-------------------------------------------------------------------------------|--------------------|
| [`base`](ccutils.models.base.md#module-ccutils.models.base)                   | cc-utils Package   |
| [`ccmeta`](ccutils.models.ccmeta.md#module-ccutils.models.ccmeta)             | cc-utils Package   |
| [`cctemplate`](ccutils.models.cctemplate.md#module-ccutils.models.cctemplate) | cc-utils Package   |
| [`config`](ccutils.models.config.md#module-ccutils.models.config)             | cc-utils Package   |
| [`github`](ccutils.models.github.md#module-ccutils.models.github)             | cc-utils Package   |
| [`metadata`](ccutils.models.metadata.md#module-ccutils.models.metadata)       | cc-utils Package   |
| [`template`](ccutils.models.template.md#module-ccutils.models.template)       | ccutils Package    |
