"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

from pathlib import Path

from jinja2 import Template

from nutrimatic.ccmeta import find_templates, load_ccmeta


def generate_readme(repo_dir: Path) -> None:
    templates_dir = repo_dir / "templates"
    repo_meta = load_ccmeta(repo_dir / "ccmeta.toml")

    readme_template = """# {{ repo_name }}

{{ repo_desc }}

## Templates Included
{% for t in templates %}
- **{{ t.name }}**: {{ t.description }}
{% endfor %}
"""
    templates_info = []
    for template_dir in find_templates(templates_dir):
        meta = load_ccmeta(template_dir)
        templates_info.append(
            {
                "name": meta["project"]["name"],
                "description": meta["project"]["description"],
            }
        )

    content = Template(readme_template).render(
        repo_name=repo_meta["project"]["name"],
        repo_desc=repo_meta["project"]["description"],
        templates=templates_info,
    )
    (repo_dir / "README.md").write_text(content)


def generate_makefile(repo_dir: Path) -> None:
    templates_dir = repo_dir / "templates"
    makefile_lines = ["PYTHON=python3\n"]

    for template_dir in find_templates(templates_dir):
        meta = load_ccmeta(template_dir)
        target_name = meta["project"]["name"].replace("-", "_")
        makefile_lines.append(
            f"{target_name}:\n\t@echo 'Building template {meta['project']['name']}'\n"
        )

    (repo_dir / "Makefile").write_text("\n".join(makefile_lines))
