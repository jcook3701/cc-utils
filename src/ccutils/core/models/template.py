"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Template Models:
(TemplateRepo, Namespace, ConfigData)
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from .base import BaseModel
from .github import GitHubRepo


@dataclass(frozen=True)
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
    variables: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class TemplateRepo(BaseModel):
    """
    A cookiecutter template repo

    Attributes:
         repo: (GitHubRepo) GitHub repository information.
         config: (ConfigData) Metadata from a cookiecutter template.
    """

    repo: GitHubRepo
    config: ConfigData | None = None


@dataclass(frozen=True)
class Namespace(BaseModel):
    """
    A GitHub user/org containing templates

    Attributes:
        templates: (list[TemplateRepo]) List of GitHub namespace/organization template repositories.
    """

    templates: list[TemplateRepo] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)
