"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: ccutils project logger.
"""

import logging
import sys
from pathlib import Path
from typing import TextIO

from .models import CLIConfig


def _log_formatter(verbose: bool = False) -> logging.Formatter:
    """Return a logging formatter depending on verbosity."""
    fmt = "%(asctime)s | %(levelname)s | %(message)s" if verbose else "%(message)s"
    datefmt = "%H:%M:%S"
    return logging.Formatter(fmt, datefmt)


def _console_handler(cfg: CLIConfig, verbose: bool = False) -> logging.StreamHandler[TextIO]:
    """Return a configured StreamHandler for console output."""
    console_handler: logging.StreamHandler[TextIO] = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG if verbose else logging.INFO)
    console_handler.setFormatter(_log_formatter(verbose))
    return console_handler


def _file_handler(cfg: CLIConfig) -> logging.FileHandler:
    """Return a FileHandler writing logs to"""
    log_dir: Path = cfg.log_dir
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = cfg.log_file

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            "%Y-%m-%d %H:%M:%S",
        )
    )
    return file_handler


def setup_logging(cfg: CLIConfig, verbose: bool | None, log_to_file: bool = True) -> logging.Logger:
    """
    Configure and return the main ccutils logger.

    Can be called at CLI startup, or once globally from config.
    """
    verbose_mode = verbose if verbose else cfg.verbose
    logger = logging.getLogger("ccutils")  # create a module-wide logger
    logger.setLevel(logging.DEBUG if verbose_mode else logging.INFO)
    logger.handlers.clear()  # avoid duplicate logs in repeated runs

    logger.addHandler(_console_handler(cfg, verbose_mode))
    if log_to_file:
        logger.addHandler(_file_handler(cfg))

    return logger
