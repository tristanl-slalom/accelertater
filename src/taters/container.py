"""Dependency injection container for the Taters CLI application."""

from dependency_injector import containers, providers

from taters.repositories.dad_joke_repository import DadJokeRepository
from taters.services.dad_joke_service import DadJokeService
from taters.actions.dad_joke_action import DadJokeAction
from taters.actions.hello_action import HelloAction


class Container(containers.DeclarativeContainer):
    """Dependency injection container."""

    # Configuration
    config = providers.Configuration()

    # Repositories (lowest layer)
    dad_joke_repository = providers.Factory(DadJokeRepository)

    # Services (middle layer)
    dad_joke_service = providers.Factory(DadJokeService, repository=dad_joke_repository)

    # Actions (top layer)
    hello_action = providers.Factory(HelloAction)

    dad_joke_action = providers.Factory(DadJokeAction, service=dad_joke_service)
