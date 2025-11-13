"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

import json
from pathlib import Path
from typing import Any, cast

from .models import Accounts, CLIConfig, GitHubAccount, GitHubAuth

CONFIG_PATH = Path.home() / ".ccutils" / "config.json"


DEFAULT_CONFIG = CLIConfig(
    github=GitHubAccount(user="", namespace="", email="", auth=GitHubAuth()),
    ga_tracking="",
    accounts=Accounts(),
)


def ensure_config() -> dict[str, Any]:
    """Ensure the user config exists and return it."""
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)

    if not CONFIG_PATH.exists():
        with open(CONFIG_PATH, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)

    with open(CONFIG_PATH) as f:
        data = json.load(f)
        return cast(dict[str, Any], data)
