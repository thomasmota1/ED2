# fases/fase1/fase1_bin.py
# Versão Lazarus — Fase 2: Os Catálogos Ordenados
# Personagens: Dr. Kaelen Aris, Prof. Elara Voss, Eng. Roric Thorne, Dra. Lin Zhao.

import random
import time
import questionary
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from utils.core import narrar, pausa, progresso_ritual, limpar_tela, esperar_enter
from fases.fase01_busca.busca_rabinKarp import desafio_rabin_karp

console = Console()


# ============================================================
# INTRODUÇÃO — A ORDEM RENASCENTE
# ============================================================

def explorar_catalogos_ordenados():
    """
    Introdução narrativa e contextual dos Catálogos Ordenados.
    Retorna o código alvo a ser buscado.
    """
    console.print(Panel.fit(
        "[bold cyan]💽 Parte 2 — Os Catálogos Ordenados[/bold cyan]",
        border_style="cyan"
    ))

    narrar("Lin: “A transição foi suave. O ruído caótico se dissipou e deu lugar a uma harmonia geométrica.”", 0.04)
    narrar("Elara: “A estrutura aqui obedece a uma simetria antiga — os Catálogos Zephyrianos.”", 0.04)
    narrar("Roric: “Diferente da varredura anterior, aqui os fragmentos se alinham numericamente. A busca poderá ser logarítmica.”", 0.04)
    narrar("Kaelen: “Então observemos. Se a ordem persiste, que ela nos guie.”", 0.04)
    pausa(0.8)

    narrar("Um eco residual do Núcleo Ressonante percorre os condutos digitais, modulando-se em pulsos binários.", 0.04)
    narrar("Lin: “Ele aprendeu... agora fala em lógica. O núcleo está nos guiando pela ordem.”", 0.04)

    console.print("\n[bold yellow]Sistema Lazarus:[/bold yellow] [dim]Decodificando registros e reconstruindo índices numéricos...[/dim]")
    progresso_ritual("Montando Catálogos Primários", 6, 0.25)

    narrar("Elara: “Há um identificador recorrente nos arquivos centrais... 734.”", 0.04)
    narrar("Roric: “Código 734. Parece um ponto de convergência.”", 0.04)
    return "734"


# ============================================================
# VISUALIZAÇÃO DOS CATÁLOGOS
# ============================================================

def mostrar_catalogos_interativo(catalogos):
    """
    Exibe parte dos catálogos em formato de tabela, simulando estrutura ordenada.
    """
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Código", width=8)
    table.add_column("Fragmento", width=30)
    table.add_column("Integridade", width=15)

    estados = ["✅ Integro", "⚠️  Instável", "🔍 Parcial", "💾 Restaurado"]
    for codigo, nome in catalogos[:10]:
        table.add_row(str(codigo), nome, random.choice(estados))

    if len(catalogos) > 10:
        table.add_row("...", f"[dim]+ {len(catalogos) - 10} registros ocultos[/dim]", "...")

    console.print("\n")
    console.print(table)


# ============================================================
# ANÁLISE DE EFICIÊNCIA — BUSCA BINÁRIA
# ============================================================

def analise_eficiencia_binaria(passos, total, tempo, sucesso):
    eficiencia = passos / total
    pausa(0.4)

    narrar("Roric: “Consolidando métricas do rastreamento binário...”", 0.04)
    narrar(f"Elara: “Foram {passos} leituras em um conjunto de {total}. O tempo foi {tempo:.2f} segundos.”", 0.04)
    narrar("Kaelen: “A complexidade é O(log n) — o ganho de eficiência é exponencial frente à varredura linear.”", 0.04)

    if sucesso:
        narrar("Lin: “A ordem favorece a razão. Cada passo reduz o caos.”", 0.04)
    else:
        narrar("Elara: “Mesmo a ordem não garante sucesso. O erro é parte do aprendizado do sistema.”", 0.04)

    narrar("Kaelen: “Para conjuntos gigantescos, a busca binária reduz drasticamente o tempo de resposta.”", 0.04)

    console.print(f"\n[bold yellow]📊 Métricas — Busca Binária[/bold yellow]")
    console.print(f"[dim]• Passos: {passos}[/dim]")
    console.print(f"[dim]• Total de registros: {total}[/dim]")
    console.print(f"[dim]• Tempo medido: {tempo:.2f}s[/dim]")
    console.print(f"[dim]• Eficiência: {eficiencia:.1%} do total consultado[/dim]")
    console.print(f"[dim]• Complexidade teórica: O(log n)[/dim]")


# ============================================================
# IMPLEMENTAÇÃO DA BUSCA BINÁRIA
# ============================================================

def busca_binaria_interativa(catalogos, alvo):
    """
    Implementa a busca binária com visualização dos passos e falas narrativas.
    Retorna (encontrado, passos, tempo).
    """
    console.print(f"\n[bold cyan]🔍 Iniciando rastreamento binário — alvo: [magenta]{alvo}[/magenta][/bold cyan]")

    esquerda, direita = 0, len(catalogos) - 1
    passos = 0
    inicio = time.time()

    while esquerda <= direita:
        passos += 1
        meio = (esquerda + direita) // 2
        codigo_atual, nome_atual = catalogos[meio]

        status = f"[dim]Analisando posição {meio}: código {codigo_atual} — {nome_atual}[/dim]"

        if codigo_atual == alvo:
            narrar("Elara: “O pulso estabilizou. Encontramos o nó central.”", 0.04)
            console.print(f"{status} [green]→ CORRESPONDÊNCIA DETECTADA[/green]")
            tempo_total = time.time() - inicio
            return True, passos, tempo_total

        elif codigo_atual > alvo:
            narrar("Roric: “Valor acima. Reduzindo o espectro.”", 0.04)
            console.print(f"{status} [yellow]↶ Intervalo acima do alvo — reduzindo espaço de busca[/yellow]")
            direita = meio - 1
        else:
            narrar("Kaelen: “Valor abaixo. Ajustando varredura para direita.”", 0.04)
            console.print(f"{status} [blue]↷ Intervalo abaixo do alvo — expandindo para direita[/blue]")
            esquerda = meio + 1

        pausa(0.6)

    tempo_total = time.time() - inicio
    return False, passos, tempo_total


# ============================================================
# EXECUÇÃO PRINCIPAL — DESAFIO BINÁRIO
# ============================================================

def desafio_binario():
    """
    Execução completa da Fase 2 — narrativa, visualização e métrica técnica integradas.
    """
    limpar_tela()
    codigo_alvo = explorar_catalogos_ordenados()
    esperar_enter()

    limpar_tela()
    console.print(Panel.fit(
        "[bold green]🧩 Banco de Dados Zephyriano[/bold green]",
        border_style="green"
    ))

    familias = ["Aether", "Chronos", "Sigma", "Nova", "Zeta", "Omega"]
    tipos = ["Sintaxe Primária", "Verbo Ancestral", "Léxico Perdido", "Fonema de Contato"]
    catalogos = []

    for _ in range(50):
        codigo = random.randint(600, 900)
        while codigo in [c[0] for c in catalogos]:
            codigo = random.randint(600, 900)
        fragmento = f"{random.choice(familias)}-{random.choice(tipos)}"
        catalogos.append((codigo, fragmento))

    catalogos.sort()
    if not any(c[0] == int(codigo_alvo) for c in catalogos):
        catalogos.append((int(codigo_alvo), "Nova-Léxico Vital"))
        catalogos.sort()

    mostrar_catalogos_interativo(catalogos)

    narrar("Kaelen: “Aqui o caos cede espaço à lógica. O catálogo é ordenado — nosso método deve ser também.”", 0.04)
    narrar("Roric: “Implementando busca binária. Metade descartada a cada passo — elegância matemática.”", 0.04)
    narrar("Elara: “Uma forma de raciocínio que imita a clareza da razão Zephyriana.”", 0.04)
    pausa(0.5)

    tentativas = 0
    sucesso = False

    sucesso = False
    tentativas = 0

    while not sucesso:
        tentativas += 1

        if tentativas == 1:
            resposta = questionary.text(
                f"Digite o código a buscar (dica: {codigo_alvo}):",
                default=codigo_alvo
            ).ask()
        else:
            resposta = questionary.text(
                f"Digite novamente o código a buscar (dica: {codigo_alvo}):",
                default=codigo_alvo
            ).ask()

        # --- SAÍDA OPCIONAL ---
        if resposta is None or resposta.lower() in ["sair", "exit", "quit"]:
            narrar("Kaelen: “Encerrar o protocolo. A simetria pode esperar outro ciclo.”", 0.04)
            return  # sai da função de forma limpa

        try:
            codigo_busca = int(resposta)
            encontrado, passos, tempo = busca_binaria_interativa(catalogos, codigo_busca)
            analise_eficiencia_binaria(passos, len(catalogos), tempo, sucesso=encontrado)

            if encontrado:
                sucesso = True
                console.print(Panel.fit(
                    f"[bold green]✅ FRAGMENTO CRÍTICO LOCALIZADO[/bold green]\n"
                    f"Código: [magenta]{codigo_alvo}[/magenta]\n"
                    f"Passos: {passos} | Catálogo: {len(catalogos)} entradas",
                    border_style="green"
                ))

                narrar("Roric: “Confirmação em poucos passos. A precisão é quase poética.”", 0.04)
                narrar("Elara: “A lógica substitui o caos. A razão, enfim, se faz música.”", 0.04)
                narrar("Kaelen: “Sigamos. Próxima etapa — padrões linguísticos e correlação simbólica.”", 0.04)

            else:
                console.print(f"\n[red]❌ Código {resposta} não encontrado[/red]")
                narrar("Lin: “Mesmo entre ordens, ainda há falhas de sintonia. Tente novamente.”", 0.04)

        except ValueError:
            console.print("[red]❌ Entrada inválida — forneça apenas números[/red]")
            narrar("Elara: “Apenas códigos numéricos são aceitos nos Catálogos Zephyrianos.”", 0.04)


    narrar("Roric: “Vamos empregar o método de correlação Rabin-Karp. Ele nos permitirá rastrear padrões em textos.”", 0.04)
    narrar("Lin: “Então, seguimos — das ordens numéricas para as tramas do significado.”", 0.04)

    esperar_enter()
    desafio_rabin_karp()
