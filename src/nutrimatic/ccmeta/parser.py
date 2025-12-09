"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

from pathlib import Path
from typing import Any

import toml


def load_teabag(path: Path) -> dict[str, Any]:
    """Load a teabag.toml file."""
    if not path.exists():
        raise FileNotFoundError(f"No teabag.toml or tea.toml at {path}")
    return toml.load(path)


def find_templates(base_dir: Path) -> list[Path]:
    """Return all template directories containing teabag.toml or tea.toml or pyproject.toml."""
    return [p for p in base_dir.iterdir() if (p / "teabag.toml").exists()]
