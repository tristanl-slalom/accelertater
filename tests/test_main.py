"""Tests for the main CLI module."""

import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from typer.testing import CliRunner

from taters.main import app


class TestMainCLI:
    """Test cases for main CLI application."""

    @pytest.fixture
    def runner(self) -> CliRunner:
        """Create a CLI test runner."""
        return CliRunner()

    def test_hello_command_without_name(self, runner: CliRunner) -> None:
        """Test hello command without providing a name."""
        with patch("taters.main.Container") as mock_container:
            mock_action = MagicMock()
            mock_action.execute.return_value = "👋 Hello there!"
            mock_container.return_value.hello_action.return_value = mock_action

            result = runner.invoke(app, ["hello"])

            assert result.exit_code == 0
            assert "👋 Hello there!" in result.stdout
            mock_action.execute.assert_called_once_with(None)

    def test_hello_command_with_name(self, runner: CliRunner) -> None:
        """Test hello command with a provided name."""
        with patch("taters.main.Container") as mock_container:
            mock_action = MagicMock()
            mock_action.execute.return_value = "👋 Hello, Alice!"
            mock_container.return_value.hello_action.return_value = mock_action

            result = runner.invoke(app, ["hello", "Alice"])

            assert result.exit_code == 0
            assert "👋 Hello, Alice!" in result.stdout
            mock_action.execute.assert_called_once_with("Alice")

    def test_dad_joke_command_success(self, runner: CliRunner) -> None:
        """Test successful dad joke command."""
        with patch("taters.main.Container") as mock_container:
            mock_action = AsyncMock()
            mock_action.execute.return_value = (
                "🃏 Dad Joke: Why don't scientists trust atoms?"
            )
            mock_container.return_value.dad_joke_action.return_value = mock_action

            result = runner.invoke(app, ["dad-joke"])

            assert result.exit_code == 0
            assert "🃏 Dad Joke:" in result.stdout

    def test_dad_joke_command_failure(self, runner: CliRunner) -> None:
        """Test dad joke command when an exception occurs."""
        with patch("taters.main.Container") as mock_container:
            mock_action = AsyncMock()
            mock_action.execute.side_effect = Exception("API Error")
            mock_container.return_value.dad_joke_action.return_value = mock_action

            result = runner.invoke(app, ["dad-joke"])

            assert result.exit_code == 1
            # Error messages go to stderr when using typer.echo(err=True)
            assert (
                "❌ Error getting dad joke: API Error" in result.stderr
                or "❌ Error getting dad joke: API Error" in result.stdout
            )

    def test_app_help(self, runner: CliRunner) -> None:
        """Test CLI help output."""
        result = runner.invoke(app, ["--help"])

        assert result.exit_code == 0
        assert "🥔 Taters - A Python CLI accelerator" in result.stdout
        assert "hello" in result.stdout
        assert "dad-joke" in result.stdout

    def test_hello_command_help(self, runner: CliRunner) -> None:
        """Test hello command help."""
        result = runner.invoke(app, ["hello", "--help"])

        assert result.exit_code == 0
        assert "Say hello to someone" in result.stdout

    def test_dad_joke_command_help(self, runner: CliRunner) -> None:
        """Test dad joke command help."""
        result = runner.invoke(app, ["dad-joke", "--help"])

        assert result.exit_code == 0
        assert "Get a random dad joke from the internet" in result.stdout
