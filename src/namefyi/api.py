"""HTTP API client for namefyi.com REST endpoints.

Requires: pip install namefyi[api]

Usage::

    from namefyi.api import NameFYI

    with NameFYI() as client:
        results = client.search("Kim")
        print(results)
"""

from __future__ import annotations

from typing import Any

import httpx


class NameFYI:
    """API client for the namefyi.com REST API."""

    def __init__(
        self,
        base_url: str = "https://namefyi.com/api",
        timeout: float = 10.0,
    ) -> None:
        self._client = httpx.Client(base_url=base_url, timeout=timeout)

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        resp = self._client.get(path, params={k: v for k, v in params.items() if v is not None})
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    def search(self, query: str, limit: int = 10) -> list[dict[str, Any]]:
        """Search for names, surnames, or characters.

        Args:
            query: Search query string (e.g., "Kim", "민준").
            limit: Maximum results to return.

        Returns:
            List of matching result dicts.
        """
        result = self._get("/search/", q=query, limit=limit)
        if isinstance(result, list):
            return list(result)
        results: list[dict[str, Any]] = result.get("results", [])
        return results

    def character_lookup(self, query: str) -> dict[str, Any]:
        """Look up a CJK character (hanja/kanji/hanzi).

        Args:
            query: Character(s) to look up (e.g., "金秀").

        Returns:
            Dict with character information (readings, meanings, stroke count).
        """
        return self._get("/character-lookup/", q=query)

    def random_name(self, gender: str = "male") -> dict[str, Any]:
        """Get a random Korean given name.

        Args:
            gender: 'male' or 'female'.

        Returns:
            Dict with name information.
        """
        return self._get("/random-name/", gender=gender)

    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()

    def __enter__(self) -> NameFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
