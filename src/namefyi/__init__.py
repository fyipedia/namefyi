"""namefyi — Pure Python naming engine for developers.

Korean romanization, Five Elements compatibility, CJK stroke count,
population formatting, and slug generation. Zero dependencies.

Basic usage::

    >>> from namefyi import romanize_korean, five_elements_for_strokes
    >>> romanize_korean("김민준")
    'gimminjun'
    >>> five_elements_for_strokes(3)
    '火'
"""

from namefyi.engine import (
    character_slug,
    check_element_compatibility,
    five_elements_for_strokes,
    format_population,
    get_stroke_count,
    romanize_korean,
    surname_slug,
)

__version__ = "0.1.0"

__all__ = [
    # Korean romanization
    "romanize_korean",
    # CJK stroke count
    "get_stroke_count",
    # Five Elements (오행)
    "five_elements_for_strokes",
    "check_element_compatibility",
    # Formatting
    "format_population",
    # Slug generation
    "surname_slug",
    "character_slug",
]
