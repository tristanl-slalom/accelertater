"""Tests for the Container dependency injection configuration."""

import pytest

from taters.container import Container
from taters.repositories.dad_joke_repository import DadJokeRepository
from taters.services.dad_joke_service import DadJokeService
from taters.actions.dad_joke_action import DadJokeAction
from taters.actions.hello_action import HelloAction


class TestContainer:
    """Test cases for Container dependency injection."""

    @pytest.fixture
    def container(self) -> Container:
        """Create a Container instance for testing."""
        return Container()

    def test_dad_joke_repository_creation(self, container: Container) -> None:
        """Test that DadJokeRepository can be created."""
        repository = container.dad_joke_repository()

        assert isinstance(repository, DadJokeRepository)

    def test_dad_joke_service_creation(self, container: Container) -> None:
        """Test that DadJokeService can be created with repository dependency."""
        service = container.dad_joke_service()

        assert isinstance(service, DadJokeService)
        assert isinstance(service.repository, DadJokeRepository)

    def test_dad_joke_action_creation(self, container: Container) -> None:
        """Test that DadJokeAction can be created with service dependency."""
        action = container.dad_joke_action()

        assert isinstance(action, DadJokeAction)
        assert isinstance(action.service, DadJokeService)
        assert isinstance(action.service.repository, DadJokeRepository)

    def test_hello_action_creation(self, container: Container) -> None:
        """Test that HelloAction can be created."""
        action = container.hello_action()

        assert isinstance(action, HelloAction)

    def test_dependency_injection_chain(self, container: Container) -> None:
        """Test that the full dependency chain is properly wired."""
        # Create the action which should have all dependencies injected
        action = container.dad_joke_action()

        # Verify the full chain
        assert hasattr(action, "service")
        assert hasattr(action.service, "repository")

        # Verify types
        assert isinstance(action, DadJokeAction)
        assert isinstance(action.service, DadJokeService)
        assert isinstance(action.service.repository, DadJokeRepository)
