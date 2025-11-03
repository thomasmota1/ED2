# fases/fase1/fase1_rabin.py
# Versão Lazarus — Fase 3: As Tramas Linguísticas de Zephyr
# Continuação direta das Fases 1 e 2, mantendo o mesmo universo narrativo.

import random
import time
from rich.console import Console
from rich.panel import Panel
import questionary
from utils.core import narrar, pausa, progresso_ritual, limpar_tela, esperar_enter

console = Console()

def introducao_tramas_zephyr():
    """
    Introdução narrativa à Fase 3 — contextualiza a aplicação do Rabin-Karp.
    """
    console.print(Panel.fit(
        "[bold magenta]📜 Fase 3 — As Tramas Linguísticas de Zephyr[/bold magenta]",
        border_style="magenta"
    ))

    narrar("Elara: “Os Catálogos estavam em ordem, mas a língua que neles habita ainda é um labirinto.”", 0.04)
    narrar("Kaelen: “Esses registros não são simples dados — são os ecos de um idioma extinto.”", 0.04)
    narrar("Lin: “Cada símbolo se repete em padrões irregulares, como se a linguagem tentasse se reescrever.”", 0.04)
    narrar("Roric: “Precisamos de um método que reconheça padrões mesmo entre ruídos — algo que rastreie repetições com eficiência.”", 0.04)
    narrar("Kaelen: “Rabin-Karp. O algoritmo de correlação textual servirá como lente filológica.”", 0.04)
    pausa(1)

    console.print("\n[bold yellow]Sistema Lazarus:[/bold yellow] [dim]Gerando amostras de texto Zephyriano fragmentado...[/dim]")
    progresso_ritual("Carregando tomos linguísticos", 5, 0.3)


def gerar_tomos_zephyrianos():
    """
    Cria tomos artificiais (textos) e padrões a serem buscados com Rabin-Karp.
    """
    base_textos = [
        "aeon-thyra-velis aeon-thyra-solum aether-velis chronos-thyra",
        "nova-lexis-velis sigma-aeon-thyra aeon-thyra-velis nova-lexis",
        "chronos-thyra nova-lexis aether-velis aeon-thyra-velis",
    ]
    padroes = ["aeon-thyra", "nova-lexis", "aether-velis"]
    return base_textos, padroes


def aplicar_rabin_karp(texto, padrao):
    """
    Implementação simples do Rabin-Karp, retornando posições do padrão no texto.
    """
    n = len(texto)
    m = len(padrao)
    h_p = hash(padrao)
    ocorrencias = []

    for i in range(n - m + 1):
        if hash(texto[i:i+m]) == h_p:
            if texto[i:i+m] == padrao:
                ocorrencias.append(i)
    return ocorrencias


def analisar_resultados_rabin_karp(resultados):
    """
    Interpreta as métricas e resultados de forma narrativa.
    """
    total_padroes = len(resultados)
    total_ocorrencias = sum(len(oc) for oc in resultados.values())

    narrar(f"Roric: “Análise concluída — {total_padroes} padrões monitorados.”", 0.04)
    narrar(f"Lin: “Foram detectadas {total_ocorrencias} ocorrências distribuídas entre os tomos.”", 0.04)
    pausa(0.5)

    if total_ocorrencias == 0:
        narrar("Elara: “Nenhum eco linguístico persistiu. Talvez o idioma tenha se dissipado no tempo.”", 0.04)
    else:
        narrar("Elara: “Cada repetição é uma batida do idioma tentando se lembrar de si mesmo.”", 0.04)
        narrar("Kaelen: “É como ouvir o coração de uma civilização voltando a pulsar.”", 0.04)
        narrar("Roric: “Rabin-Karp operou com eficiência linear — correlação rápida, varredura direta.”", 0.04)
        narrar("Lin: “Os padrões estão voltando à superfície.”", 0.04)

    console.print("\n[bold yellow]📊 Métricas da Análise Linguística (Rabin-Karp)[/bold yellow]")
    console.print(f"[dim]• Padrões analisados: {total_padroes}[/dim]")
    console.print(f"[dim]• Ocorrências encontradas: {total_ocorrencias}[/dim]")
    console.print(f"[dim]• Complexidade média: O(n + m)[/dim]")


def desafio_rabin_karp():
    """
    Fase final — executa a reconstrução linguística usando Rabin-Karp.
    """
    limpar_tela()
    introducao_tramas_zephyr()

    textos, padroes = gerar_tomos_zephyrianos()
    resultados = {}

    narrar("Kaelen: “Escolha o padrão linguístico a ser rastreado.”", 0.04)
    padrao_escolhido = questionary.select(
        "Selecione um padrão Zephyriano:",
        choices=padroes
    ).ask()

    progresso_ritual("Rastreando padrões de correlação", 5, 0.25)

    for idx, texto in enumerate(textos, start=1):
        ocorrencias = aplicar_rabin_karp(texto, padrao_escolhido)
        resultados[f"Tomo_{idx}"] = ocorrencias
        console.print(f"\n[bold cyan]Tomo {idx} analisado:[/bold cyan]")
        console.print(f"[dim]{texto}[/dim]")
        if ocorrencias:
            console.print(f"[green]→ Padrão '{padrao_escolhido}' encontrado em {len(ocorrencias)} posição(ões).[/green]")
        else:
            console.print(f"[red]→ Nenhuma ocorrência do padrão encontrada.[/red]")
        pausa(0.6)

    analisar_resultados_rabin_karp(resultados)

    narrar("Elara: “As Tramas estão se recompondo... camada após camada, o idioma renasce.”", 0.04)
    narrar("Kaelen: “A missão linguística se completa. O Lazarus revive não apenas dados — mas significados.”", 0.04)
    narrar("Lin: “E cada repetição, cada eco, é uma lembrança resgatada da extinção.”", 0.04)
    narrar("Roric: “Fase concluída. Todos os protocolos de varredura e correlação encerrados.”", 0.04)

    console.print("\n[bold green]🌌 Missão Concluída — A Linguagem Zephyriana Ressurge[/bold green]")
    esperar_enter()
