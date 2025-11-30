"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

from pathlib import Path

from nutrimatic.core.config import ensure_config
from nutrimatic.core.logger import setup_logging

cfg = ensure_config()  # loads singleton config
logger = setup_logging(cfg)  # loads singleton logger


def generate_ansible_dirs() -> None:
    """Generate ansible project directories"""
    project_dir = Path.cwd()
    ansible_dirs = [
        "playbooks",
        "roles",
        "tests",
        "tests/unit/",
        "tests/integration",
    ]

    for d in ansible_dirs:
        dir_path = project_dir / d
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)
            logger.info(f"📁 Created {dir_path}")
        else:
            logger.info(f"✔️  {dir_path} already exists")
