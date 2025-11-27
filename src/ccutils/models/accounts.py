"""cc-utils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Accounts Model:
(Accounts)
"""

from pydantic import BaseModel


class Accounts(BaseModel):
    """
    Represents user accounts.

    Attributes:
        github_username (str): GitHub username of the account.
        twitter_username (str): Twitter handle.
        linkedin_usercode (str): LinkedIn user code.
        buymeacoffee_username (str): BuyMeACoffee username.
    """

    github_username: str = ""
    twitter_username: str = ""
    linkedin_usercode: str = ""
    buymeacoffee_username: str = ""
