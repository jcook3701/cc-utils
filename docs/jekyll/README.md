# {{ site.title }}

__Author:__ {{ site.author }}  
__Version:__ {{ site.version }}  

## Overview
{{ site.description }}  

## Development
### Build environment (.venv)
``` shell
$ make install  
```
### Linting (ruff & yaml-lint)
2.
``` shell
$ make lint-check  
```
### Typechecking (mypy)
``` shell
$ make typecheck  
```
### Testing (pytest)
``` shell
$ make test  
```
### Build Help
``` shell
$ make help  
```
## Usage
1. Source environment created by ```make install```.  
``` shell
$ source .venv  
```

## Usage (Commands)
### Add Docs  
__Description:__ Add GitHub docs to an existing project using the github-docs-cookiecutter template.  
1.  
``` shell
```

### Extract  
__Description:__ Clone a repo, extract cookiecutter.json, remove Jinja placeholders, save locally.  
1.  
``` shell
$ ccutils extract ./python3-cookiecutter  
```
2. Modify extracted json to meet you new projects requirements.  

3. Run ccutils extract command:  
``` shell
$ ccutils extract \
    --repo git@github.com:jcook3701/python3-cookiecutter.git \
    --branch develop \
    --output clean_cookiecutter.json  
```

### Run  
__Description:__ Run a cookiecutter template using a pre-supplied JSON configuration file.  
1.  
``` shell
```
