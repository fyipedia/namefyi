# namefyi

Pure Python naming engine — Korean romanization, Five Elements compatibility, CJK stroke count. Zero dependencies.

## Install

```bash
pip install namefyi              # Core (zero deps)
pip install "namefyi[cli]"       # + CLI (typer, rich)
pip install "namefyi[mcp]"       # + MCP server
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

## Features

- **Korean romanization** — Revised Romanization of Hangul syllables
- **Five Elements (오행)** — stroke count to element mapping (木火土金水)
- **Element compatibility** — check 상생/상극 between element pairs
- **CJK stroke count** — Unicode-based stroke lookup
- **Population formatting** — human-readable numbers (10.3M, 850K)
- **Slug generation** — URL-safe slugs for surnames and characters

## CLI

```bash
namefyi romanize 김민준
namefyi elements 3
namefyi compatibility 木 火
```

## MCP Server

Add to your Claude Desktop config:

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

Tools: `romanize_korean`, `five_elements`, `element_compatibility`, `format_population`

## API Client

```python
from namefyi.api import NameFYI

with NameFYI() as client:
    results = client.search("Kim")
    character = client.character_lookup("金秀")
    name = client.random_name(gender="male")
```

## License

MIT
