"""Tests for the namefyi MCP server."""

from namefyi.mcp_server import (
    element_compatibility,
    five_elements,
    format_population,
    romanize_korean,
)


def test_romanize_korean() -> None:
    result = romanize_korean("김민준")
    assert "gimminjun" in result
    assert "김민준" in result
    assert "Romanization" in result


def test_romanize_korean_single() -> None:
    result = romanize_korean("박")
    assert "bak" in result


def test_five_elements_fire() -> None:
    result = five_elements(3)
    assert "火" in result
    assert "Fire" in result


def test_five_elements_water() -> None:
    result = five_elements(9)
    assert "水" in result
    assert "Water" in result


def test_element_compatibility_compatible() -> None:
    result = element_compatibility("木", "火")
    assert "compatible" in result


def test_element_compatibility_incompatible() -> None:
    result = element_compatibility("木", "土")
    assert "incompatible" in result


def test_format_population_millions() -> None:
    result = format_population(10_304_000)
    assert "10.3M" in result
    assert "10,304,000" in result


def test_format_population_small() -> None:
    result = format_population(500)
    assert "500" in result
