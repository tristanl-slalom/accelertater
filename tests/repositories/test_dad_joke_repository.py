"""Tests for the dad joke repository."""

import pytest
from unittest.mock import AsyncMock, Mock, patch
import httpx

from taters.repositories.dad_joke_repository import DadJokeRepository


class TestDadJokeRepository:
    """Test cases for DadJokeRepository."""

    @pytest.fixture
    def repository(self) -> DadJokeRepository:
        """Create a repository instance for testing."""
        return DadJokeRepository()

    @pytest.mark.asyncio
    async def test_get_random_joke_success(self, repository: DadJokeRepository) -> None:
        """Test successful joke retrieval."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "joke": "Why did the chicken cross the road?"
        }
        mock_response.raise_for_status.return_value = None

        mock_client = AsyncMock()
        mock_client.get.return_value = mock_response

        with patch("httpx.AsyncClient") as mock_async_client:
            mock_async_client.return_value.__aenter__.return_value = mock_client

            result = await repository.get_random_joke()

            assert result == "Why did the chicken cross the road?"
            mock_client.get.assert_called_once_with(
                "https://icanhazdadjoke.com",
                headers={
                    "Accept": "application/json",
                    "User-Agent": "Taters CLI (https://github.com/tristanl-slalom/accelertater)",
                },
                timeout=10.0,
            )

    @pytest.mark.asyncio
    async def test_get_random_joke_request_error(
        self, repository: DadJokeRepository
    ) -> None:
        """Test handling of request errors."""
        mock_client = AsyncMock()
        mock_client.get.side_effect = httpx.RequestError("Connection failed")

        with patch("httpx.AsyncClient") as mock_async_client:
            mock_async_client.return_value.__aenter__.return_value = mock_client

            result = await repository.get_random_joke()

            assert result is None

    @pytest.mark.asyncio
    async def test_get_random_joke_http_error(
        self, repository: DadJokeRepository
    ) -> None:
        """Test handling of HTTP status errors."""
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "404 Not Found", request=Mock(), response=Mock()
        )

        mock_client = AsyncMock()
        mock_client.get.return_value = mock_response

        with patch("httpx.AsyncClient") as mock_async_client:
            mock_async_client.return_value.__aenter__.return_value = mock_client

            result = await repository.get_random_joke()

            assert result is None

    @pytest.mark.asyncio
    async def test_get_random_joke_json_missing_joke(
        self, repository: DadJokeRepository
    ) -> None:
        """Test handling when response JSON doesn't contain joke."""
        mock_response = Mock()
        mock_response.json.return_value = {"id": "123", "status": 200}
        mock_response.raise_for_status.return_value = None

        mock_client = AsyncMock()
        mock_client.get.return_value = mock_response

        with patch("httpx.AsyncClient") as mock_async_client:
            mock_async_client.return_value.__aenter__.return_value = mock_client

            result = await repository.get_random_joke()

            assert result is None

    @pytest.mark.asyncio
    async def test_get_random_joke_unexpected_error(
        self, repository: DadJokeRepository
    ) -> None:
        """Test handling of unexpected errors."""
        mock_client = AsyncMock()
        mock_client.get.side_effect = Exception("Unexpected error")

        with patch("httpx.AsyncClient") as mock_async_client:
            mock_async_client.return_value.__aenter__.return_value = mock_client

            result = await repository.get_random_joke()

            assert result is None
