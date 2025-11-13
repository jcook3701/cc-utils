"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Github Models:
(GitHubaccount, RepoInfo)
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from .base import BaseModel


@dataclass(frozen=True)
class GitHubAuth(BaseModel):
    """
    GitHub authentication types.

    Attributes:
         auth_type (Literal['token', 'ssh']): Type of authentication method.
         token (str | None): GitHub personal access token, if using token authentication.
         ssh_key_path (Path | None): Path to SSH private key, if using SSH authentication.
    """

    auth_type: Literal["token", "ssh"] = "ssh"
    token: str | None = None
    ssh_key_path: Path | None = Path("~/.ssh/id_rsa")


@dataclass(frozen=True)
class GitHubAccount(BaseModel):
    """
    GitHub users/org personal info

    Attributes:
         user: (str) GitHub username.
         namespace: (str) GitHub organization or namespace; often same as user.
         email: (str) GitHub account email.
         auth: (GitHubAuth) Authentication configuration for GitHub access.
    """

    user: str
    namespace: str
    email: str
    auth: GitHubAuth


@dataclass(frozen=True)
class GitHubRepo(BaseModel):
    """
    Represents a GitHub repository within a namespace.

    Attributes:
         owner: (str) GitHub repository owner.
         namespace: (str) GitHub organization or namespace; often same as user.
         name: (str) GitHub repository name.
         full_name: (str) GitHub owner fullname.
         description: GitHub repository description.
         url: (str) GitHub repository url.
         html_url: (str).
         ssh_url: (str).
         clone_url: (str).
         is_template: (bool).
    """

    owner: str
    namespace: str
    name: str
    full_name: str
    description: str
    url: str
    html_url: str
    ssh_url: str
    clone_url: str
    is_template: bool
