from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress
from rich.markdown import Markdown
from news import fetch_api_news
from weather import get_weather
from todo import manage_todo
from quotes import get_quote 
import time

console = Console()

def display_header():
    console.print(Panel.fit("🌟 [bold magenta]SMART PERSONAL DASHBOARD[/bold magenta] 🌟", 
                          subtitle="By [bold green]You[/bold green]",
                          border_style="blue"))

def display_menu():
    menu = Table(title="🔮 [bold]Menu Options[/bold]", show_header=False, padding=(0, 2))
    menu.add_column("Option", style="cyan", no_wrap=True)
    menu.add_column("Description", style="magenta")
    menu.add_row("1", "📰 Latest News")
    menu.add_row("2", "☀️ Weather Update")
    menu.add_row("3", "📝 To-Do List")
    menu.add_row("4", "💬 Random Quote")
    menu.add_row("5", "🚪 Exit")
    console.print(menu)

def loading_animation():
    with Progress() as progress:
        task = progress.add_task("[cyan]Loading...", total=100)
        while not progress.finished:
            progress.update(task, advance=5)
            time.sleep(0.05)

def main():
    while True:
        console.clear()
        display_header()
        display_menu()
        choice = console.input("\n👉 [bold yellow]Choose an option (1-5): [/bold yellow]")

        if choice == "1":
            console.clear()
            console.print(Panel.fit("📰 [bold blue]LATEST NEWS[/bold blue]", border_style="green"))
            fetch_api_news()
        elif choice == "2":
            console.clear()
            city = console.input("\n🌍 [bold]Enter city (default: London): [/bold]") or "London"
            console.print(Panel.fit(f"☀️ [bold blue]WEATHER IN {city.upper()}[/bold blue]", border_style="yellow"))
            get_weather(city)
        elif choice == "3":
            console.clear()
            console.print(Panel.fit("📝 [bold blue]TO-DO LIST MANAGER[/bold blue]", border_style="red"))
            manage_todo()
        elif choice == "4":
            console.clear()
            console.print(Panel.fit("💬 [bold blue]RANDOM QUOTE[/bold blue]", border_style="purple"))
            console.print(get_quote())
        elif choice == "5":
            console.print("\n[bold red]Exiting... Goodbye! 👋[/bold red]")
            break
        else:
            console.print("[red]❌ Invalid choice! Try again.[/red]")
        
        input("\nPress [bold]Enter[/bold] to continue...")
        loading_animation()

if __name__ == "__main__":
    main()