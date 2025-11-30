"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Template Models:
(TemplateRepo, Namespace, ConfigData)
"""

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from .github import GitHubRepo


class ConfigData(BaseModel):
    """
    Metadata from a cookiecutter template project's config.json

    Attributes:
         project_name: Cookiecutter
         author: Cookiecutter
         version: Cookiecutter template version.
         description: Cookiecutter project discription.
         variables: Cookiecutter project variables.
    """

    project_name: str
    author: str
    version: str
    description: str
    variables: dict[str, Any] = Field(default_factory=dict)


class TemplateRepo(BaseModel):
    """
    A cookiecutter template repo

    Attributes:
         repo: (GitHubRepo) GitHub repository information.
         config: (ConfigData) Metadata from a cookiecutter template.
    """

    repo: GitHubRepo
    config: ConfigData | None = None


class Namespace(BaseModel):
    """
    A GitHub user/org containing templates

    Attributes:
        templates: (list[TemplateRepo]) List of GitHub namespace/organization template repositories.
    """

    templates: list[TemplateRepo] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
