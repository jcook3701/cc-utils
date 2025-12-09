"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

import os
from pathlib import Path
from typing import Any

from nutrimatic.core.config import ensure_config
from nutrimatic.core.logger import setup_logging

cfg = ensure_config()  # loads singleton config
logger = setup_logging(cfg)  # loads singleton logger


def replace_placeholders_in_file(
    filepath: Path,
    replacements: dict[str, Any],
) -> None:
    """Reads a file, replaces the placeholder, and writes it back."""
    try:
        text = filepath.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        logger.debug(f"Skipping binary file: {filepath}")
        pass
    except Exception as e:
        logger.info(f"An error occurred processing file {filepath}: {e}")

    changed = False

    for placeholder, value in replacements.items():
        if placeholder in text:
            text = text.replace(placeholder, str(value))
            changed = True

    if changed:
        filepath.write_text(text, encoding="utf-8")
        logger.debug(f"Updated: {filepath}")


def replace_placeholders_in_dir(
    replacements: dict[str, Any],
    path: Path = Path.cwd(),
) -> None:
    """
    Walk through every file in the newly generated project directory
    and replace placeholders in all files.
    """
    for root, _dirs, files in os.walk(path):
        for file in files:
            # Exclude this hook script itself from the replacement
            if file == "post_gen_project.py":
                continue

            file_path: Path = Path(root) / file
            replace_placeholders_in_file(file_path, replacements)

    logger.debug("Timestamp injection complete.")
