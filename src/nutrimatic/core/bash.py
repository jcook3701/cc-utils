"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Bash commands ported to python.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

from nutrimatic.core.config import ensure_config
from nutrimatic.core.logger import setup_logging

cfg = ensure_config()  # loads singleton config
logger = setup_logging(cfg)  # loads singleton logger


def clean() -> None:
    """Remove _shared_hooks directory."""
    _shared_hooks = Path.cwd() / "_shared_hooks"
    logger.info(f"hooks directory: {_shared_hooks}")
    if _shared_hooks.exists() and _shared_hooks.is_dir():
        shutil.rmtree(_shared_hooks)
        logger.info(f"Removed {_shared_hooks} directory.")
    else:
        logger.info("_shared_hooks directory does not exist, nothing to remove.")


def make(cmd: str) -> None:
    """Run a make target inside post-gen, exiting on failure."""
    logger.info(f"▶ Running: make {cmd}")
    result = subprocess.run(["make", cmd], check=True)
    if result.returncode != 0:
        logger.error(f"❌ Command failed: make {cmd}")
        sys.exit(result.returncode)


def tree() -> None:
    """Run tree cmd inside the post-gen."""
    logger.info(f"Current working directory: {os.getcwd()}")
    subprocess.run(["tree", "-a", "."], check=False)
