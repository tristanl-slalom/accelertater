"""Tests for HelloAction."""

import pytest

from taters.actions.hello_action import HelloAction


@pytest.fixture
def action() -> HelloAction:
    """Create a HelloAction instance for testing."""
    return HelloAction()


class TestHelloAction:
    """Test cases for HelloAction."""

    def test_execute_with_name(self, action: HelloAction) -> None:
        """Test execute with a provided name."""
        result = action.execute("Alice")

        assert result == "👋 Hello, Alice!"

    def test_execute_without_name(self, action: HelloAction) -> None:
        """Test execute without a name (None)."""
        result = action.execute(None)

        assert result == "👋 Hello there!"

    def test_execute_with_empty_string(self, action: HelloAction) -> None:
        """Test execute with an empty string."""
        result = action.execute("")

        # Empty string is falsy, so it should use the generic greeting
        assert result == "👋 Hello there!"
