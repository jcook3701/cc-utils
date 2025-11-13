"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Accounts Model:
(Accounts)
"""

from dataclasses import dataclass

from .base import BaseModel

dataclass(frozen=True)


class Accounts(BaseModel):
    """
    Represents user accounts.

    Attributes:
         github_username:
         twitter_username:
         linkedin_username:
         buymeacoffee_username:
    """

    github_username: str = ""
    twitter_username: str = ""
    linkedin_usercode: str = ""
    buymeacoffee_username: str = ""
