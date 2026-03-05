# namefyi

[![PyPI](https://img.shields.io/pypi/v/namefyi)](https://pypi.org/project/namefyi/)
[![Python](https://img.shields.io/pypi/pyversions/namefyi)](https://pypi.org/project/namefyi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Pure Python naming engine for developers. [Korean romanization](https://namefyi.com/culture/korean/) using the Revised Romanization system, [Five Elements](https://namefyi.com/) (오행) compatibility analysis from stroke counts, CJK stroke lookup, population formatting, and URL slug generation -- all with zero dependencies.

> **Explore Korean names and meanings at [namefyi.com](https://namefyi.com/)** -- surname histories, character meanings, naming traditions, and romanization tools.

<p align="center">
  <img src="demo.gif" alt="namefyi CLI demo" width="800">
</p>

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [Korean Romanization](#korean-romanization)
- [Five Elements in Korean Naming](#five-elements-오행-in-korean-naming)
- [Utilities](#utilities)
- [Command-Line Interface](#command-line-interface)
- [MCP Server (Claude, Cursor, Windsurf)](#mcp-server-claude-cursor-windsurf)
- [REST API Client](#rest-api-client)
- [API Reference](#api-reference)
  - [Korean Romanization](#korean-romanization-1)
  - [CJK Stroke Count](#cjk-stroke-count)
  - [Five Elements](#five-elements-오행)
  - [Formatting & Slugs](#formatting--slugs)
- [Features](#features)
- [Learn More About Names](#learn-more-about-names)
- [FYIPedia Developer Tools](#fyipedia-developer-tools)
- [License](#license)

## Install

```bash
pip install namefyi              # Core engine (zero deps)
pip install "namefyi[cli]"       # + Command-line interface
pip install "namefyi[mcp]"       # + MCP server for AI assistants
pip install "namefyi[api]"       # + HTTP client for namefyi.com API
pip install "namefyi[all]"       # Everything
```

## Quick Start

```python
from namefyi import romanize_korean, five_elements_for_strokes, check_element_compatibility

# Korean romanization (Revised Romanization)
romanize_korean("김민준")                    # 'gimminjun'
romanize_korean("이서연")                    # 'iseoyeon'

# Five Elements (오행) from stroke count
five_elements_for_strokes(3)                 # '火' (Fire)
five_elements_for_strokes(7)                 # '金' (Metal)

# Element compatibility
check_element_compatibility("木", "火")      # 'compatible' (상생)
check_element_compatibility("木", "土")      # 'incompatible' (상극)
check_element_compatibility("木", "木")      # 'neutral'
```

## Korean Romanization

The [Revised Romanization of Korean](https://en.wikipedia.org/wiki/Revised_Romanization_of_Korean) (국어의 로마자 표기법) was adopted by the South Korean government in 2000, replacing the older McCune-Reischauer system. It is the official standard for road signs, textbooks, and government documents.

Korean Hangul is a featural alphabet where each syllable block is composed of up to three parts: an initial consonant (초성), a medial vowel (중성), and an optional final consonant (종성). The Unicode Hangul Syllables block (U+AC00-U+D7A3) encodes all 11,172 possible syllable combinations. Decomposition follows a mathematical formula:

```
syllable_index = code_point - 0xAC00
initial  = syllable_index // (21 * 28)    # 19 possible initials
medial   = (syllable_index // 28) % 21    # 21 possible medials
final    = syllable_index % 28            # 28 possible finals (0 = none)
```

```python
from namefyi import romanize_korean

# Decomposition and romanization happen automatically
romanize_korean("한글")     # 'hangeul'
romanize_korean("서울")     # 'seoul'
romanize_korean("부산")     # 'busan'
romanize_korean("박지성")   # 'bakjiseong'
```

In practice, Korean surnames have well-established conventional romanizations (Kim, Lee, Park) that differ from the strict Revised Romanization rules (Gim, I, Bak). The `namefyi` engine applies the standard algorithmic rules; conventional surname spellings are handled at the application level.

## Five Elements (오행) in Korean Naming

Traditional Korean naming practice uses the Five Elements cycle (오행, 五行) based on the stroke count of each Hanja character. The five elements -- Wood (木), Fire (火), Earth (土), Metal (金), Water (水) -- follow two fundamental cycles:

**Sangseang (상생, 相生) -- the generative cycle:**
Wood feeds Fire, Fire creates Earth (ash), Earth bears Metal, Metal collects Water (condensation), Water nourishes Wood.

**Sanggeuk (상극, 相剋) -- the overcoming cycle:**
Wood parts Earth, Earth absorbs Water, Water quenches Fire, Fire melts Metal, Metal chops Wood.

```python
from namefyi import five_elements_for_strokes, check_element_compatibility, get_stroke_count

# Stroke count determines element (1-2: Wood, 3-4: Fire, 5-6: Earth, 7-8: Metal, 9-10: Water)
five_elements_for_strokes(1)    # '木' (Wood)
five_elements_for_strokes(5)    # '土' (Earth)

# Check compatibility between elements
check_element_compatibility("水", "木")  # 'compatible' -- Water nourishes Wood (상생)
check_element_compatibility("水", "火")  # 'incompatible' -- Water quenches Fire (상극)

# CJK character stroke count
get_stroke_count("金")   # stroke count for the character
```

In a well-formed Korean name, the elements of the three characters (surname + given name) should follow the generative cycle (상생), creating a harmonious flow of energy. This practice remains culturally significant and is still consulted by many Korean families when naming children.

## Utilities

```python
from namefyi import format_population, surname_slug, character_slug

# Population formatting
format_population(10_345_678)    # '10.3M'
format_population(856_000)       # '856K'

# URL slug generation
surname_slug("김")    # URL-safe slug for surname pages
character_slug("秀")  # URL-safe slug for character pages
```

## Command-Line Interface

```bash
pip install "namefyi[cli]"

namefyi romanize 김민준
namefyi elements 3
namefyi compatibility 木 火
```

## MCP Server (Claude, Cursor, Windsurf)

Add naming tools to any AI assistant that supports [Model Context Protocol](https://modelcontextprotocol.io/).

```bash
pip install "namefyi[mcp]"
```

Add to your `claude_desktop_config.json`:

```json
{
    "mcpServers": {
        "namefyi": {
            "command": "python",
            "args": ["-m", "namefyi.mcp_server"]
        }
    }
}
```

**Available tools**: `romanize_korean`, `five_elements`, `element_compatibility`, `format_population`

## REST API Client

```python
pip install "namefyi[api]"
```

```python
from namefyi.api import NameFYI

with NameFYI() as client:
    results = client.search("Kim")
    character = client.character_lookup("金秀")
    name = client.random_name(gender="male")
```

Full [API documentation](https://namefyi.com/developers/) at namefyi.com.

## API Reference

### Korean Romanization

| Function | Description |
|----------|-------------|
| `romanize_korean(text) -> str` | Revised Romanization of Hangul syllables |

### CJK Stroke Count

| Function | Description |
|----------|-------------|
| `get_stroke_count(char) -> int` | Unicode-based stroke count for CJK characters |

### Five Elements (오행)

| Function | Description |
|----------|-------------|
| `five_elements_for_strokes(count) -> str` | Map stroke count to element (木火土金水) |
| `check_element_compatibility(e1, e2) -> str` | Check 상생/상극 between element pairs |

### Formatting & Slugs

| Function | Description |
|----------|-------------|
| `format_population(n) -> str` | Human-readable population (e.g., "10.3M") |
| `surname_slug(surname) -> str` | URL-safe slug for a Korean surname |
| `character_slug(char) -> str` | URL-safe slug for a CJK character |

## Features

- **Korean romanization** -- Revised Romanization of Hangul syllables
- **Five Elements (오행)** -- stroke count to element mapping (木火土金水)
- **Element compatibility** -- check 상생/상극 between element pairs
- **CJK stroke count** -- Unicode-based stroke lookup
- **Population formatting** -- human-readable numbers (10.3M, 850K)
- **Slug generation** -- URL-safe slugs for surnames and characters
- **CLI** -- Rich terminal output with romanization and element tables
- **MCP server** -- 4 tools for AI assistants (Claude, Cursor, Windsurf)
- **REST API client** -- httpx-based client for [namefyi.com API](https://namefyi.com/developers/)
- **Zero dependencies** -- pure Python standard library only
- **Type-safe** -- full type annotations, `py.typed` marker (PEP 561)

## Learn More About Names

- **Tools**: [Name Search](https://namefyi.com/search/) · [Romanization Tool](https://namefyi.com/tools/romanize/)
- **Browse**: [Korean Names](https://namefyi.com/korean/) · [Cultures](https://namefyi.com/culture/)
- **Guides**: [Glossary](https://namefyi.com/glossary/) · [Blog](https://namefyi.com/blog/)
- **API**: [REST API Docs](https://namefyi.com/developers/) · [OpenAPI Spec](https://namefyi.com/api/openapi.json)

## FYIPedia Developer Tools

Part of the [FYIPedia](https://fyipedia.com) open-source developer tools ecosystem.

| Package | PyPI | npm | Description |
|---------|------|-----|-------------|
| colorfyi | [PyPI](https://pypi.org/project/colorfyi/) | [npm](https://www.npmjs.com/package/@fyipedia/colorfyi) | Color conversion, WCAG contrast, harmonies -- [colorfyi.com](https://colorfyi.com/) |
| emojifyi | [PyPI](https://pypi.org/project/emojifyi/) | [npm](https://www.npmjs.com/package/emojifyi) | Emoji encoding & metadata for 3,781 emojis -- [emojifyi.com](https://emojifyi.com/) |
| symbolfyi | [PyPI](https://pypi.org/project/symbolfyi/) | [npm](https://www.npmjs.com/package/symbolfyi) | Symbol encoding in 11 formats -- [symbolfyi.com](https://symbolfyi.com/) |
| unicodefyi | [PyPI](https://pypi.org/project/unicodefyi/) | [npm](https://www.npmjs.com/package/unicodefyi) | Unicode lookup with 17 encodings -- [unicodefyi.com](https://unicodefyi.com/) |
| fontfyi | [PyPI](https://pypi.org/project/fontfyi/) | [npm](https://www.npmjs.com/package/fontfyi) | Google Fonts metadata & CSS -- [fontfyi.com](https://fontfyi.com/) |
| distancefyi | [PyPI](https://pypi.org/project/distancefyi/) | [npm](https://www.npmjs.com/package/distancefyi) | Haversine distance & travel times -- [distancefyi.com](https://distancefyi.com/) |
| timefyi | [PyPI](https://pypi.org/project/timefyi/) | [npm](https://www.npmjs.com/package/timefyi) | Timezone ops & business hours -- [timefyi.com](https://timefyi.com/) |
| **namefyi** | [PyPI](https://pypi.org/project/namefyi/) | [npm](https://www.npmjs.com/package/namefyi) | Korean romanization & Five Elements -- [namefyi.com](https://namefyi.com/) |
| unitfyi | [PyPI](https://pypi.org/project/unitfyi/) | [npm](https://www.npmjs.com/package/unitfyi) | Unit conversion, 220 units -- [unitfyi.com](https://unitfyi.com/) |
| holidayfyi | [PyPI](https://pypi.org/project/holidayfyi/) | [npm](https://www.npmjs.com/package/holidayfyi) | Holiday dates & Easter calculation -- [holidayfyi.com](https://holidayfyi.com/) |
| cocktailfyi | [PyPI](https://pypi.org/project/cocktailfyi/) | -- | Cocktail ABV, calories, flavor -- [cocktailfyi.com](https://cocktailfyi.com/) |
| fyipedia | [PyPI](https://pypi.org/project/fyipedia/) | -- | Unified CLI: `fyi color info FF6B35` -- [fyipedia.com](https://fyipedia.com/) |
| fyipedia-mcp | [PyPI](https://pypi.org/project/fyipedia-mcp/) | -- | Unified MCP hub for AI assistants -- [fyipedia.com](https://fyipedia.com/) |

## License

MIT
