"""MCP server for namefyi — naming tools for AI assistants.

Requires: pip install namefyi[mcp]

Configure in claude_desktop_config.json::

    {
        "mcpServers": {
            "namefyi": {
                "command": "python",
                "args": ["-m", "namefyi.mcp_server"]
            }
        }
    }
"""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("namefyi")


@mcp.tool()
def romanize_korean(hangul: str) -> str:
    """Romanize Korean text using Revised Romanization.

    Decomposes Hangul syllables into their romanized form.

    Args:
        hangul: Korean text to romanize (e.g., "김민준").
    """
    from namefyi import romanize_korean as _romanize

    result = _romanize(hangul)
    lines = [
        "## Romanization",
        "",
        "| Hangul | Romanized |",
        "|--------|----------|",
        f"| {hangul} | {result} |",
    ]
    return "\n".join(lines)


@mcp.tool()
def five_elements(stroke_count: int) -> str:
    """Get the Five Elements (오행) category for a CJK character stroke count.

    Traditional Korean naming maps stroke counts to elements:
    1-2=Wood(木), 3-4=Fire(火), 5-6=Earth(土), 7-8=Metal(金), 9-0=Water(水).

    Args:
        stroke_count: Number of strokes in the CJK character.
    """
    from namefyi import five_elements_for_strokes

    element = five_elements_for_strokes(stroke_count)
    element_names = {"木": "Wood", "火": "Fire", "土": "Earth", "金": "Metal", "水": "Water"}
    name = element_names.get(element, "Unknown")

    lines = [
        "## Five Elements",
        "",
        "| Strokes | Element | Name |",
        "|---------|---------|------|",
        f"| {stroke_count} | {element} | {name} |",
    ]
    return "\n".join(lines)


@mcp.tool()
def element_compatibility(element_a: str, element_b: str) -> str:
    """Check Five Elements (오행) compatibility between two elements.

    Returns whether the pair is compatible (상생), neutral, or incompatible (상극).

    Args:
        element_a: First element symbol (木, 火, 土, 金, or 水).
        element_b: Second element symbol (木, 火, 土, 金, or 水).
    """
    from namefyi import check_element_compatibility

    result = check_element_compatibility(element_a, element_b)
    emoji = {"compatible": "+", "neutral": "~", "incompatible": "-"}.get(result, "")

    return f"## Element Compatibility\n\n{element_a} + {element_b} = **{result}** {emoji}"


@mcp.tool()
def format_population(population: int) -> str:
    """Format a population number with human-readable suffix (M/K).

    Args:
        population: Raw population number (e.g., 10304000).
    """
    from namefyi import format_population as _format

    formatted = _format(population)
    return f"{population:,} → **{formatted}**"


def main() -> None:
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
