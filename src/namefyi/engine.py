"""
NameEngine — stateless pure functions for name computations.

No database access; all inputs are plain Python types.
All functions are deterministic and fast (<1ms).
"""

import unicodedata


def romanize_korean(hangul: str) -> str:
    """Basic Korean romanization (Revised Romanization).

    Handles simple syllable-by-syllable decomposition.
    For complex cases (assimilation, liaison), use a dedicated library.

    Args:
        hangul: Korean text string to romanize.

    Returns:
        Romanized string in lowercase ASCII.

    Examples:
        >>> romanize_korean("김민준")
        'gimminjun'
        >>> romanize_korean("이서연")
        'iseoyeon'
    """
    INITIALS = [
        "g",
        "kk",
        "n",
        "d",
        "tt",
        "r",
        "m",
        "b",
        "pp",
        "s",
        "ss",
        "",
        "j",
        "jj",
        "ch",
        "k",
        "t",
        "p",
        "h",
    ]
    MEDIALS = [
        "a",
        "ae",
        "ya",
        "yae",
        "eo",
        "e",
        "yeo",
        "ye",
        "o",
        "wa",
        "wae",
        "oe",
        "yo",
        "u",
        "wo",
        "we",
        "wi",
        "yu",
        "eu",
        "ui",
        "i",
    ]
    FINALS = [
        "",
        "k",
        "k",
        "k",
        "n",
        "n",
        "n",
        "t",
        "l",
        "l",
        "l",
        "l",
        "l",
        "l",
        "l",
        "l",
        "m",
        "p",
        "p",
        "t",
        "t",
        "ng",
        "t",
        "t",
        "k",
        "t",
        "p",
        "t",
    ]

    result = []
    for char in hangul:
        code = ord(char)
        if 0xAC00 <= code <= 0xD7A3:
            offset = code - 0xAC00
            initial = offset // (21 * 28)
            medial = (offset % (21 * 28)) // 28
            final = offset % 28
            result.append(INITIALS[initial] + MEDIALS[medial] + FINALS[final])
        else:
            result.append(char)

    return "".join(result)


def get_stroke_count(character: str) -> int:
    """Get the stroke count for a CJK character using Unicode data.

    Args:
        character: A single CJK character.

    Returns:
        Stroke count (0 if not a recognized CJK character).

    Note:
        This is a placeholder using character length. Real stroke data
        comes from the Unihan database.
    """
    try:
        name = unicodedata.name(character, "")
        if "CJK" in name:
            return len(character)  # Placeholder — real stroke data comes from Unihan
    except ValueError:
        pass
    return 0


def five_elements_for_strokes(stroke_count: int) -> str:
    """Determine the Five Elements (오행) category from stroke count.

    Traditional Korean naming uses this mapping:
    - 1, 2 strokes -> Wood (木)
    - 3, 4 strokes -> Fire (火)
    - 5, 6 strokes -> Earth (土)
    - 7, 8 strokes -> Metal (金)
    - 9, 0 strokes -> Water (水)

    Args:
        stroke_count: Number of strokes in the character.

    Returns:
        Five Elements symbol (木/火/土/金/水) or empty string.
    """
    remainder = stroke_count % 10
    elements = {
        1: "木",
        2: "木",
        3: "火",
        4: "火",
        5: "土",
        6: "土",
        7: "金",
        8: "金",
        9: "水",
        0: "水",
    }
    return elements.get(remainder, "")


def check_element_compatibility(element_a: str, element_b: str) -> str:
    """Check Five Elements compatibility between two characters.

    Compatible pairs (상생):
    木->火, 火->土, 土->金, 金->水, 水->木

    Incompatible pairs (상극):
    木->土, 土->水, 水->火, 火->金, 金->木

    Args:
        element_a: First Five Elements symbol (木/火/土/金/水).
        element_b: Second Five Elements symbol (木/火/土/金/水).

    Returns:
        One of 'compatible', 'neutral', or 'incompatible'.
    """
    COMPATIBLE = {
        ("木", "火"),
        ("火", "土"),
        ("土", "金"),
        ("金", "水"),
        ("水", "木"),
        ("火", "木"),
        ("土", "火"),
        ("金", "土"),
        ("水", "金"),
        ("木", "水"),
    }
    INCOMPATIBLE = {
        ("木", "土"),
        ("土", "水"),
        ("水", "火"),
        ("火", "金"),
        ("金", "木"),
        ("土", "木"),
        ("水", "土"),
        ("火", "水"),
        ("金", "火"),
        ("木", "金"),
    }

    if element_a == element_b:
        return "neutral"
    if (element_a, element_b) in COMPATIBLE:
        return "compatible"
    if (element_a, element_b) in INCOMPATIBLE:
        return "incompatible"
    return "neutral"


def format_population(population: int) -> str:
    """Format population number with appropriate suffix.

    Args:
        population: Raw population number.

    Returns:
        Formatted string with M/K suffix.

    Examples:
        >>> format_population(10_304_000)
        '10.3M'
        >>> format_population(850_000)
        '850K'
        >>> format_population(500)
        '500'
    """
    if population >= 1_000_000:
        return f"{population / 1_000_000:.1f}M"
    if population >= 1_000:
        return f"{population / 1_000:.0f}K"
    return str(population)


def surname_slug(romanized: str, culture_slug: str) -> str:
    """Generate a URL-safe slug for a surname.

    Args:
        romanized: Romanized surname (e.g., "Kim").
        culture_slug: Culture identifier (e.g., "korean").

    Returns:
        URL slug (e.g., "kim-korean").
    """
    return f"{romanized.lower().replace(' ', '-')}-{culture_slug}"


def character_slug(romanized: str, meaning_keyword: str) -> str:
    """Generate a URL-safe slug for a name character.

    Args:
        romanized: Romanized reading (e.g., "geum").
        meaning_keyword: English meaning (e.g., "gold").

    Returns:
        URL slug (e.g., "geum-gold").
    """
    return f"{romanized.lower().replace(' ', '-')}-{meaning_keyword.lower().replace(' ', '-')}"
