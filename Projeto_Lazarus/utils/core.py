# utils/core.py

from rich.console import Console
from rich.progress import track
import time, sys, os

console = Console()

def narrar(texto: str, velocidade: float = 0.02):
    for c in texto:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()

def pausa(segundos: float = 1.0):
    time.sleep(segundos)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def progresso_ritual(descricao: str, passos: int = 5, atraso: float = 0.3):
    console.print(f"\n[cyan]{descricao}[/cyan]")
    for _ in track(range(passos), description="Processando..."):
        time.sleep(atraso)

def esperar_enter(msg: str = "\n [dim][ENTER para continuar][/dim]"):
    console.input(msg)
