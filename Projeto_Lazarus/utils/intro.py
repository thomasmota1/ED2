from rich.console import Console
from rich.panel import Panel
from utils.core import narrar, pausa, progresso_ritual, limpar_tela, esperar_enter, fala, pensar
from time import sleep
from fases.fase01_busca.busca_sequencial import DesafioSequencial

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

    fala("Kaelen", "Captamos ecos digitais vindos de Aetherios. Uma biblioteca viva, adormecida sob poeira cósmica.")
    fala("Kaelen", "Hoje, ativamos o protocolo Lazarus. Que os ecos despertem...")
    pausa(1)

    narrar("\n[Transmissão de Sistema — Núcleo Zephyriano]", 0.03)
    narrar("‘A humanidade esqueceu as linguagens que a criaram. Vozes antigas aguardam o guardião que ousar decifrá-las.’", 0.03)
    narrar("‘Somente aquele que compreender a ordem dentro do caos poderá restaurar a harmonia perdida.’", 0.03)
    pausa(1)

    console.print("\n[bold yellow]>>> Sequência de inicialização autorizada <<<[/bold yellow]")
    progresso_ritual("Sincronizando com Núcleo de Decodificação Zephyriano...", 5, 0.25)

    fala("Elara", "O despertar começou... Cada bit pulsante é uma lembrança de eras esquecidas.")
    fala("Roric", "Preparem-se. Se o Lazarus for bem-sucedido, traremos de volta o que o tempo tentou apagar.")
    fala("Lin", "Ou libertaremos algo que nunca deveria ter sido reanimado...")
    pausa(1)

    console.print(Panel.fit(
        "[bold bright_cyan]PROTOCOLO LAZARUS — ONLINE[/bold bright_cyan]\n[dim]Iniciando reconstrução cognitiva dos Fragmentos Perdidos...[/dim]",
        border_style="bright_cyan"
    ))
    pausa(1.2)

    narrar("\n[Sistema]: ‘Carregando setorização da Cripta de Dados...’", 0.03)
    narrar("[Sistema]: ‘Fragmentos corrompidos detectados. Iniciando varredura manual assistida.’", 0.03)
    pausa(1)