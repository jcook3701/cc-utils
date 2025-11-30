"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Entry point for running nutrimatic via `python -m nutrimatic`.
"""

from nutrimatic.cli.main import app


def main() -> None:
    app()


if __name__ == "__main__":
    main()
