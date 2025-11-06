---
title: ccutils.extract_cookiecutter_config_from_repo
layout: default
nav_order: 2
parent: api
---
ccutils.extract_cookiecutter_config_from_repo
=================================================

### ccutils.extract_cookiecutter_config_from_repo(repo_url: str, branch: str = 'main', output_file: str = 'clean_cookiecutter.json') → Path

Clone a repo, extract cookiecutter.json, remove Jinja placeholders, save locally.
