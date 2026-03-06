---
name: name-tools
description: Romanize Korean Hangul text, compute Five Elements (오행) from CJK stroke counts, check element compatibility, and generate URL slugs. Use when working with Korean names, Hanja characters, or CJK text analysis.
license: MIT
metadata:
  author: fyipedia
  version: "0.1.1"
  homepage: "https://namefyi.com/"
---

# NameFYI -- Korean Name Tools for AI Agents

Pure Python naming engine. Korean romanization using Revised Romanization, Five Elements (오행) compatibility from stroke counts, CJK stroke lookup, population formatting, and URL slug generation -- all with zero dependencies.

**Install**: `pip install namefyi` -- **Web**: [namefyi.com](https://namefyi.com/) -- **API**: [REST API](https://namefyi.com/developers/) -- **npm**: `npm install namefyi`

## When to Use

- User asks to romanize Korean text (Hangul to Latin characters)
- User needs Five Elements (오행) analysis for Korean name characters
- User wants to check compatibility between name elements (상생/상극)
- User needs CJK character stroke counts
- User asks about Korean naming traditions or Hanja meanings

## Tools

### `romanize_korean(hangul) -> str`

Romanize Korean text using the Revised Romanization system (syllable-by-syllable decomposition).

```python
from namefyi import romanize_korean

romanize_korean("김민준")    # 'gimminjun'
romanize_korean("이서연")    # 'iseoyeon'
romanize_korean("서울")      # 'seoul'
romanize_korean("부산")      # 'busan'
romanize_korean("한글")      # 'hangeul'
romanize_korean("박지성")    # 'bakjiseong'
```

### `five_elements_for_strokes(stroke_count) -> str`

Determine the Five Elements category from a character's stroke count. Returns one of: 木 (Wood), 火 (Fire), 土 (Earth), 金 (Metal), 水 (Water).

```python
from namefyi import five_elements_for_strokes

five_elements_for_strokes(1)   # '木' (Wood) — 1-2 strokes
five_elements_for_strokes(3)   # '火' (Fire) — 3-4 strokes
five_elements_for_strokes(5)   # '土' (Earth) — 5-6 strokes
five_elements_for_strokes(7)   # '金' (Metal) — 7-8 strokes
five_elements_for_strokes(9)   # '水' (Water) — 9-10 strokes
```

### `check_element_compatibility(element_a, element_b) -> str`

Check Five Elements compatibility between two elements. Returns 'compatible' (상생), 'incompatible' (상극), or 'neutral'.

```python
from namefyi import check_element_compatibility

check_element_compatibility("木", "火")  # 'compatible' (Wood feeds Fire)
check_element_compatibility("水", "木")  # 'compatible' (Water nourishes Wood)
check_element_compatibility("木", "土")  # 'incompatible' (Wood parts Earth)
check_element_compatibility("水", "火")  # 'incompatible' (Water quenches Fire)
check_element_compatibility("木", "木")  # 'neutral' (same element)
```

### `get_stroke_count(character) -> int`

Get the stroke count for a CJK character using Unicode data.

```python
from namefyi import get_stroke_count

get_stroke_count("金")  # stroke count for the character
get_stroke_count("秀")  # stroke count for the character
```

### `format_population(population) -> str`

Format population number with appropriate suffix (M/K).

```python
from namefyi import format_population

format_population(10_304_000)  # '10.3M'
format_population(850_000)     # '850K'
format_population(500)         # '500'
```

### `surname_slug(romanized, culture_slug) -> str`

Generate a URL-safe slug for a surname.

```python
from namefyi import surname_slug

surname_slug("Kim", "korean")  # 'kim-korean'
```

### `character_slug(romanized, meaning_keyword) -> str`

Generate a URL-safe slug for a name character.

```python
from namefyi import character_slug

character_slug("geum", "gold")  # 'geum-gold'
```

## REST API (No Auth Required)

```bash
curl https://namefyi.com/api/romanize/김민준/
curl https://namefyi.com/api/search/Kim/
curl https://namefyi.com/api/character/金/
curl https://namefyi.com/api/random/?gender=male
```

Full spec: [OpenAPI 3.1.0](https://namefyi.com/api/openapi.json)

## Five Elements Reference

| Element | Hanja | Korean | Strokes | Generates | Overcomes |
|---------|-------|--------|---------|-----------|-----------|
| Wood | 木 | 목 (mok) | 1-2 | Fire | Earth |
| Fire | 火 | 화 (hwa) | 3-4 | Earth | Metal |
| Earth | 土 | 토 (to) | 5-6 | Metal | Water |
| Metal | 金 | 금 (geum) | 7-8 | Water | Wood |
| Water | 水 | 수 (su) | 9-10 | Wood | Fire |

## Korean Romanization Reference

| Hangul | Revised | McCune-Reischauer | Conventional |
|--------|---------|-------------------|-------------|
| 김 | gim | kim | Kim |
| 이 | i | yi/i | Lee |
| 박 | bak | pak | Park |
| 최 | choe | ch'oe | Choi |
| 정 | jeong | chong | Jung |

## Demo

![NameFYI demo](https://raw.githubusercontent.com/fyipedia/namefyi/main/demo.gif)

## Utility FYI Family

Part of the [FYIPedia](https://fyipedia.com) ecosystem: [UnitFYI](https://unitfyi.com), [TimeFYI](https://timefyi.com), [HolidayFYI](https://holidayfyi.com), [NameFYI](https://namefyi.com), [DistanceFYI](https://distancefyi.com).
