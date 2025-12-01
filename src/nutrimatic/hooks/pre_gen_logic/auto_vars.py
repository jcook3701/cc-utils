"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

import datetime
import json
from pathlib import Path


def release_date() -> None:
    # Path to cookiecutter.json in the template folder
    project_dir = Path.cwd()
    json_file = project_dir / "cookiecutter.json"

    with open(json_file) as f:
        context = json.load(f)

    # Add release_date as now
    context["release_date"] = datetime.datetime.now().strftime("%Y-%m-%d")

    # Write it to a file that the template can read
    with open(".cookiecutter_release.json", "w") as f:
        json.dump(context, f)
