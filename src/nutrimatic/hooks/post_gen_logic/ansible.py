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


def generate_ansible_dirs() -> None:
    """Generate ansible project directories"""
    ansible_dirs = [
        "plugins",
        "plugins/action",
        "plugins/inventory",
        "plugins/lookup",
        "plugins/module_utils",
        "plugins/modules",
        "playbooks",
        "playbooks/files",
        "playbooks/tasks",
        "playbooks/templates",
        "playbooks/vars",
        "roles",
        "tests",
        "tests/units/",
        "tests/units/plugins",
        "tests/units/plugins/action",
        "tests/units/plugins/inventory",
        "tests/units/plugins/lookup",
        "tests/units/plugins/module_utils",
        "tests/units/plugins/modules",
        "tests/integration",
        "tests/integration/targets",
    ]
    make_dirs(ansible_dirs)
