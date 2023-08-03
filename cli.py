import time
from enum import Enum

from rich import print
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt
from rich.table import Table

from shop import BackToTheFutureStrategy, Cart


class Commands(str, Enum):
    ADD = "add"
    CLEAR = "clear"
    PRICE = "price"
    QUIT = "quit"
    HELP = "help"
    LIST = "list"


def help():
    print("To [bold]add[/bold] a movie to your cart use the [bold green]add[/bold green] command")
    print("To [bold]empty your cart[/bold] use the [bold green]clear[/bold green] command")
    print("To show the [bold]price[/bold] use the [bold green]price[/bold green] command")

    print("To list the products in your cart use the [bold green]list[/bold green] command")

    print("To abort the process use the [bold green]quit[/bold green] command")

    print("To show the [bold]help menu[/bold] use the [bold green]help[/bold green] command")


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


def cli_entry_point():
    startup()
    help()
    cart = Cart()
    strategy = BackToTheFutureStrategy()
    cmd = Prompt.ask("Command => ")
    while True:
        if cmd == Commands.ADD:
            while True:
                movie = Prompt.ask("add a movie to your cart, press enter at the end")
                if not movie:
                    break
                cart.add_dvd(dvd_name=movie)

        elif cmd == Commands.CLEAR:
            cart.empty_cart()
            print("Your cart is now empty")
        elif cmd == Commands.PRICE:
            print(f"The total price of your cart is : {cart.price(strategy=strategy)}")
        elif cmd == Commands.HELP:
            help()
        elif cmd == Commands.LIST:
            table = Table("Title", show_lines=True)
            [table.add_row(movie) for movie in cart.products]
            print(table)
        elif cmd == Commands.QUIT:
            break
        else:
            print(
                "[bold red]Unsupported command[/bold red] use [bold green]help[/bold green] to know available commands"
            )
        cmd = Prompt.ask("Command => ")
