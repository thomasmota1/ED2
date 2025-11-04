
from rich.console import Console
from fases.fase01_busca.busca_sequencial import DesafioSequencial, desafio_sequencial
from utils.core import esperar_enter, fala, limpar_tela, narrar, pausa, pensar, progresso_ritual
from rich.panel import Panel


console = Console()

def introducao_fase1():
    limpar_tela()
    narrar("...SILÊNCIO...")
    pausa(1)

    console.print("[bold white on red]--- ALERTA: INTEGRIDADE COMPROMETIDA ---[/bold white on red]")
    progresso_ritual("Fragmentos de conhecimento perdidos...", 5, 0.25)
    fala("Kaelen", "Precisamos agir! A entropia está devorando a biblioteca!")
    fala("Elara", "Os dados estão se desfazendo... linhas inteiras de código se corrompendo em tempo real!")
    fala("Roric", "Sem estrutura, só há uma opção: procurar manualmente, uma entrada por vez.")
    fala("Lin", "A Busca Sequencial... a mais primitiva das técnicas, mas talvez a única que reste.")
    pensar("O silêncio digital ecoa — o nascimento de uma era de redescoberta e ruído.")
    pausa(0.5)

    console.print(Panel.fit(
        "[bold yellow]🌐 Fase 1 — Ecos da Ressonância[/bold yellow]\n[dim]Iniciando protocolo de varredura sequencial...[/dim]",
        border_style="yellow"
    ))
    esperar_enter()