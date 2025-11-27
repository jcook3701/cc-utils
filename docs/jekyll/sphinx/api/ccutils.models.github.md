---
title: ccutils.models.github
layout: default
nav_order: 2
parent: api
---
ccutils.models.github
=====================

<a id="module-ccutils.models.github"></a>

cc-utils Package

Description: Github Models:
(GitHubaccount, RepoInfo)

### Classes

| [`GitHubAccount`](#ccutils.models.github.GitHubAccount)(\*[, user, namespace, email, auth])   | GitHub users/org personal info                     |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------|
| [`GitHubAuth`](#ccutils.models.github.GitHubAuth)(\*[, auth_type, token, ssh_key_path])       | GitHub authentication types.                       |
| [`GitHubRepo`](#ccutils.models.github.GitHubRepo)(\*[, owner, namespace, name, ...])          | Represents a GitHub repository within a namespace. |

### *class* ccutils.models.github.GitHubAuth(, auth_type: Literal['token', 'ssh'] = 'ssh', token: str | None = None, ssh_key_path: Path | None = PosixPath('~/.ssh/id_rsa'))

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

### *class* ccutils.models.github.GitHubAccount(, user: str = '', namespace: str = '', email: str = '', auth: [GitHubAuth](#ccutils.models.github.GitHubAuth) = GitHubAuth(auth_type='ssh', token=None, ssh_key_path=PosixPath('~/.ssh/id_rsa')))

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
  [ccutils.models.github.GitHubAuth](#ccutils.models.github.GitHubAuth)

#### user *: str*

#### namespace *: str*

#### email *: str*

#### auth *: [GitHubAuth](#ccutils.models.github.GitHubAuth)*

### *class* ccutils.models.github.GitHubRepo(, owner: str = '', namespace: str = '', name: str = '', full_name: str = '', description: str = '', url: str = '', html_url: str = '', ssh_url: str = '', clone_url: str = '', is_template: bool = False)

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
