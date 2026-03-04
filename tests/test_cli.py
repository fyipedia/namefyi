"""Tests for the namefyi CLI."""

from typer.testing import CliRunner

from namefyi.cli import app

runner = CliRunner()


def test_romanize_command() -> None:
    result = runner.invoke(app, ["romanize", "김민준"])
    assert result.exit_code == 0
    assert "gimminjun" in result.output


def test_romanize_single_syllable() -> None:
    result = runner.invoke(app, ["romanize", "한"])
    assert result.exit_code == 0
    assert "han" in result.output


def test_elements_command() -> None:
    result = runner.invoke(app, ["elements", "3"])
    assert result.exit_code == 0
    assert "火" in result.output
    assert "Fire" in result.output


def test_elements_water() -> None:
    result = runner.invoke(app, ["elements", "9"])
    assert result.exit_code == 0
    assert "水" in result.output
    assert "Water" in result.output


def test_compatibility_compatible() -> None:
    result = runner.invoke(app, ["compatibility", "木", "火"])
    assert result.exit_code == 0
    assert "compatible" in result.output


def test_compatibility_incompatible() -> None:
    result = runner.invoke(app, ["compatibility", "木", "土"])
    assert result.exit_code == 0
    assert "incompatible" in result.output
