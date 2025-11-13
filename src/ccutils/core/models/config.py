"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: CLI Configuration models:
(CLIConfig)
"""

from dataclasses import dataclass
from pathlib import Path

from .accounts import Accounts
from .base import BaseModel
from .github import GitHubAccount


@dataclass(frozen=True)
class CLIConfig(BaseModel):
    """
    Represents user CLI configuration for ccutils.


    Attributes:
         github: GitHub users/org personal info.
         ga_tracking: Google Analytics Tracking number.
         accounts: User accounts.

         default_template_branch:
         cache_dir: ccutils cache directory.
         verbose: ccutils verbose mode.
    """

    github: GitHubAccount
    ga_tracking: str
    accounts: Accounts | None

    token: str | None = None
    default_template_branch: str = "main"
    cache_dir: Path = Path.home() / ".cache" / "ccutils"
    verbose: bool = False
