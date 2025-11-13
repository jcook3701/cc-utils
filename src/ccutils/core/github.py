"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Github API Core
"""

import json

import requests

from .models import ConfigData, GitHubRepo, Namespace, TemplateRepo


def fetch_config(repo_url: str) -> ConfigData | None:
    """
    Fetch cookiecutter.json from a GitHub repo,
    trying both main and master branches.
    """
    base_raw_url = repo_url.replace("github.com", "raw.githubusercontent.com")
    branches = ["main", "master"]

    for branch in branches:
        raw_url = f"{repo_url}/raw/{branch}/config.json"
        resp = requests.get(raw_url)

        if resp.status_code == 200:
            try:
                data = json.loads(resp.text)
                return ConfigData(
                    project_name=data.get("project_name", ""),
                    author=data.get("author", ""),
                    version=data.get("version", ""),
                    description=data.get("description", ""),
                    variables=data,
                )
            except json.JSONDecodeError:
                return None

    return None


def fetch_namespace(namespace: str) -> Namespace:
    """Fetch all repositories in a namespace and their configs."""
    url = f"https://api.github.com/users/{namespace}/repos"
    resp = requests.get(url)
    resp.raise_for_status()
    repos = resp.json()

    templates = []
    for repo in repos:
        repo_url = repo["html_url"]
        config = fetch_config(repo_url)
        owner = repo["owner"]["login"] if "owner" in repo else namespace

        if config:
            templates.append(
                TemplateRepo(
                    repo=GitHubRepo(
                        owner=owner,
                        namespace=owner,
                        name=repo.get("name", ""),
                        full_name=repo.get("full_name", ""),
                        description=repo.get("description", ""),
                        url=repo.get("url", ""),
                        html_url=repo_url,
                        ssh_url=repo.get("ssh_url", ""),
                        clone_url=repo.get("clone_url", ""),
                        is_template=repo.get("is_template", ""),
                    ),
                    config=config,
                )
            )

    return Namespace(templates=templates)
