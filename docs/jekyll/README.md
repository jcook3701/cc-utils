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
$ cc-utils add-docs --help
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
$ cc-utils run --help
```

#### List:
__Description:__ List available cookiecutter templates under a namespace.  
```shell
$ cc-utils list --help
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
```makefile
readme:
  cc-build readme $(JEKYLL_DIR) ./README.md \
	  --tmp-dir $(README_GEN_DIR) --jekyll-cmd '$(JEKYLL_BUILD_CMD)'
```

#### add-yaml-front-matter:
__Description:__
```shell
$ cc-templates add-yaml-front-matter
```

***

## 🍪 Template (cc-templates)
__Description:__ cc-templates tools.
__Note:__
#### Sub-commands: (generate)

#### Generate: 
__Description:__
```shell
$ cc-templates generate
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

### Authors Notes:  


### Future Ideas (TODOs):
1. cc-templates/ccindex.toml
  * create/update this file using the individual ccmeta.toml files in cc-templates
2. Finish updating this.readme with command usage.

## Packages
### PyPi (stable)

### TestPyPi (development)
https://test.pypi.org/project/cc-utils/