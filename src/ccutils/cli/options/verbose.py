"""cc-utils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Options Imports.
"""

from dataclasses import replace
from typing import Any

from ccutils.core.logger import setup_logging
from ccutils.models import CLIConfig


def verbose_mode(cfg: CLIConfig, verbose: bool) -> Any:
    """
    Handle the --verbose / -v flag.

    Override verbosity if CLI flag provided
    """
    if verbose:
        cfg = replace(cfg, verbose=True)
    logger = setup_logging(cfg)

    logger.debug("Verbose mode enabled.")
    logger.debug(f"Loaded configuration: {cfg}")

    return {"cfg": cfg, "logger": logger}
