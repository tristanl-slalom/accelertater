"""Main CLI application for Taters."""

import asyncio
from typing import Optional

import typer

from taters.container import Container


app = typer.Typer(help="🥔 Taters - A Python CLI accelerator")


@app.command("hello")
def hello(name: Optional[str] = typer.Argument(None, help="Name to greet")) -> None:
    """Say hello to someone."""
    container = Container()
    action = container.hello_action()
    greeting = action.execute(name)
    typer.echo(greeting)


@app.command("dad-joke")
def dad_joke() -> None:
    """Get a random dad joke from the internet."""

    async def _async_dad_joke() -> None:
        container = Container()
        action = container.dad_joke_action()
        try:
            joke = await action.execute()
            typer.echo(joke)
        except Exception as e:
            typer.echo(f"❌ Error getting dad joke: {e}", err=True)
            raise typer.Exit(1)

    asyncio.run(_async_dad_joke())


def main() -> None:
    """Main entry point for the CLI application."""
    app()


if __name__ == "__main__":
    main()
