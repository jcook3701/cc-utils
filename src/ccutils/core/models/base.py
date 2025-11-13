"""ccutils Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Base model for ccutils project models.
"""

from dataclasses import asdict, dataclass, fields, is_dataclass
from typing import Any, TypeVar, cast

T = TypeVar("T", bound="BaseModel")


@dataclass(frozen=True)
class BaseModel:
    """Base class providing common (de)serialization helpers."""

    def to_dict(self) -> dict[str, Any]:
        """Recursively convert a dataclass instance to a dict."""
        if not is_dataclass(self):
            raise TypeError("to_dict() should be called on a dataclass instance")
        return asdict(self)

    @classmethod
    def from_dict(cls: type[T], data: dict[str, Any]) -> T:
        """Instantiate a dataclass from a dict. Supports nested dataclasses."""
        if not is_dataclass(cls):
            raise TypeError("from_dict() should be called on a dataclass class")

        fieldtypes = {f.name: f.type for f in fields(cls)}
        init_data: dict[str, Any] = {}

        for key, typ in fieldtypes.items():
            if key not in data:
                continue
            value = data[key]
            # Recursively create nested dataclasses
            if hasattr(typ, "__dataclass_fields__") and isinstance(value, dict):
                nested_cls = cast(type[BaseModel], typ)
                init_data[key] = nested_cls.from_dict(value)
            else:
                init_data[key] = value

        return cast(T, cls(**init_data))
