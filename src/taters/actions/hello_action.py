"""Action for handling hello command workflow."""

from typing import Optional


class HelloAction:
    """Action for orchestrating hello command workflow."""

    def __init__(self) -> None:
        """Initialize the hello action."""
        pass

    def execute(self, name: Optional[str] = None) -> str:
        """
        Execute the hello action.

        Args:
            name: Optional name to greet. If None, uses a generic greeting.

        Returns:
            A formatted greeting message ready for CLI output.
        """
        if name:
            return f"👋 Hello, {name}!"
        else:
            return "👋 Hello there!"
