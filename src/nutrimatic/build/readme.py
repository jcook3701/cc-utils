"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

from pathlib import Path


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
