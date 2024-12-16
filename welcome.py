import sys
from rich.console import Console
from rich.table import Table
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

console = Console()

def welcome():
    init(strip=not sys.stdout.isatty())

    ascii_art = figlet_format('Awesome CLI', font='isometric1')
    console.print(f"[bold green]{ascii_art}[/bold green]", justify="center")

    console.print("[bold green]One 'CLI' to rule them all! :boom:[/bold green]", justify="center")

    table = Table(title="Awesome CLI Categories", show_lines=True)

    table.add_column("Category", style="cyan bold", no_wrap=True, justify="center")
    table.add_column("Commands", style="cyan bold", no_wrap=True, justify="center")
    table.add_column("Description", style="magenta bold", justify="center")

    table.add_row(
        "Entertainment",
        "entertainment-cli",
        "Apps for enjoying movies, music, and games"
    )
    table.add_row(
        "Music",
        "music-cli",
        "Manage playlists, find lyrics, or stream music"
    )
    table.add_row(
        "Social Media",
        "socialmedia-cli",
        "Tools for managing and accessing social platforms"
    )
    table.add_row(
        "Video",
        "video-cli",
        "Video downloaders, converters, or players"
    )
    table.add_row(
        "Movies",
        "movies-cli",
        "Find movie information and watch trailers"
    )
    table.add_row(
        "Games",
        "games-cli",
        "Fun and interactive CLI-based games"
    )
    table.add_row(
        "Books",
        "books-cli",
        "Search and manage book collections"
    )
    table.add_row(
        "Text Editors",
        "nano | vim | emacs",
        "CLI-based text editing tools"
    )
    table.add_row(
        "Frontend Development",
        "webpack-cli",
        "Tools for web development workflows"
    )
    table.add_row(
        "Mobile Development",
        "flutter-cli",
        "Utilities for building mobile apps"
    )
    table.add_row(
        "Database",
        "sql-cli",
        "Interact with and manage databases"
    )
    table.add_row(
        "DevOps",
        "devops-cli",
        "Deployment and server management tools"
    )
    table.add_row(
        "Docker",
        "docker-compose",
        "Container management and image building"
    )
    table.add_row(
        "Release",
        "release-cli",
        "Tools for versioning and deploying applications"
    )
    table.add_row(
        "Productivity",
        "todo-cli",
        "Boost your efficiency with timers, calendars, etc."
    )
    table.add_row(
        "Weather",
        "weather-cli",
        "Check current weather conditions"
    )
    table.add_row(
        "Security",
        "encryptor-cli",
        "Encrypt, decrypt, and manage credentials"
    )
    table.add_row(
        "System Interaction",
        "htop | ps",
        "Monitor and control system resources"
    )
    table.add_row(
        "Internet Speedtest",
        "speedtest-cli",
        "Check your internet speed from the CLI"
    )

   
    console.print(table, justify = "center")

welcome()
