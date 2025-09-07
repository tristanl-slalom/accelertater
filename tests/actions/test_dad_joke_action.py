"""Tests for the dad joke action."""

import pytest
from unittest.mock import AsyncMock

from taters.actions.dad_joke_action import DadJokeAction
from taters.services.dad_joke_service import DadJokeService


class TestDadJokeAction:
    """Test cases for DadJokeAction."""

    @pytest.fixture
    def mock_service(self) -> DadJokeService:
        """Create a mock service for testing."""
        return AsyncMock(spec=DadJokeService)

    @pytest.fixture
    def action(self, mock_service: DadJokeService) -> DadJokeAction:
        """Create an action instance with mock service."""
        return DadJokeAction(mock_service)

    @pytest.mark.asyncio
    async def test_execute_success(
        self, action: DadJokeAction, mock_service: DadJokeService
    ) -> None:
        """Test successful action execution."""
        expected_joke = "What do you call a fish wearing a crown? A king fish!"
        mock_service.get_joke.return_value = expected_joke

        result = await action.execute()

        assert result == f"🃏 Dad Joke: {expected_joke}"
        mock_service.get_joke.assert_called_once()

    @pytest.mark.asyncio
    async def test_execute_formats_output_correctly(
        self, action: DadJokeAction, mock_service: DadJokeService
    ) -> None:
        """Test that the action formats output with emoji prefix."""
        joke = "Simple joke"
        mock_service.get_joke.return_value = joke

        result = await action.execute()

        assert result.startswith("🃏 Dad Joke: ")
        assert joke in result
