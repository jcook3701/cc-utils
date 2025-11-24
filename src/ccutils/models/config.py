"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: CLI Configuration model.

Configuration file location: ~/.config/ccutils/config.yml
"""

from pathlib import Path

from pydantic import BaseModel

from .accounts import Accounts
from .github import GitHubAccount, GitHubAuth


class CLIConfig(BaseModel):
    """
    Represents user CLI configuration for ccutils.


    Attributes:
         github: (GitHubAccount) GitHub users/org personal info.
         ga_tracking: (str) Google Analytics Tracking number.
         accounts: (Accounts) User accounts.
         default_template_branch: (str)
         cache_dir: (Path) ccutils cache directory.
         log_file: (Path) ccutils log file.
         verbose: (bool) ccutils verbose mode.
    """

    github: GitHubAccount | None = None
    ga_tracking: str | None = None
    accounts: Accounts | None = None

    default_template_branch: str = "main"

    cache_dir: Path = Path.home() / ".cache" / "ccutils"
    log_file: Path = Path.home() / ".ccutils" / "ccutlis.log"

    verbose: bool = False

    @property
    def log_dir(self) -> Path:
        return self.log_file.parent


DEFAULT_CONFIG = CLIConfig(
    github=GitHubAccount(user="", namespace="", email="", auth=GitHubAuth()),
    ga_tracking="",
    accounts=Accounts(),
)
