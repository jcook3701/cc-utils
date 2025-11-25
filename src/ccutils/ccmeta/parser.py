"""cc-utils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

from pathlib import Path
from typing import Any

import toml


def load_ccmeta(path: Path) -> dict[str, Any]:
    """Load a ccmeta.toml file."""
    if not path.exists():
        raise FileNotFoundError(f"No ccmeta.toml at {path}")
    return toml.load(path)


def find_templates(base_dir: Path) -> list[Path]:
    """Return all template directories containing ccmeta.toml."""
    return [p for p in base_dir.iterdir() if (p / "ccmeta.toml").exists()]
