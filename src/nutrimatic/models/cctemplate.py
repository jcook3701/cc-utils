"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
"""

from pathlib import Path

from pydantic import BaseModel, Field


class CCTemplateVariable(BaseModel):
    """Represents a single cookiecutter input variable."""

    name: str
    default: str | None = None
    description: str | None = None


class CCTemplate(BaseModel):
    """
    A single template defined in ccmeta.toml.
    """

    # --- universal / global template metadata ---
    name: str
    description: str | None = None
    path: Path = Field(..., description="Relative path to the template folder")

    # consistent across all project types:
    language: str | None = None  # e.g. "python", "node", "ansible"
    license: str | None = "MIT"  # default license
    version: str | None = "0.1.0"  # template versioning
    maintainer: str | None = None  # "Jared Cook", etc.
    project_type: str | None = None  # "library", "service", "cli"...

    # ─── cookiecutter input variables (template-specific) ───
    variables: list[CCTemplateVariable] = Field(
        default_factory=list, description="User input variables used by the template"
    )

    # ─── tags / feature flags ───
    tags: list[str] = Field(default_factory=list)
    features: list[str] = Field(default_factory=list)

    class Config:
        extra = "allow"
