"""Tests for the namefyi engine."""

from namefyi import (
    character_slug,
    check_element_compatibility,
    five_elements_for_strokes,
    format_population,
    get_stroke_count,
    romanize_korean,
    surname_slug,
)

# ── Korean Romanization ──


def test_romanize_kim_minjun() -> None:
    """김민준 → gimminjun."""
    assert romanize_korean("김민준") == "gimminjun"


def test_romanize_lee_seoyeon() -> None:
    """이서연 → iseoyeon."""
    assert romanize_korean("이서연") == "iseoyeon"


def test_romanize_park() -> None:
    """박 → bak."""
    assert romanize_korean("박") == "bak"


def test_romanize_han() -> None:
    """한 → han."""
    assert romanize_korean("한") == "han"


def test_romanize_non_hangul_passthrough() -> None:
    """Non-Hangul characters pass through unchanged."""
    assert romanize_korean("abc") == "abc"
    assert romanize_korean("123") == "123"


def test_romanize_mixed() -> None:
    """Mixed Hangul and ASCII."""
    result = romanize_korean("김A")
    assert result == "gimA"


def test_romanize_empty() -> None:
    """Empty string returns empty."""
    assert romanize_korean("") == ""


# ── CJK Stroke Count ──


def test_stroke_count_non_cjk() -> None:
    """Non-CJK character returns 0."""
    assert get_stroke_count("A") == 0
    assert get_stroke_count("a") == 0


# ── Five Elements ──


def test_five_elements_wood() -> None:
    """1, 2 strokes → Wood (木)."""
    assert five_elements_for_strokes(1) == "木"
    assert five_elements_for_strokes(2) == "木"
    assert five_elements_for_strokes(11) == "木"
    assert five_elements_for_strokes(12) == "木"


def test_five_elements_fire() -> None:
    """3, 4 strokes → Fire (火)."""
    assert five_elements_for_strokes(3) == "火"
    assert five_elements_for_strokes(4) == "火"
    assert five_elements_for_strokes(13) == "火"


def test_five_elements_earth() -> None:
    """5, 6 strokes → Earth (土)."""
    assert five_elements_for_strokes(5) == "土"
    assert five_elements_for_strokes(6) == "土"


def test_five_elements_metal() -> None:
    """7, 8 strokes → Metal (金)."""
    assert five_elements_for_strokes(7) == "金"
    assert five_elements_for_strokes(8) == "金"


def test_five_elements_water() -> None:
    """9, 0 strokes → Water (水)."""
    assert five_elements_for_strokes(9) == "水"
    assert five_elements_for_strokes(10) == "水"
    assert five_elements_for_strokes(20) == "水"


# ── Element Compatibility ──


def test_compatibility_same_element() -> None:
    """Same element is neutral."""
    assert check_element_compatibility("木", "木") == "neutral"
    assert check_element_compatibility("火", "火") == "neutral"


def test_compatibility_wood_fire() -> None:
    """木 and 火 are compatible (상생)."""
    assert check_element_compatibility("木", "火") == "compatible"
    assert check_element_compatibility("火", "木") == "compatible"


def test_compatibility_fire_earth() -> None:
    """火 and 土 are compatible."""
    assert check_element_compatibility("火", "土") == "compatible"


def test_compatibility_earth_metal() -> None:
    """土 and 金 are compatible."""
    assert check_element_compatibility("土", "金") == "compatible"


def test_compatibility_metal_water() -> None:
    """金 and 水 are compatible."""
    assert check_element_compatibility("金", "水") == "compatible"


def test_compatibility_water_wood() -> None:
    """水 and 木 are compatible."""
    assert check_element_compatibility("水", "木") == "compatible"


def test_incompatibility_wood_earth() -> None:
    """木 and 土 are incompatible (상극)."""
    assert check_element_compatibility("木", "土") == "incompatible"
    assert check_element_compatibility("土", "木") == "incompatible"


def test_incompatibility_earth_water() -> None:
    """土 and 水 are incompatible."""
    assert check_element_compatibility("土", "水") == "incompatible"


def test_incompatibility_water_fire() -> None:
    """水 and 火 are incompatible."""
    assert check_element_compatibility("水", "火") == "incompatible"


def test_incompatibility_fire_metal() -> None:
    """火 and 金 are incompatible."""
    assert check_element_compatibility("火", "金") == "incompatible"


def test_incompatibility_metal_wood() -> None:
    """金 and 木 are incompatible."""
    assert check_element_compatibility("金", "木") == "incompatible"


# ── Population Formatting ──


def test_format_population_millions() -> None:
    assert format_population(10_304_000) == "10.3M"


def test_format_population_millions_small() -> None:
    assert format_population(4_500_000) == "4.5M"


def test_format_population_thousands() -> None:
    assert format_population(850_000) == "850K"


def test_format_population_small_thousands() -> None:
    assert format_population(12_000) == "12K"


def test_format_population_small() -> None:
    assert format_population(500) == "500"


def test_format_population_zero() -> None:
    assert format_population(0) == "0"


# ── Slug Generation ──


def test_surname_slug() -> None:
    assert surname_slug("Kim", "korean") == "kim-korean"


def test_surname_slug_with_space() -> None:
    assert surname_slug("Le Nguyen", "vietnamese") == "le-nguyen-vietnamese"


def test_character_slug() -> None:
    assert character_slug("geum", "gold") == "geum-gold"


def test_character_slug_with_space() -> None:
    assert character_slug("Da Hye", "big wisdom") == "da-hye-big-wisdom"
