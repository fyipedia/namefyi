"""Tests for the namefyi API client."""

from namefyi.api import NameFYI


def test_client_init() -> None:
    """Client initializes with default URL."""
    client = NameFYI()
    assert str(client._client.base_url).rstrip("/") == "https://namefyi.com/api"
    client.close()


def test_client_custom_url() -> None:
    """Client accepts custom base URL."""
    client = NameFYI(base_url="https://custom.example.com/api")
    assert str(client._client.base_url).rstrip("/") == "https://custom.example.com/api"
    client.close()


def test_client_context_manager() -> None:
    """Client works as context manager."""
    with NameFYI() as client:
        assert client._client is not None
