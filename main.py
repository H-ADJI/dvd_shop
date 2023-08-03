import time
from enum import Enum

import typer
from rich import print
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt


class Commands(str, Enum):
    ADD = "add"
    CLEAR = "clear"
    PRICE = "price"
    QUIT = "quit"
    HELP = "help"
    LIST = "list"


def help():
    print(
        "To [bold]add[/bold] a movie to your cart use the [bold green]add[/bold green] command"
    )
    print(
        "To [bold]empty your cart[/bold] use the [bold green]clear[/bold green] command"
    )
    print(
        "To show the [bold]price[/bold] use the [bold green]price[/bold green] command"
    )
    print("To abort the process use the [bold green]quit[/bold green] command")

    print(
        "To show the [bold]help menu[/bold] use the [bold green]help[/bold green] command"
    )


def startup():
    print("[bold]Welcome to our movies shop[/bold]")
    print("[bold green]Creating a Cart for you[/bold green]")
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        SpinnerColumn(),
        # transient=True,
    ) as progress:
        progress.add_task(description="Preparing...", total=None)
        time.sleep(1)
    print("[bold green]Cart created ! [/bold green]")


def main():
    startup()
    help()

    cmd = Prompt.ask("Command => ")
    if cmd == Commands.ADD:
        pass
    elif cmd == Commands.QUIT:
        pass
    elif cmd == Commands.CLEAR:
        pass
    elif cmd == Commands.PRICE:
        pass
    elif cmd == Commands.HELP:
        pass
    elif cmd == Commands.LIST:
        pass


if __name__ == "__main__":
    typer.run(main)
