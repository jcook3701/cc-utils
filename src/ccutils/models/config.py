"""cc-utils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: CLI Configuration model.

Configuration file location: ~/.config/cc-utils/config.yml
"""

from pathlib import Path

from pydantic import BaseModel

from .accounts import Accounts
from .github import GitHubAccount, GitHubAuth


class CLIConfig(BaseModel):
    """
    Represents user CLI configuration for cc-utils.

    Attributes:
         github: (GitHubAccount) GitHub users/org personal info.
         ga_tracking: (str) Google Analytics Tracking number.
         accounts: (Accounts) User accounts.
         default_template_branch: (str)
         cache_dir: (Path) cc-utils cache directory.
         log_file: (Path) cc-utils log file.
         verbose: (bool) cc-utils verbose mode.
    """

    github: GitHubAccount | None = None
    ga_tracking: str | None = None
    accounts: Accounts | None = None

    default_template_branch: str = "main"

    cache_dir: Path = Path.home() / ".cache" / "cc-utils"
    log_file: Path = Path.home() / ".cc-utils" / "ccutlis.log"

    verbose: bool = False

    @property
    def log_dir(self) -> Path:
        return self.log_file.parent


DEFAULT_CONFIG = CLIConfig(
    github=GitHubAccount(user="", namespace="", email="", auth=GitHubAuth()),
    ga_tracking="",
    accounts=Accounts(),
)
