from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from menu import menu
console = Console()
console.print(Panel("[bold magenta]Bem-vindo ao Sistema![/bold magenta]", style="blue"))



if __name__ == "__main__":
    menu()
