import sys
import time
import questionary
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from utils.core import esperar_enter, narrar
from utils.intro import intro_lazarus
from fases.fase01_busca.introducao import introducao_fase1
from fases.fase01_busca.busca_sequencial import DesafioSequencial
from fases.fase01_busca.busca_binaria import DesafioBinario
from fases.fase01_busca.rabin import FaseRabinTempoReal

console = Console()


def animacao_inicio():
    console.clear()
    logo = [
        "██╗      █████╗ ███████╗ █████╗ ██████╗ ██╗   ██╗███████╗",
        "██║     ██╔══██╗╚══███╔╝██╔══██╗██╔══██╗██║   ██║██╔════╝",
        "██║     ███████║  ███╔╝ ███████║██████╔╝██║   ██║███████╗",
        "██║     ██╔══██║ ███╔╝  ██╔══██║██╔══██╗██║   ██║╚════██║",
        "███████╗██║  ██║███████╗██║  ██║██║  ██║╚██████╔╝███████║",
        "╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝"
    ]

    console.print("\n\n")
    for linha in logo:
        console.print(Align.center(Text(linha, style="bold cyan")))
        time.sleep(0.06)

    subtitulo = Text("Sistema Zephyriano de Recuperação de Memória", style="bold yellow")
    console.print(Align.center(subtitulo))
    console.print()
    console.print(Align.center(Text("Inicializando protocolos de acesso neural...", style="dim")))
    time.sleep(1.5)
    console.clear()


def limpar_tela():
    console.clear()

def painel_menu(titulo: str):
    borda = "═" * 36
    texto_titulo = Text(f"╔{borda}╗\n║ {titulo:^34} ║\n╚{borda}╝", style="cyan")
    console.print(Align.center(texto_titulo))
    console.print()

def menu_principal():
    limpar_tela()
    painel_menu("MENU PRINCIPAL - PROJETO LAZARUS")
    console.print(Align.center(Text("Selecione um protocolo para iniciar:", style="dim")))
    console.print()
    escolha = questionary.select(
        "",
        choices=[
            "🚀 Iniciar Jogo Completo",
            "💾 Carregar Fase/Parte",
            "🛑 Encerrar Sistema"
        ],
        qmark="⚡",
        pointer="➤"
    ).ask()
    return escolha

def menu_carregar_fase_parte():
    limpar_tela()
    painel_menu("CARREGAR FASE / PARTE")
    console.print(Align.center(Text("Selecione o ponto de entrada desejado:", style="dim")))
    console.print()
    escolha = questionary.select(
        "",
        choices=[
            "Fase 1 - Busca Sequencial",
            "Fase 1 - Busca Binária",
            "Fase 1 - Rabin-Karp em Tempo Real",
            "⬅ Voltar ao menu principal"
        ],
        qmark="💠",
        pointer="➤"
    ).ask()
    return escolha


def executar_fase1_completa():
    introducao_fase1()
    DesafioSequencial().executar_desafio()
    DesafioBinario().executar_desafio()
    FaseRabinTempoReal().executar()
    narrar("\n[bold green]Parabéns! Você completou a Fase 1 do Projeto Lazarus![/bold green]\n")
    esperar_enter()

def executar_parte_especifica(escolha):
    if escolha == "Fase 1 - Busca Sequencial":
        introducao_fase1()
        DesafioSequencial().executar_desafio()
    elif escolha == "Fase 1 - Busca Binária":
        DesafioBinario().executar_desafio()
    elif escolha == "Fase 1 - Rabin-Karp em Tempo Real":
        FaseRabinTempoReal().executar()


def main():
    animacao_inicio()

    while True:
        opcao = menu_principal()

        if opcao == "🚀 Iniciar Jogo Completo":
            intro_lazarus()
            executar_fase1_completa()

        elif opcao == "💾 Carregar Fase/Parte":
            while True:
                escolha = menu_carregar_fase_parte()
                if escolha == "⬅ Voltar ao menu principal":
                    break
                else:
                    executar_parte_especifica(escolha)
                    narrar("\n[bold cyan]Retornando ao menu de fases...[/bold cyan]\n")
                    esperar_enter()

        elif opcao == "🛑 Encerrar Sistema":
            console.print("\n[bold red]Encerrando o Protocolo Lazarus... Memórias em repouso.[/bold red]")
            time.sleep(1.5)
            sys.exit()

if __name__ == "__main__":
    main()
