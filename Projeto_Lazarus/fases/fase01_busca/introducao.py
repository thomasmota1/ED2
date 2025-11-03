# fases/fase1_intro.py

from rich.console import Console
from fases.fase01_busca.busca_sequencial import desafio_sequencial
from utils.core import esperar_enter, limpar_tela, narrar, pausa, progresso_ritual

console = Console()

def introducao_fase1():
    limpar_tela()
    narrar("...SILÊNCIO...")
    pausa(1)
    console.print("[bold white on red]--- ALERTA: INTEGRIDADE COMPROMETIDA ---[/bold white on red]")
    progresso_ritual("Fragmentos de conhecimento perdidos...", 5, 0.25)
    narrar("Aris: 'Guardião, precisamos agir! A entropia está devorando a biblioteca!'")
    esperar_enter()
    desafio_sequencial()
