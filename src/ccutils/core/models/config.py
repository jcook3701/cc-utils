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
         github: (GitHubAccount) GitHub users/org personal info.
         ga_tracking: (str) Google Analytics Tracking number.
         accounts: (Accounts) User accounts.
         default_template_branch: (str)
         cache_dir: (Path) ccutils cache directory.
         config_file: (Path) ccutils configuration file.
         log_file: (Path) ccutils log file.
         verbose: (bool) ccutils verbose mode.
    """

    github: GitHubAccount | None = None
    ga_tracking: str | None = None
    accounts: Accounts | None = None

    default_template_branch: str = "main"

    cache_dir: Path = Path.home() / ".cache" / "ccutils"
    config_file: Path = Path.home() / ".ccutils" / "config.yml"
    log_file: Path = Path.home() / ".ccutils" / "log" / "ccutlis.log"

    verbose: bool = False

    @property
    def config_dir(self) -> Path:
        return self.config_file.parent

    @property
    def log_dir(self) -> Path:
        return self.log_file.parent
