"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

from pydantic import BaseModel, Field

from .cctemplate import CCTemplate


class CCMeta(BaseModel):
    """
    Root model for ccmeta.toml.
    Adjust fields as needed to match your ccmeta.toml structure.
    """

    # If your file describes a single template:
    template: CCTemplate

    # Convenience / repo-level metadata
    tags: list[str] = Field(default_factory=list)
    features: list[str] = Field(default_factory=list)

    # Accept arbitrary extra keys (keeps backward compatibility)
    extra: dict[str, object] = Field(default_factory=dict)

    class Config:
        extra = "allow"
