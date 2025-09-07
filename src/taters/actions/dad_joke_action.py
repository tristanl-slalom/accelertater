"""Action for handling dad joke command workflow."""

from taters.services.dad_joke_service import DadJokeService


class DadJokeAction:
    """Action for orchestrating dad joke command workflow."""

    def __init__(self, service: DadJokeService) -> None:
        """
        Initialize the dad joke action.

        Args:
            service: The dad joke service for business logic.
        """
        self.service = service

    async def execute(self) -> str:
        """
        Execute the dad joke action.

        Returns:
            A formatted dad joke ready for CLI output.
        """
        joke = await self.service.get_joke()
        return f"🃏 Dad Joke: {joke}"
