"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

from .config import ensure_config
from .github import fetch_namespace
from .models import (
    Accounts,
    CLIConfig,
    ConfigData,
    GitHubAccount,
    GitHubAuth,
    GitHubRepo,
    Namespace,
    TemplateRepo,
)

__all__ = [
    # models:
    "Accounts",
    "CLIConfig",
    "ConfigData",
    "GitHubAccount",
    "GitHubAuth",
    "GitHubRepo",
    "Namespace",
    "TemplateRepo",
]

__all__ += [
    # core:
    "ensure_config",
    "fetch_namespace",
]
