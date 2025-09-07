"""Repository for fetching dad jokes from external API."""

from typing import Optional
import httpx


class DadJokeRepository:
    """Repository for fetching dad jokes from icanhazdadjoke.com API."""

    def __init__(self) -> None:
        """Initialize the dad joke repository."""
        self.base_url = "https://icanhazdadjoke.com"
        self.headers = {
            "Accept": "application/json",
            "User-Agent": "Taters CLI (https://github.com/tristanl-slalom/accelertater)",
        }

    async def get_random_joke(self) -> Optional[str]:
        """
        Fetch a random dad joke from the API.

        Returns:
            The joke text if successful, None if failed.
        """
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    self.base_url, headers=self.headers, timeout=10.0
                )
                response.raise_for_status()
                data = response.json()
                joke = data.get("joke")
                return joke if isinstance(joke, str) else None
        except httpx.RequestError:
            return None
        except httpx.HTTPStatusError:
            return None
        except Exception:
            return None
