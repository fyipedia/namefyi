"""HTTP API client for namefyi.com REST endpoints.

Requires the ``api`` extra: ``pip install namefyi[api]``

Usage::

    from namefyi.api import NameFYI

    with NameFYI() as api:
        items = api.list_characters()
        detail = api.get_character("example-slug")
        results = api.search("query")
"""

from __future__ import annotations

from typing import Any

import httpx


class NameFYI:
    """API client for the namefyi.com REST API.

    Provides typed access to all namefyi.com endpoints including
    list, detail, and search operations.

    Args:
        base_url: API base URL. Defaults to ``https://namefyi.com``.
        timeout: Request timeout in seconds. Defaults to ``10.0``.
    """

    def __init__(
        self,
        base_url: str = "https://namefyi.com",
        timeout: float = 10.0,
    ) -> None:
        self._client = httpx.Client(base_url=base_url, timeout=timeout)

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        resp = self._client.get(
            path,
            params={k: v for k, v in params.items() if v is not None},
        )
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    # -- Endpoints -----------------------------------------------------------

    def list_characters(self, **params: Any) -> dict[str, Any]:
        """List all characters."""
        return self._get("/api/v1/characters/", **params)

    def get_character(self, slug: str) -> dict[str, Any]:
        """Get character by slug."""
        return self._get(f"/api/v1/characters/" + slug + "/")

    def list_cultures(self, **params: Any) -> dict[str, Any]:
        """List all cultures."""
        return self._get("/api/v1/cultures/", **params)

    def get_culture(self, slug: str) -> dict[str, Any]:
        """Get culture by slug."""
        return self._get(f"/api/v1/cultures/" + slug + "/")

    def list_faqs(self, **params: Any) -> dict[str, Any]:
        """List all faqs."""
        return self._get("/api/v1/faqs/", **params)

    def get_faq(self, slug: str) -> dict[str, Any]:
        """Get faq by slug."""
        return self._get(f"/api/v1/faqs/" + slug + "/")

    def list_given_names(self, **params: Any) -> dict[str, Any]:
        """List all given names."""
        return self._get("/api/v1/given-names/", **params)

    def get_given_name(self, slug: str) -> dict[str, Any]:
        """Get given name by slug."""
        return self._get(f"/api/v1/given-names/" + slug + "/")

    def list_glossary(self, **params: Any) -> dict[str, Any]:
        """List all glossary."""
        return self._get("/api/v1/glossary/", **params)

    def get_term(self, slug: str) -> dict[str, Any]:
        """Get term by slug."""
        return self._get(f"/api/v1/glossary/" + slug + "/")

    def list_guides(self, **params: Any) -> dict[str, Any]:
        """List all guides."""
        return self._get("/api/v1/guides/", **params)

    def get_guide(self, slug: str) -> dict[str, Any]:
        """Get guide by slug."""
        return self._get(f"/api/v1/guides/" + slug + "/")

    def list_meaning_tags(self, **params: Any) -> dict[str, Any]:
        """List all meaning tags."""
        return self._get("/api/v1/meaning-tags/", **params)

    def get_meaning_tag(self, slug: str) -> dict[str, Any]:
        """Get meaning tag by slug."""
        return self._get(f"/api/v1/meaning-tags/" + slug + "/")

    def list_surnames(self, **params: Any) -> dict[str, Any]:
        """List all surnames."""
        return self._get("/api/v1/surnames/", **params)

    def get_surname(self, slug: str) -> dict[str, Any]:
        """Get surname by slug."""
        return self._get(f"/api/v1/surnames/" + slug + "/")

    def search(self, query: str, **params: Any) -> dict[str, Any]:
        """Search across all content."""
        return self._get(f"/api/v1/search/", q=query, **params)

    # -- Lifecycle -----------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> NameFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
