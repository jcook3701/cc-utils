# {{ site.title }}

__Author:__ {{ site.author }}  
__Version:__ {{ site.version }}  

## Overview
{{ site.description }}

***

![black-format](https://github.com/{{ site.github_username }}/{{ site.repo_name }}/actions/workflows/black-format.yml/badge.svg)
![dependency-check](https://github.com/{{ site.github_username }}/{{ site.repo_name }}/actions/workflows/dependency-check.yml/badge.svg)
![ruff-lint](https://github.com/{{ site.github_username }}/{{ site.repo_name }}/actions/workflows/ruff-lint.yml/badge.svg)
![security-audit](https://github.com/{{ site.github_username }}/{{ site.repo_name }}/actions/workflows/security-audit.yml/badge.svg)
![spellcheck](https://github.com/{{ site.github_username }}/{{ site.repo_name }}/actions/workflows/spellcheck.yml/badge.svg)
![tests](https://github.com/{{ site.github_username }}/{{ site.repo_name }}/actions/workflows/tests.yml/badge.svg)
![typecheck](https://github.com/{{ site.github_username }}/{{ site.repo_name }}/actions/workflows/typecheck.yml/badge.svg)
![yaml-lint](https://github.com/{{ site.github_username }}/{{ site.repo_name }}/actions/workflows/yaml-lint.yml/badge.svg)

***

## 📦 Package Information:
__GitHub:__ [Source Code](https://github.com/jcook3701/{{ site.repo_name }}/)  
__GitDocs:__ [Api Documentation](https://jcook3701.github.io/{{ site.repo_name }}/)  

## 📦 Package Installation:
__PyPi:__ ([stable](https://pypi.org/project/{{ site.repo_name }}/))  
```shell
$ python -m pip install nutri-matic
```
__TestPyPi:__ ([development](https://test.pypi.org/project/{{ site.repo_name }}/))  
```shell
$ python -m pip install -i https://test.pypi.org/simple/ nutri-matic
```

## Command Examples:
### 🔧 nutrimatic (add_docs, extract, run, list)
#### Add Docs:
__Description:__ Add GitHub docs to an existing project using the github-docs-cookiecutter template.
1.
``` shell
$ nutrimatic add-docs $(target_dir)
```

#### Extract:
__Description:__ Clone a repo, extract cookiecutter.json, remove Jinja placeholders, save locally.
1. Run extract command to local cookiecutter repository:
``` shell
$ nutrimatic extract ./python3-cookiecutter
```
__OR__
2. Run extract command to remote github cookiecutter repository:
``` shell
$ nutrimatic extract \
    --repo git@github.com:jcook3701/python3-cookiecutter.git \
    --branch develop \
    --output clean_cookiecutter.json
```
2. Modify extracted json to meet you new projects requirements.

#### Run:
__Description:__ Run a cookiecutter template using a pre-supplied JSON configuration file.
```shell
$ nutrimatic run $(template) $(config)
```

#### List:
__Description:__ List available cookiecutter templates under a namespace.
```shell
$ nutrimatic list
```

***

### ⚙️ Config (nm-config)
__Description:__ nutrimatic configuration tools.  
__Note:__ These are tools that are used to manage package configuration file.  
__Sub-commands:__ (show)  

#### Show:
__Description:__
```shell
$ nm-config show
```

***

### 🔨 Build (nm-build)
__Description:__ Cookiecutter build automation utilities.  
__Note:__ These commands are intended to be used within project Makefiles as build tools. Examples will assume for use in Makefile.  
__Sub-commands:__ (readme, add-yaml-front-matter)

#### Readme:
__Description:__ Generates project readme from projects github-docs jekyll project.  The intention is keep the readme within ```./docs/jekyll``` as the project's single source of truth.  
__Note__: Intended for use within project Makefile as shown below.  
```shell
PROJECT_ROOT := $(PWD)
DOCS_DIR := $(PROJECT_ROOT)/docs
JEKYLL_DIR := $(DOCS_DIR)/jekyll
JEKYLL_BUILD := bundle exec jekyll build --quiet
README_GEN_DIR := $(JEKYLL_DIR)/tmp_readme
README_FILE := $(PROJECT_ROOT)/README.md

readme:
  nm-build readme $(JEKYLL_DIR) $(README_FILE) \
	  --tmp-dir $(README_GEN_DIR) --jekyll-cmd '$(JEKYLL_BUILD)'
```

#### add-yaml-front-matter:
__Description:__ This adds yaml-front-matter to the head of (md, yml, & yaml) files to help beautify github docs.  Intended to be used with [github-docs-cookiecutter](https://github.com/jcook3701/github-docs-cookiecutter)
```shell
$ nm-build add-yaml-front-matter
```

***

## 🍪 Template (nm-templates)
__Description:__ nm-templates tools.  
__Note:__ github-docs-cookiecutter will either be moved to [cc-templates](https://github.com/jcook3701/cc-templates) or be added to cc-templates as a submodule.  
__Sub-commands:__ (generate)  

#### Generate:
__Description:__ This is for custom Cookiecutter template ([cc-templates](https://github.com/jcook3701/cc-templates)) that utilizes ccmeta.toml files to organize projects.  
__Note:__ This feature is still in development.  __(Use at your own risk!!!)__  
__Arguments:__
  * repo: Path to the template repository to generate README.md and Makefile
```shell
$ nm-templates generate $(repo)
```

***

## Development Strategy:
### 🐍️ Build environment (.venv)
__Description:__ This creates python virtual environment and installs all necessary packages.  
``` shell
$ make install
```
### CI/CD Checklist: ```🧬 + 🛡️ + 🎨 + 🔍 + 🎓 + 🧠 + 🧪```
__Description:__  Runs all checks that are used for CI/CD.  This should pass without error before attempting a pull-request.  
__Note:__ All Makefile commands are used in CI/CD to ensure that if they pass locally they should also pass once pushed to github.  
```shell
$ make pre-commit
```
### 🧪 📢 Test Release Project (Test PyPi):
__Description:__ This runs the entire build cycle and results in a new test release to [test.pypi](https://test.pypi.org/project/nutri-matic/).  
```shell
$ make test-release
```
### 📢 Release Project (Github & PyPi):
__Description:__   This runs the entire build cycle and results in a new release to Github and [Pypi](https://pypi.org/project/nutri-matic/).  Project is also versioned up after release has been published.  
```shell
$ make release
```

***

## Make Toolkit (Individual Commands):
### 🧬 Dependency Management (deptry)
```shell
$ make dependency-check
```
### 🛡️ Security Audit (pip-audit)
```shell
$ make security
```
### 🎨 Formatting (black)
```shell
$ make format-check
```
```shell
$ make format-fix
```
### 🔍 Linting (ruff, toml, & yaml-lint)
``` shell
$ make lint-check
```
``` shell
$ make lint-fix
```
### 🎓 Spellchecking (codespell)
```shell
$ make spellcheck
```
### 🧠 Typechecking (mypy)
``` shell
$ make typecheck
```
### 🧪 Testing (pytest)
``` shell
$ make test
```
### 📦 Building (build)
```shell
$ make build
```
### 🚀 Publishing (Twine + Github)
```shell
$ make publish
```
### 🔖 Version Bumping (bumpy-my-version)
```shell
$ make bump-version-patch
```
### ❓ Build Help
``` shell
$ make help
```

***

## Commit Help:
__Note:__ Commits are required to be conventional git commit message.  This helps with the auto-generation of the changelog files and is enforced by pre-commit.  
__example:__  
```shell
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```
* ```<type>```: A required noun that describes the nature of the change.  
* ```[optional scope]```: An optional phrase within parentheses that specifies the part of the codebase being affected (e.g., fix(parser):).  
* ```<description>```: A required short, imperative-mood summary of the changes.  
* ```[optional body]```: A longer description providing additional context and "what and why" details.  
* ```[optional footer(s)]```: Used for adding meta-information, such as issue references (Fixes #123) or indicating breaking changes.  

***

## Requirements:
1. Python 3.11  
```shell
$ sudo apt install python3.11
```
2. [rustup](https://rust-lang.org/tools/install/)  
__Note:__ I found that it is easiest to use rustup to manage rustc and cargo but this is not required.  
__Example:__ Install rustup with the following:  
```shell
$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

3. [git-cliff](https://git-cliff.org/)  
__Note:__ git-cliff can generate changelog files from the Git history by utilizing conventional commits as well as regex-powered custom parsers.  
```shell
$ cargo install git-cliff
```

***

## 🍹Authors Notes:
Their fundamental design flaws are completely hidden by their superficial design flaws.


### TODO's:
1. cc-templates/ccindex.toml
  * create/update this file using the individual ccmeta.toml files in cc-templates
2. Finish updating this.readme with command usage.
3. Readme ```make readme``` should end up being a ci/cd process to ensure it is always up to date.
4. Thinking about adding a ci/cd process for version bumping.  To create a git tag.

### Future Design Decisions:
1. I need to decide whether to change all my current Cookiecutter projects to use the prefix ```cc-``` and use them as submodules within the [cc-templates](https://github.com/jcook3701/cc-templates) repository.  Or to just move the code directly into the cc-templates repository and use it as a monolithic repo.


<!--

2. Need to come up with a new name as ccutils and cc-utils are giving me issues on either pypi or testpypi.
  * Thinking of going with Hitch Hikers Guide to Galaxy based names as this is becoming rediculious.


🧣📖🤖🧑‍🚀👽✨🚀🛸🪐🍹🧃

cc-utils -> slartibartfast, improbability_drive, probability_engine, hyperjumps
cc-templates -> ~~Magrathea~~, restaurant_at_end_of_universe, life_universe_everything

slartibartfast -> src -> fjord
slartibartfast -> Magrathea

SubEtha -> Messaging system.  Good Open Name. (should claim)

To replace cc-utils:
  1. ✅ HeartOfGold
  2. ✅ heart_of_gold, (claim)
  3. ❌ ImprobCore
  4. ✅ improbability_core (claim)
  5. ✅ improb_core
  6. ✅ robot_marvin
To replace cc-templates:
  1. ❌ NutriMatic
  2. ✅ nutri_matic (claim)

__Notes:__
##### Project Theme (Hitch Hikers Guide the Galaxy)
"Don't Panic."
"The ships hung in the sky in much the same way that bricks don't."
"The answer to the great question...of Life, the Universe and Everything...is...forty-two."
"For a moment, nothing happened. Then, after a second or so, nothing continued to happen."
"I may not have gone where I intended to go, but I think I have ended up where I needed to be".
"The story so far: In the beginning the Universe was created. This has made a lot of people very angry and been widely regarded as a bad move".

##### Heart of Gold (cc-utils)
1. “Hi there! This is Eddie, your shipboard computer, and I’m feeling just great, guys, and I know I’m just going to get a bundle of kicks out of any program you care to run through me.”

2. “That ship?” said Ford in sudden excitement. “What happened to it? Do you know?” “It hated me because I talked to it.” “You talked to it?” exclaimed Ford. “What do you mean you talked to it?” “Simple. I got very bored and depressed, so I went and plugged myself in to its external computer feed. I talked to the computer at great length and explained my view of the Universe to it,” said Marvin. “And what happened?” pressed Ford. “It committed suicide,” said Marvin, and stalked off back to the Heart of Gold.

##### Nuri-Matic (cc-utils)
“The Nutri-Matic Drinks Synthesizer claimed to produce the widest possible range of drinks personally matched to the tastes and metabolism of whoever cared to use it. When put to test, however, it invariably produced a plastic cup filled with a liquid which was almost, but not quite, entirely unlike tea.”


cc-python-cli
cc-ansible-role
cc-sphinx-docs
cc-github-docs
-->




<!--
# Authors Second Hidden Notes:

## Development Ideas:
1. Right now I am thinking about adding two different types of meta files.
  * teabag.toml -> This will be used in (cc-templates, to be changed to: )
  * tea.toml -> This will be automatically to generated projects and used for updates.
      1. Potentially human generated and added to a project to allow
-->
