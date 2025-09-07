"""Tests for the dad joke service."""

import pytest
from unittest.mock import AsyncMock

from taters.services.dad_joke_service import DadJokeService
from taters.repositories.dad_joke_repository import DadJokeRepository


class TestDadJokeService:
    """Test cases for DadJokeService."""

    @pytest.fixture
    def mock_repository(self) -> DadJokeRepository:
        """Create a mock repository for testing."""
        return AsyncMock(spec=DadJokeRepository)

    @pytest.fixture
    def service(self, mock_repository: DadJokeRepository) -> DadJokeService:
        """Create a service instance with mock repository."""
        return DadJokeService(mock_repository)

    @pytest.mark.asyncio
    async def test_get_joke_success(
        self, service: DadJokeService, mock_repository: DadJokeRepository
    ) -> None:
        """Test successful joke retrieval."""
        expected_joke = "Why don't eggs tell jokes? They'd crack each other up!"
        mock_repository.get_random_joke.return_value = expected_joke

        result = await service.get_joke()

        assert result == expected_joke
        mock_repository.get_random_joke.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_joke_api_failure_returns_fallback(
        self, service: DadJokeService, mock_repository: DadJokeRepository
    ) -> None:
        """Test fallback joke when API fails."""
        mock_repository.get_random_joke.return_value = None

        result = await service.get_joke()

        assert (
            result
            == "Why don't scientists trust atoms? Because they make up everything!"
        )
        mock_repository.get_random_joke.assert_called_once()

    def test_fallback_joke(self, service: DadJokeService) -> None:
        """Test the fallback joke method directly."""
        result = service._get_fallback_joke()

        assert (
            result
            == "Why don't scientists trust atoms? Because they make up everything!"
        )
        assert isinstance(result, str)
        assert len(result) > 0
