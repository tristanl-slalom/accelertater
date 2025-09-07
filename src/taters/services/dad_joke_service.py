"""Service for handling dad joke business logic."""

from typing import Optional

from taters.repositories.dad_joke_repository import DadJokeRepository


class DadJokeService:
    """Service for handling dad joke business logic."""

    def __init__(self, repository: DadJokeRepository) -> None:
        """
        Initialize the dad joke service.

        Args:
            repository: The dad joke repository for data access.
        """
        self.repository = repository

    async def get_joke(self) -> str:
        """
        Get a dad joke, with fallback handling.

        Returns:
            A dad joke string. If the API fails, returns a fallback joke.
        """
        joke = await self.repository.get_random_joke()

        if joke is None:
            return self._get_fallback_joke()

        return joke

    def _get_fallback_joke(self) -> str:
        """
        Get a fallback joke when the API is unavailable.

        Returns:
            A hardcoded fallback dad joke.
        """
        return "Why don't scientists trust atoms? Because they make up everything!"
