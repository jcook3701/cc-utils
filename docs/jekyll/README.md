# {{ site.title }}

__Author:__ {{ site.author }}  
__Version:__ {{ site.version }}  

## Overview
{{ site.description }}  

***

![black-format](https://github.com/jcook3701/cc-utils/actions/workflows/black-format.yml/badge.svg)
![ruff-lint](https://github.com/jcook3701/cc-utils/actions/workflows/ruff-lint.yml/badge.svg)
![tests](https://github.com/jcook3701/cc-utils/actions/workflows/tests.yml/badge.svg)
![typecheck](https://github.com/jcook3701/cc-utils/actions/workflows/typecheck.yml/badge.svg)
![yaml-lint](https://github.com/jcook3701/cc-utils/actions/workflows/yaml-lint.yml/badge.svg)

## Command Examples:
### 🔧 cc-utils (add_docs, extract, run, list)
#### Add Docs:
__Description:__ Add GitHub docs to an existing project using the github-docs-cookiecutter template.  
1. 
``` shell
$ cc-utils add-docs $(target_dir)
```

#### Extract:
__Description:__ Clone a repo, extract cookiecutter.json, remove Jinja placeholders, save locally.  
1.  
``` shell
$ cc-utils extract ./python3-cookiecutter  
```
2. Modify extracted json to meet you new projects requirements.  

3. Run ccutils extract command:  
``` shell
$ cc-utils extract \
    --repo git@github.com:jcook3701/python3-cookiecutter.git \
    --branch develop \
    --output clean_cookiecutter.json  
```

#### Run:
__Description:__ Run a cookiecutter template using a pre-supplied JSON configuration file.  
```shell
$ cc-utils run $(template) $(config)
```

#### List:
__Description:__ List available cookiecutter templates under a namespace.  
```shell
$ cc-utils list
```

***

### ⚙️ Config (cc-config)
__Description:__ cc-utils configuration tools.  
__Note:__ These are tools that are used to manage the cc-utils configuration file.  

#### Sub-commands: (show)

#### Show:
__Description:__
```shell
$ cc-config show
```

***

### 🔨 Build (cc-build)
__Description:__ Cookiecutter build automation utilities.  
__Note:__ These commands are intended to be used within project Makefiles as build tools. Examples will assume for use in Makefile. 
#### Sub-commands: (readme, add-yaml-front-matter)

#### Readme:
__Description:__ Generates project readme from projects github-docs jekyll project.  The intention is keep the readme within ./docs/jekyll as the projects single source of truth.  
__Note__: Replace with real values.  
```shell
PROJECT_ROOT := $(PWD)
DOCS_DIR := $(PROJECT_ROOT)/docs
JEKYLL_DIR := $(DOCS_DIR)/jekyll
JEKYLL_BUILD := bundle exec jekyll build --quiet
README_GEN_DIR := $(JEKYLL_DIR)/tmp_readme

readme:
  cc-build readme $(JEKYLL_DIR) ./README.md \
	  --tmp-dir $(README_GEN_DIR) --jekyll-cmd '$(JEKYLL_BUILD)'
```

#### add-yaml-front-matter:
__Description:__ This adds yaml-front-matter to the head of (md, yml, & yaml) files to help beautify github docs.  Intended to be used with [github-docs-cookiecutter](https://github.com/jcook3701/github-docs-cookiecutter)  
__Note:__ github-docs-cookiecutter will either be moved to [cc-templates](https://github.com/jcook3701/cc-templates) or be added to cc-templates as a submodule.  
```shell
$ cc-templates add-yaml-front-matter
```

***

## 🍪 Template (cc-templates)
__Description:__ cc-templates tools.
__Note:__
#### Sub-commands: (generate)

#### Generate: 
__Description:__ This is for custom Cookiecutter template ([cc-templates](https://github.com/jcook3701/cc-templates)) that utilizes ccmeta.toml files to organize projects.  
__Note:__ This feature is still in development.  __(Use at your own risk!!!)__  
__Arguments:__
  * repo: Path to the template repository to generate README.md and Makefile
```shell
$ cc-templates generate $(repo)
```

***

## Development Strategy
__Note:__ All Makefile commands are used in ci/cd to ensure that if they pass locally they should also pass once pushed to github.  
### 🐍️ Build environment (.venv)
``` shell
$ make install  
```
### 🔍 Linting (ruff & yaml-lint)
``` shell
$ make lint-check  
```
``` shell
$ make lint-fix  
```
### 🎨 Formatting (black)
```shell
$ make format-check
```
```shell
$ make format-fix
```
### 🧠 Typechecking (mypy)
``` shell
$ make typecheck  
```
### 🧪 Testing (pytest)
``` shell
$ make test  
```
### 🔖 Version Bumping (bumpy-my-version)
```shell
$ make bump-version-patch
```
### 📦 Building (build)
```shell
$ make build
```
### 🚀 Publishing (Twine)
```shell
$ make pubish
```
### Build Help
``` shell
$ make help  
```

***

## Authors Notes:
### TODO's:
1. cc-templates/ccindex.toml
  * create/update this file using the individual ccmeta.toml files in cc-templates
2. Finish updating this.readme with command usage.
3. Readme ```make readme``` should end up being a ci/cd process to ensure it is always up to date.
4. Thinking about adding a ci/cd process for version bumping.  To create a git tag.

### Future Design Decisions:
1. I need to decide whether to change all my current Cookiecutter projects to use the prefix ```cc-``` and use them as submodules within the [cc-templates](https://github.com/jcook3701/cc-templates) repository.  Or to just move the code directly into the cc-templates repository and use it as a monolithic repo.

## Package:
### PyPi: (stable)

### TestPyPi: (development)
https://test.pypi.org/project/cc-utils/