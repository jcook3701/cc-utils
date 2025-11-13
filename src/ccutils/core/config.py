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
    ga_tracking = "",
    accounts=Accounts(),
)


def ensure_config() -> CLIConfig:
    """Ensure the user config exists and return its contents as a dict."""
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)

    if not CONFIG_PATH.exists():
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)

    with open(CONFIG_PATH, encoding="utf-8") as f:
        data = cast(dict[str, Any], json.load(f))

    # Convert paths back to Path objects if needed
    data["cache_dir"] = Path(data["cache_dir"])
    data["config_file"] = Path(data["config_file"])
    data["log_file"] = Path(data["log_file"])

    return CLIConfig(**data)
