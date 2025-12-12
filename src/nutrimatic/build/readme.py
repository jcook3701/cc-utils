"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

import shutil
import subprocess
from pathlib import Path

from nutrimatic.core.config import ensure_config
from nutrimatic.core.logger import setup_logging

cfg = ensure_config()  # loads singleton config
logger = setup_logging(cfg)  # loads singleton logger


def _write_front_matter(
    tmp_readme: Path,
    source_readme: Path,
    jekyll_dir: Path,
) -> None:
    """Write the Jekyll front matter + auto-generated comment + original content."""

    with tmp_readme.open("w", encoding="utf-8") as f:
        f.write("---\n")
        f.write("layout: raw\n")
        f.write("permalink: /README.md\n")
        f.write("---\n")
        f.write("<!--\n")
        f.write("  Auto-generated file. Do not edit directly.\n")
        f.write(f"  Edit {source_readme} instead.\n")
        f.write("  Run ```make readme``` to regenerate this file\n")
        f.write("-->\n")
        # Append original README.md content
        f.write((jekyll_dir / "README.md").read_text(encoding="utf-8"))


def readme_generator(
    jekyll_dir: Path,
    output_file: Path,
    readme_gen_dir: Path,
    jekyll_build_cmd: str,
) -> None:
    """_summary_

    Args:
        jekyll_dir (Path): _description_
        output_file (Path): _description_
        readme_gen_dir (Path): _description_
        jekyll_build_cmd (str): _description_
    """

    # Ensure temp build directory exists
    readme_gen_dir.mkdir(parents=True, exist_ok=True)

    # Copy _config.yml and Gemfile
    shutil.copy(jekyll_dir / "_config.yml", readme_gen_dir / "_config.yml")
    shutil.copy(jekyll_dir / "Gemfile", readme_gen_dir / "Gemfile")

    # Write tmp README.md (front matter + comment + content)
    tmp_readme = readme_gen_dir / "README.md"
    source_readme = jekyll_dir / "README.md"
    _write_front_matter(tmp_readme, source_readme, jekyll_dir)

    # Run Jekyll build
    subprocess.run(jekyll_build_cmd, shell=True, check=True, cwd=readme_gen_dir)

    # Copy result back to project
    shutil.copy(readme_gen_dir / "_site/README.md", output_file)

    # Cleanup
    shutil.rmtree(readme_gen_dir)
