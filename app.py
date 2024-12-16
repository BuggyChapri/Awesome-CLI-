from rich.console import Console
from rich.progress import track
from rich.table import Table
import typer
import time

app = typer.Typer()
console = Console()

def main():
    welcome()

def welcome():
    for i in track(range(5), description="Processing..."):
        time.sleep(1)
    console.print("⚡ Welcome to Awesome CLI! ⚡")
    console.print("The tool to make your terminal truly AWESOME!")
    console.print("Let's get started—Hit any key to see the magic!")
    help = input()
    return help

@app.command()
def help():

    console.print("Here’s what you can do:")

    table = Table(title="All General Commands")

    table.add_column("Command", style="cyan", no_wrap=True)
    table.add_column("Description", style="magenta")
    table.add_column("Example", style="green")

    table.add_row("news", "Get the latest news headlines.", "awesome-cli news")
    table.add_row("weather", "Check the weather for any location.", "awesome-cli weather --city=London")
    table.add_row("notes", "Create, view, or manage notes.", "awesome-cli notes add 'Buy milk'")
    table.add_row("tasks", "Manage your to-do list.", "awesome-cli tasks --list")
    table.add_row("translate", "Translate text into another language.", "awesome-cli translate --text='Hello' --to=fr")

    console.print(table)


main()

if __name__ == "__main__":
    app()