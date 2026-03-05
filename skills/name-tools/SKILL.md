---
name: name-tools
description: Romanize Korean names, check Five Elements compatibility, lookup CJK stroke counts.
---

# Name Tools

Korean name romanization and Five Elements analysis powered by [namefyi](https://namefyi.com/) -- a pure Python name engine with zero dependencies.

## Setup

Install the MCP server:

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

## Available Tools

| Tool | Description |
|------|-------------|
| `romanize_korean` | Romanize a Korean name using Revised Romanization |
| `five_elements` | Analyze the Five Elements (Wuxing) of a Korean name |
| `element_compatibility` | Check Five Elements compatibility between two names |
| `format_population` | Format Korean surname population statistics |

## When to Use

- Converting Korean names to their romanized form
- Analyzing the Five Elements (Wood, Fire, Earth, Metal, Water) of a name
- Checking name compatibility based on traditional East Asian philosophy
- Looking up Korean surname statistics and rankings

## Demo

![NameFYI CLI Demo](https://raw.githubusercontent.com/fyipedia/namefyi/main/demo.gif)

## Links

- [Name Explorer](https://namefyi.com/) -- Korean name analysis tools
- [API Documentation](https://namefyi.com/developers/) -- Free REST API
- [PyPI Package](https://pypi.org/project/namefyi/)
