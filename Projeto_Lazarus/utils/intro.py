# utils/intro.py

from rich.console import Console
from rich.panel import Panel
from utils.core import narrar, pausa, progresso_ritual, limpar_tela, esperar_enter
from time import sleep

console = Console()

def intro_lazarus():
    limpar_tela()
    logo = [
        "██╗      █████╗ ███████╗ █████╗ ██████╗ ██╗   ██╗███████╗",
        "██║     ██╔══██╗╚══███╔╝██╔══██╗██╔══██╗██║   ██║██╔════╝",
        "██║     ███████║  ███╔╝ ███████║██████╔╝██║   ██║███████╗",
        "██║     ██╔══██║ ███╔╝  ██╔══██║██╔══██╗██║   ██║╚════██║",
        "███████╗██║  ██║███████╗██║  ██║██║  ██║╚██████╔╝███████║",
        "╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝"
    ]
    for linha in logo:
        console.print(f"[bright_cyan]{linha}[/bright_cyan]")
        sleep(0.1)
    pausa(1)

    narrar("\nAtivando protocolo LAZARUS...", 0.025)
    progresso_ritual("Verificando integridade dos bancos de memória...", 6, 0.25)
    pausa(1)
    limpar_tela()

    console.print(Panel.fit(
        "[bold cyan]Expedição Lazarus — Frota Kepler-9[/bold cyan]\n[dim]Ano 2247 | Sistema de Aetherios[/dim]",
        border_style="bright_cyan"
    ))
    narrar("Dr. Kaelen Aris (log de voz): “Captamos ecos digitais vindos de Aetherios. Uma biblioteca viva, adormecida sob poeira cósmica.”", 0.025)
    narrar("“Hoje, ativamos o protocolo Lazarus. Que os ecos despertem...”", 0.025)
    progresso_ritual("Sincronizando com núcleo de decodificação Zephyriano...", 5, 0.25)
    esperar_enter()







"""""
from rich.console import Console
from rich.panel import Panel
from utils.core import narrar, pausa, limpar_tela, progresso_ritual, esperar_enter
from time import sleep

console = Console()


def intro_lazarus():
    limpar_tela()
    
    ascii_logo = [
        "██╗      █████╗ ███████╗ █████╗ ██████╗ ██╗   ██╗███████╗",
        "██║     ██╔══██╗╚══███╔╝██╔══██╗██╔══██╗██║   ██║██╔════╝",
        "██║     ███████║  ███╔╝ ███████║██████╔╝██║   ██║███████╗",
        "██║     ██╔══██║ ███╔╝  ██╔══██║██╔══██╗██║   ██║╚════██║",
        "███████╗██║  ██║███████╗██║  ██║██║  ██║╚██████╔╝███████║",
        "╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝"
    ]

    console.print("\n", style="bold cyan")
    for linha in ascii_logo:
        console.print(f"[cyan]{linha}[/cyan]")
        sleep(0.1)
    console.print("[dim]Versão 1.0 — Projeto Aetherianos[/dim]\n")
    pausa(1.5)

    narrar(">>> PROTOCOLO DE REANIMAÇÃO DE DADOS ATIVADO <<<", 0.02)
    narrar("Iniciando sequência Lazarus.", 0.025)
    progresso_ritual("Verificando integridade dos bancos de memória...", passos=6, atraso=0.3)
    pausa(1)

    limpar_tela()
    console.print(Panel.fit(
        "[bold cyan]Expedição Lazarus — Frota Kepler-9[/bold cyan]\n"
        "[dim]Ano 2247 | Sistema de Aetherios[/dim]",
        border_style="bright_cyan"
    ))

    narrar("Dr. Kaelen Aris (log de voz):", 0.03)
    narrar("“Há dias captamos ecos digitais vindos de Aetherios. "
           "Parece uma biblioteca viva, adormecida sob camadas de poeira cósmica.”", 0.025)
    pausa(1.2)

    narrar("“Hoje, a Frota Kepler nos autorizou a ativar o Protocolo Lazarus. "
           "Vamos tentar reanimar o que restou dessa civilização esquecida.”", 0.025)

    progresso_ritual("Sincronizando com núcleo de decodificação Zephyriano...", passos=5, atraso=0.25)
    pausa(1)
    limpar_tela()

    console.print(Panel(
        "[bold green]SISTEMA LAZARUS PRONTO[/bold green]\n"
        "[dim]Pressione ENTER para iniciar a Fase 1: Os Fragmentos Iniciais[/dim]",
        border_style="green"
    ))
    esperar_enter()
"""""