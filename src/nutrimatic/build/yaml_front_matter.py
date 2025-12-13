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
    return len(file_path.parents)


def build_front_matter(
    file_path: Path,
    extensions: set[str],
    depth: int,
    project: str,
) -> str:
    """
    Builds front matter for a file.

    Args:
        file_path (Path): _description_
        project (str | None, optional): _description_. Defaults to None.

    Returns:
        str: Returns front matter as a string.
    """
    title = (
        file_path.stem if file_path.suffix.lstrip(".") in extensions else file_path.name
    )
    parent_name = project if depth == 1 else file_path.parent.name
    front_matter = [
        "---",
        f"title: {title}",
        "layout: default",
        f"nav_order: {depth}",
        f"parent: {parent_name}",
        "---",
        "",
    ]
    new_text = "\n".join(front_matter)
    return new_text


def add_front_matter_to_file(
    file_path: Path,
    extensions: set[str],
    depth: int,
    project: str | None = None,
) -> bool:
    """
    Add YAML front matter to a single file.
    Returns True if modified, False if skipped.
    """
    project_name = project or "unknown_project"

    original_content = file_path.read_text(encoding="utf-8")
    # Skip if file already begins with '---'
    if original_content.lstrip().startswith("---"):
        return False

    new_text = (
        build_front_matter(file_path, extensions, depth, project_name)
        + original_content
    )

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
        if file_path.suffix.lower().lstrip(".") not in extensions:
            logger.info(f" - skipped due to extension: {file_path.suffix}")
            continue
        file_path_rel = file_path.relative_to(directory)
        depth = compute_folder_depth(file_path_rel)
        if add_front_matter_to_file(file_path, extensions, depth, project):
            logger.info(f" - front matter added: {file_path}")
            count += 1

    return count
