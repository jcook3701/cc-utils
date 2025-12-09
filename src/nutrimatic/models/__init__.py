"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Init python models (types)
"""

from .accounts import Accounts
from .ccmeta import CCMeta
from .cctemplate import CCTemplate, CCTemplateVariable
from .config import DEFAULT_CONFIG, CLIConfig
from .github import GitHubAccount, GitHubAuth, GitHubRepo
from .metadata import DEFAULT_METADATA, Metadata
from .template import ConfigData, Namespace, TemplateRepo

__all__ = [
    "DEFAULT_CONFIG",
    "DEFAULT_METADATA",
    "Accounts",
    "CCMeta",
    "CCTemplate",
    "CCTemplateVariable",
    "CLIConfig",
    "ConfigData",
    "GitHubAccount",
    "GitHubAuth",
    "GitHubRepo",
    "Metadata",
    "Namespace",
    "TemplateRepo",
]
