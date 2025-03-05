from time import sleep

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from crud import inserir_usuario, listar_usuarios, buscar_usuario, atualizar_usuario, excluir_usuario

console = Console()

def exibir_menu():
    console.print(Panel.fit("[bold cyan]📋 MENU DE OPÇÕES[/bold cyan]", style="blue"))
    menu_opcoes = Table(show_header=False, header_style="bold magenta")
    menu_opcoes.add_column("Opção", justify="center", style="bold yellow")
    menu_opcoes.add_column("Descrição", justify="left", style="bold green")

    menu_opcoes.add_row("1", "Cadastrar Usuário")
    menu_opcoes.add_row("2", "Listar Usuários")
    menu_opcoes.add_row("3", "Buscar Usuário")
    menu_opcoes.add_row("4", "Atualizar Usuário")
    menu_opcoes.add_row("5", "Excluir Usuário")
    menu_opcoes.add_row("6", "[red]Sair[/red]")

    console.print(menu_opcoes)

def menu():
    while True:
        exibir_menu()
        opcao = console.input("[bold cyan]Escolha uma opção: [/bold cyan]")

        if opcao == "1":
            nome = console.input("[bold green]Nome: [/bold green]")
            email = console.input("[bold green]Email: [/bold green]")
            telefone = console.input("[bold green]Telefone: [/bold green]")
            print("Cadastrando informações...")
            sleep(2)
            inserir_usuario(nome, email, telefone)

        elif opcao == "2":
            print("Procurando...")
            sleep(2)
            listar_usuarios()

        elif opcao == "3":
            nome = console.input("[bold yellow]Nome para buscar: [/bold yellow]")
            print("Buscando...")
            sleep(2)
            buscar_usuario(nome)





        elif opcao == "4":
            id = console.input("[bold blue]ID do usuário para atualizar: [/bold blue]")
            nome = console.input("[bold blue]Novo nome: [/bold blue]")
            email = console.input("[bold blue]Novo email: [/bold blue]")
            telefone = console.input("[bold blue]Novo telefone: [/bold blue]")
            print("Atualizando...")
            sleep(2)
            atualizar_usuario(id, nome, email, telefone)

        elif opcao == "5":
            id = console.input("[bold red]ID do usuário para excluir: [/bold red]")
            print("Excluindo...")
            sleep(2)
            excluir_usuario(id)

        elif opcao == "6":
            console.print("[bold red]Saindo do programa...[/bold red]")
            sleep(2)
            break

        else:
            console.print("[bold red]Opção inválida! Tente novamente.[/bold red]")

