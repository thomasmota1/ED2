# fases/fase1_impl.py
''''''''''
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
import questionary, time

from fases.buscas import BuscaSequencial, BuscaBinaria, BuscaRabinKarp
from utils.core import narrar, pausa, progresso_ritual, limpar_tela, esperar_enter

console = Console()

def fase1_buscas():
    limpar_tela()
    console.print(Panel.fit(
        "[bold cyan]FASE 1 — OS FRAGMENTOS INICIAIS[/bold cyan]\n"
        "[dim]Expedição Lazarus | Frota Kepler-9 | Ano 2247[/dim]",
        border_style="bright_cyan"
    ))

    pausa(1)
    narrar("Sistema: [AETHERLINK ONLINE].", 0.015)
    narrar("Localizando arquivos de origem Zephyriana...", 0.02)
    progresso_ritual("Conectando ao banco de dados Aetheriano...", passos=7, atraso=0.25)
    limpar_tela()

    # =========================================================
    # ETAPA 1 – BUSCA SEQUENCIAL
    # =========================================================
    console.print(Panel("[yellow]Etapa 1: Varredura Sequencial[/yellow]", border_style="yellow"))
    narrar("Dra. Voss: 'O caos domina o diretório. Precisamos encontrar o arquivo [lexicon_core.zph].'", 0.025)
    pausa(1)
    
    seq = BuscaSequencial()
    progresso_ritual("Iniciando varredura manual...", passos=5, atraso=0.4)
    sucesso = seq.executar("lexicon_core.zph")

    if sucesso:
        narrar("Dr. Aris: 'O núcleo léxico vibra... ainda há vida nesses fragmentos.'", 0.03)
    else:
        narrar("Dra. Voss: 'Nada... talvez os fragmentos tenham se corrompido além da restauração.'", 0.03)
        return
    esperar_enter()

    # =========================================================
    # ETAPA 2 – BUSCA BINÁRIA
    # =========================================================
    limpar_tela()
    console.print(Panel("[yellow]Etapa 2: Rastreamento Binário[/yellow]", border_style="yellow"))
    narrar("Eng. Thorne: 'O mapa setorial está intacto. Precisamos localizar o Setor 877.'", 0.02)
    pausa(1)
    binaria = BuscaBinaria()
    progresso_ritual("Escaneando setores ordenados...", passos=6, atraso=0.25)
    resultado = binaria.buscar(877, 0, len(binaria.setores) - 1)

    if resultado:
        narrar(f"Eng. Thorne: 'Setor localizado: [bold cyan]{resultado}[/bold cyan]. Energia estável.'", 0.025)
    else:
        narrar("Eng. Thorne: 'Nenhum sinal de resposta... os canais podem ter colapsado.'", 0.025)
        return
    esperar_enter()

    # =========================================================
    # ETAPA 3 – BUSCA RABIN-KARP
    # =========================================================
    limpar_tela()
    console.print(Panel("[yellow]Etapa 3: Detecção de Padrões — Rabin-Karp[/yellow]", border_style="yellow"))
    narrar("Dra. Zhao: 'Há coordenadas escondidas em uma linguagem híbrida. Precisamos decifrar o padrão.'", 0.02)
    pausa(1)

    rabin = BuscaRabinKarp()
    progresso_ritual("Analisando registros textuais Zephyrianos...", passos=6, atraso=0.3)
    padrao = questionary.text("Insira o padrão de busca:").ask()

    if rabin.buscar(padrao):
        narrar("Dra. Zhao: 'Decodificação completa. As coordenadas foram restauradas.'", 0.025)
    else:
        narrar("Dra. Zhao: 'Nenhum padrão válido... tente outro marcador.'", 0.025)
    esperar_enter()

    # =========================================================
    # FINALIZAÇÃO
    # =========================================================
    limpar_tela()
    console.print(Panel.fit(
        Text.from_markup(
            "[bold green]Fase 1 completa![/bold green]\n"
            "[dim]Os fragmentos Aetherianos começam a se recompor.\n"
            "Um sussurro digital ecoa: 'Vocês despertaram algo que dormia há milênios...'[/dim]"
        ),
        border_style="green"
    ))
    pausa(3)

'''''''''