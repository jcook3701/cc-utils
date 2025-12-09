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


def compute_folder_depth(file_path: Path) -> int:
    zero_depth = {"readme", "index"}
    return 0 if file_path.stem.lower() in zero_depth else len(file_path.parents)


def add_front_matter_to_file(file_path: Path, project: str | None = None) -> bool:
    """
    Add YAML front matter to a single file.
    Returns True if modified, False if skipped.
    """
    # TODO:If README.md is the name change to ansible-autodocs.md
    depth = compute_folder_depth(file_path)
    readme = ["readme", "index"]
    stem = file_path.stem.lower()
    if stem in readme:
        new_name = "ansible-autodocs.md"
        new_path = file_path.with_name(new_name)
    else:
        new_path = file_path
    # Adjust for 'readme' having 0 parents but being at depth 0
    # depth = len(file_path.parents) - (1 if file_path.stem.lower() != "readme" else 0)

    parent_dir = new_path.parent.name or (project or "Project")

    original_content = (
        new_path.read_text(encoding="utf-8")
        if new_path.exists()
        else file_path.read_text(encoding="utf-8")
    )
    # Skip if file already begins with '---'
    if original_content.lstrip().startswith("---"):
        return False

    front_matter = [
        "---",
        f"title: {new_path.stem}",
        "layout: default",
        f"nav_order: {depth}",
        f"parent: {parent_dir}",
        "---",
        "",
    ]
    new_text = "\n".join(front_matter) + original_content
    file_path.write_text(new_text, encoding="utf-8")
    return True


def add_front_matter_to_dir(
    directory: Path,
    extensions: set[str],
    project: str | None = None,
) -> int:
    """
    Walk a directory recursively, adding front matter to all valid extensions.
    Returns the number of files modified.
    """
    count = 0
    for file_path in directory.rglob("*"):
        if not file_path.is_file():
            continue
        logger.debug(f"Checking file: {file_path}")
        if file_path.suffix.lower().lstrip('.') not in extensions:
            logger.info(f" - skipped due to extension: {file_path.suffix}")
            continue
        if add_front_matter_to_file(file_path, project):
            logger.info(f" - front matter added: {file_path}")
            count += 1

    return count