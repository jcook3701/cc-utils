"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

from nutrimatic.core.config import ensure_config
from nutrimatic.core.logger import setup_logging
from nutrimatic.core.utils import make_dirs

cfg = ensure_config()  # loads singleton config
logger = setup_logging(cfg)  # loads singleton logger


def generate_cliff_changelog_dirs() -> None:
    """Generate changelog project directories"""
    changelog_dirs = [
        "changelogs",
        "changelogs/releases",
    ]
    make_dirs(changelog_dirs)
