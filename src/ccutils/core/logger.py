"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: ccutils project logger.
"""

import logging
import sys
from functools import cache
from pathlib import Path
from typing import TextIO

import typer

from ccutils.models import CLIConfig


@cache
class TyperHandler(logging.Handler):
    """Custom handler that routes log messages to typer.echo()."""

    def __init__(self, stream: TextIO | None = None) -> None:
        super().__init__()
        self.stream = stream or sys.stdout

    def emit(self, record: logging.LogRecord) -> None:
        try:
            msg = self.format(record)
            try:
                # Try to use typer.echo() if running under a Typer context
                typer.echo(msg, file=self.stream)
            except Exception:
                # Fallback to normal write
                self.stream.write(msg + "\n")
                self.stream.flush()
        except Exception:
            self.handleError(record)


def _log_formatter(verbose: bool = False) -> logging.Formatter:
    """Return a logging formatter depending on verbosity."""
    fmt = "%(asctime)s | %(levelname)s | %(message)s" if verbose else "%(message)s"
    datefmt = "%H:%M:%S"
    return logging.Formatter(fmt, datefmt)


def _console_handler(cfg: CLIConfig, verbose: bool = False) -> logging.Handler:
    """Return a console handler — uses TyperHandler for CLI-aware output."""

    handler: logging.Handler = TyperHandler()

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


def setup_logging(cfg: CLIConfig, log_to_file: bool = True) -> logging.Logger:
    """
    Configure and return the main ccutils logger.

    Can be called at CLI startup, or once globally from config.
    """
    logger = logging.getLogger("ccutils")  # create a module-wide logger
    logger.setLevel(logging.DEBUG if cfg.verbose else logging.INFO)
    logger.handlers.clear()  # avoid duplicate logs in repeated runs

    logger.addHandler(_console_handler(cfg, cfg.verbose))
    if log_to_file:
        logger.addHandler(_file_handler(cfg))

    return logger
