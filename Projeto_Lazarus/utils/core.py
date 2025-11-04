# utils/core.py
# ==========================================
# Núcleo utilitário — Sistema Lazarus
# Adiciona narração, pausas, progresso e
# formatação colorida das falas dos personagens.
# ==========================================

from rich.console import Console
from rich.progress import track
import time, sys, os

console = Console()


CORES_PERSONAGENS = {
    "Kaelen": "bold blue",
    "Elara": "bold magenta",
    "Roric": "bold yellow",
    "Lin": "bold cyan",
    "Núcleo": "bold bright_magenta"
}

def narrar(texto: str, velocidade: float = 0.02):
    """
    Exibe o texto de forma narrativa, simulando digitação.
    """
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
    """
    Exibe uma barra de progresso com descrição .
    """
    console.print(f"\n[cyan]{descricao}[/cyan]")
    for _ in track(range(passos), description="Processando..."):
        time.sleep(atraso)

def esperar_enter(msg: str = "\n [dim][ENTER para continuar][/dim]"):
    console.input(msg)


def fala(personagem: str, texto: str, velocidade: float = 0.03):
    """
    Exibe a fala de um personagem com cor, estilo padronizado
    E ANIMAÇÃO de digitação.
    """
    cor = CORES_PERSONAGENS.get(personagem, "white")
    
    # --- [MUDANÇA AQUI] ---
    # 1. Imprime o prefixo formatado (ex: "[bold blue]Kaelen: [/]")
    #    O 'end=""' impede a quebra de linha.
    console.print(f"[{cor}]{personagem}:[/] ", end="")
    
    # 2. Reutiliza a lógica de 'narrar' para animar o texto
    for c in texto:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(velocidade)
    print() # Adiciona a quebra de linha no final
    # --- [FIM DA MUDANÇA] ---

    pausa(0.3)

def nucleo(texto: str, velocidade: float = 0.03):
    """
    Fala especial do Núcleo Ressonante, COM ANIMAÇÃO.
    """
    # --- [MUDANÇA AQUI] ---
    # 1. Imprime o prefixo formatado
    console.print(f"[bold bright_magenta]💫 Núcleo Ressonante:[/] ", end="")

    # 2. Anima o texto
    for c in texto:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(velocidade)
    print() # Adiciona a quebra de linha no final
    # --- [FIM DA MUDANÇA] ---
    
    pausa(0.3)

def pensar(texto: str, velocidade: float = 0.03):
    """
    Exibe pensamentos ou reflexões internas em itálico e cinza.
    """
    console.print(f"[italic dim white]{texto}[/italic dim white]")
    pausa(0.4)

# ============================================================
# FUNÇÃO DE TESTE RÁPIDO (opcional)
# ============================================================

if __name__ == "__main__":
    limpar_tela()
    narrar("🔧 Teste de narrativa do Sistema Lazarus...")
    fala("Kaelen", "A ordem deve prevalecer.")
    fala("Elara", "Os padrões retornam, mas em nova forma.")
    fala("Roric", "O cálculo é exato, mas a mente... não.")
    fala("Lin", "A harmonia surge da iteração.")
    nucleo("Ressonância detectada... padrão 4_7 estável.")
    pensar("Talvez o código seja mais do que um número.")
    progresso_ritual("Sincronizando camadas cognitivas", 5, 0.15)
    esperar_enter()
