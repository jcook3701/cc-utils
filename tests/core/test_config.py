"""nutri-matic Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Description: Tests for nutrimatic.core.config
"""

from __future__ import annotations

import json
from collections.abc import Generator
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

import pytest
import yaml

import nutrimatic.core.config as config_module
from nutrimatic.models import CLIConfig

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def mock_cli_config() -> MagicMock:
    """Mock CLIConfig with minimal structure."""
    mock: MagicMock = MagicMock(spec=CLIConfig)
    mock.model_dump.return_value = {"key": "value"}
    mock.model_dump_json.return_value = json.dumps({"key": "value"}, indent=4)
    return mock


@pytest.fixture
def mock_default_config(
    mock_cli_config: MagicMock,
) -> Generator[MagicMock, None, None]:
    """Patch DEFAULT_CONFIG with a mock CLIConfig."""
    with patch.object(config_module, "DEFAULT_CONFIG", mock_cli_config):
        yield mock_cli_config


@pytest.fixture
def quiet_logger() -> Generator[None, None, None]:
    """Prevent test output from being cluttered with logs."""
    with patch.object(config_module, "logger"):
        yield


# ---------------------------------------------------------------------------
# _read_config
# ---------------------------------------------------------------------------


def test_read_config_yaml(tmp_path: Path, quiet_logger: None) -> None:
    cfg_file = tmp_path / "config.yml"
    content: dict[str, Any] = {"a": 1, "b": 2}
    cfg_file.write_text(yaml.safe_dump(content))
    result = config_module._read_config(cfg_file)
    assert result == content


def test_read_config_json(tmp_path: Path, quiet_logger: None) -> None:
    cfg_file = tmp_path / "config.json"
    content: dict[str, Any] = {"a": 1}
    cfg_file.write_text(json.dumps(content))
    result = config_module._read_config(cfg_file)
    assert result == content


def test_read_config_missing(tmp_path: Path, quiet_logger: None) -> None:
    cfg_file = tmp_path / "does-not-exist.yml"
    with pytest.raises(FileNotFoundError):
        config_module._read_config(cfg_file)


def test_read_config_wrong_type(tmp_path: Path, quiet_logger: None) -> None:
    cfg_file = tmp_path / "config.yml"
    cfg_file.write_text("[]")  # YAML list, not dict
    with pytest.raises(TypeError):
        config_module._read_config(cfg_file)


# ---------------------------------------------------------------------------
# _write_config
# ---------------------------------------------------------------------------


def test_write_config_yaml(
    tmp_path: Path,
    mock_cli_config: MagicMock,
    mock_default_config: MagicMock,
    quiet_logger: None,
) -> None:
    cfg_file = tmp_path / "out.yml"
    config_module._write_config(cfg_file, mock_cli_config)
    assert cfg_file.exists()
    written = yaml.safe_load(cfg_file.read_text())
    assert written == {"key": "value"}


def test_write_config_json(
    tmp_path: Path,
    mock_cli_config: MagicMock,
    mock_default_config: MagicMock,
    quiet_logger: None,
) -> None:
    cfg_file = tmp_path / "out.json"
    config_module._write_config(cfg_file, mock_cli_config)
    assert cfg_file.exists()
    written = json.loads(cfg_file.read_text())
    assert written == {"key": "value"}


# ---------------------------------------------------------------------------
# _load_or_create_config
# ---------------------------------------------------------------------------


def test_load_or_create_config_existing_valid(
    tmp_path: Path,
    mock_cli_config: MagicMock,
    mock_default_config: MagicMock,
    quiet_logger: None,
) -> None:
    cfg_file = tmp_path / "config.yml"
    cfg_file.write_text(yaml.safe_dump({"key": "value"}))

    with patch.object(CLIConfig, "model_validate", return_value=mock_cli_config):
        cfg = config_module._load_or_create_config(cfg_file)

    assert cfg is mock_cli_config


def test_load_or_create_config_invalid_yaml(
    tmp_path: Path,
    mock_cli_config: MagicMock,
    mock_default_config: MagicMock,
    quiet_logger: None,
) -> None:
    cfg_file = tmp_path / "config.yml"
    cfg_file.write_text("not: valid: yaml:::")  # corrupt YAML

    with patch.object(
        CLIConfig, "model_validate", side_effect=Exception("validation error")
    ):
        cfg = config_module._load_or_create_config(cfg_file)

    assert cfg is mock_cli_config
    assert cfg_file.exists()


def test_load_or_create_config_missing_file(
    tmp_path: Path,
    mock_cli_config: MagicMock,
    mock_default_config: MagicMock,
    quiet_logger: None,
) -> None:
    cfg_file = tmp_path / "missing.yml"

    with patch.object(CLIConfig, "model_validate", return_value=mock_cli_config):
        cfg = config_module._load_or_create_config(cfg_file)

    assert cfg is mock_cli_config
    assert cfg_file.exists()


# ---------------------------------------------------------------------------
# ensure_config
# ---------------------------------------------------------------------------


def test_ensure_config_uses_cache(
    tmp_path: Path,
    mock_cli_config: MagicMock,
    mock_default_config: MagicMock,
    quiet_logger: None,
) -> None:
    with patch.object(config_module, "CONFIG_PATH", tmp_path / "config.yml"):
        config_module.ensure_config.cache_clear()

        with patch.object(
            config_module, "_load_or_create_config", return_value=mock_cli_config
        ) as mock_load:
            c1 = config_module.ensure_config()
            c2 = config_module.ensure_config()

        mock_load.assert_called_once()
        assert c1 is c2
        assert c1 is mock_cli_config
