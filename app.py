import typer
from welcome import welcome
from rich.console import Console

app = typer.Typer()
console = Console()

welcome() 

