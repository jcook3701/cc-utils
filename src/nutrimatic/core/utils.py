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


def make_dirs(dirs: list[str], project_dir: Path = Path.cwd()) -> None:
    """Generate project directories"""
    for d in dirs:
        dir_path = project_dir / d
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)
            logger.info(f"📁 Created {dir_path}")
        else:
            logger.info(f"✔️  {dir_path} already exists")
