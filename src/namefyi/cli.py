"""Command-line interface for namefyi.

Requires: pip install namefyi[cli]

Usage::

    namefyi romanize 김민준
    namefyi elements 3
    namefyi compatibility 木 火
"""

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(
    name="namefyi",
    help="Korean naming engine — romanization, Five Elements, compatibility.",
    no_args_is_help=True,
)
console = Console()


@app.command()
def romanize(
    hangul: str = typer.Argument(help="Korean text to romanize (e.g., 김민준)"),
) -> None:
    """Romanize Korean text using Revised Romanization."""
    from namefyi import romanize_korean

    result = romanize_korean(hangul)

    table = Table(title="Romanization")
    table.add_column("Hangul", style="cyan")
    table.add_column("Romanized", style="green")
    table.add_row(hangul, result)

    console.print(table)


@app.command()
def elements(
    stroke_count: int = typer.Argument(help="Number of strokes in the character"),
) -> None:
    """Get the Five Elements (오행) for a stroke count."""
    from namefyi import five_elements_for_strokes

    element = five_elements_for_strokes(stroke_count)

    element_names = {"木": "Wood", "火": "Fire", "土": "Earth", "金": "Metal", "水": "Water"}
    name = element_names.get(element, "Unknown")

    table = Table(title="Five Elements")
    table.add_column("Strokes", style="cyan")
    table.add_column("Element", style="green")
    table.add_column("Name", style="yellow")
    table.add_row(str(stroke_count), element, name)

    console.print(table)


@app.command()
def compatibility(
    element_a: str = typer.Argument(help="First element (木/火/土/金/水)"),
    element_b: str = typer.Argument(help="Second element (木/火/土/金/水)"),
) -> None:
    """Check Five Elements compatibility between two elements."""
    from namefyi import check_element_compatibility

    result = check_element_compatibility(element_a, element_b)

    style_map = {
        "compatible": "green",
        "neutral": "yellow",
        "incompatible": "red",
    }
    style = style_map.get(result, "white")

    table = Table(title="Element Compatibility")
    table.add_column("Element A", style="cyan")
    table.add_column("Element B", style="cyan")
    table.add_column("Result", style=style)
    table.add_row(element_a, element_b, result)

    console.print(table)
