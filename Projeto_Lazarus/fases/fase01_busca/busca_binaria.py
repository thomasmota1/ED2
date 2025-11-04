# Continuação direta após a recuperação do Núcleo Lexicônico (Fase 1).

import random
import time
import questionary
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from utils.core import narrar, fala, pausa, progresso_ritual, limpar_tela, esperar_enter

console = Console()


class DesafioBinario:

    def __init__(self):
        self.codigo_alvo = None
        self.catalogos = []
        self.nome_tratado = "Tratado de Convergência Zephyriana"
        self._familias = ["Aether", "Chronos", "Sigma", "Nova", "Zeta", "Omega"]
        self._tipos = ["Sintaxe Primária", "Verbo Ancestral", "Léxico Perdido", "Fonema de Contato"]


    def explorar_catalogos_ordenados(self):
        """
        Introdução narrativa e definição do código alvo.
        """
        console.print(Panel.fit(
            "[bold cyan]💽 Parte 2 - Os Catálogos de Convergência Zephyriana[/bold cyan]",
            border_style="cyan"
        ))

        fala("Lin", "A transição foi suave. O ruído caótico se dissipou e deu lugar a uma harmonia geométrica.")
        fala("Elara", "A estrutura aqui obedece a uma simetria antiga: os Catálogos Zephyrianos.")
        fala("Roric", "Diferente da varredura anterior, aqui os fragmentos se alinham numericamente. A busca poderá ser logarítmica.")
        fala("Kaelen", "Então observemos. Se a ordem persiste, que ela nos guie.")
        pausa(0.8)

        narrar("_Um eco residual do Núcleo Lexicônico percorre os condutos digitais, modulando-se em pulsos binários..._")
        fala("Lin", "Ele aprendeu... agora fala em lógica. O núcleo está nos guiando pela ordem.")

        console.print("\n[bold yellow]Sistema Lazarus:[/bold yellow] [dim]Decodificando registros e reconstruindo índices numéricos...[/dim]")
        progresso_ritual("Montando Catálogos Primários", 6, 0.25)

        fala("Elara", "Há um identificador recorrente nos arquivos centrais... 734-Δ.")
        fala("Roric", "Código 734. Parece um ponto de convergência. Talvez seja o índice do Tratado.")
        pausa(0.6)

        self.codigo_alvo = "734"
        return self.codigo_alvo


    def _gerar_catalogos(self):

        if not self.codigo_alvo:
            console.print("[red]ERRO: Código alvo não definido antes de gerar catálogos.[/red]")
            return

        codigo_alvo_int = int(self.codigo_alvo)

        for _ in range(50):
            codigo = random.randint(600, 900)
            while codigo in [c[0] for c in self.catalogos]:
                codigo = random.randint(600, 900)
            fragmento = f"{random.choice(self._familias)}-{random.choice(self._tipos)}"
            self.catalogos.append((codigo, fragmento))

        if not any(c[0] == codigo_alvo_int for c in self.catalogos):
            self.catalogos.append((codigo_alvo_int, "Nova-Convergência do Pensamento"))
        
        self.catalogos.sort()


    def mostrar_catalogos_interativo(self):

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Código", width=8)
        table.add_column("Fragmento", width=30)
        table.add_column("Integridade", width=15)

        estados = ["✅ Integro", "⚠️ Instável", "🔍 Parcial", "💾 Restaurado"]

        for codigo, nome in self.catalogos[:10]:
            table.add_row(str(codigo), nome, random.choice(estados))

        if len(self.catalogos) > 10:
            table.add_row("...", f"[dim]+ {len(self.catalogos) - 10} registros ocultos[/dim]", "...")

        console.print("\n")
        console.print(table)


    def analise_eficiencia_binaria(self, passos, tempo, sucesso):

        total = len(self.catalogos)
        eficiencia = passos / total
        pausa(0.4)

        fala("Roric", "Consolidando métricas do rastreamento binário...")
        fala("Elara", f"Foram {passos} leituras em um conjunto de {total}. Tempo decorrido: {tempo:.2f} segundos.")
        fala("Kaelen", "Complexidade teórica: O(log n). Cada passo é uma compressão da incerteza.")
        fala("Lin", "É quase poético. A ordem transformando o caos em clareza digital.")

        tempo_sequencial_estimado = tempo * (len(self.catalogos) / passos)
        fala("Kaelen", "Nossa, se fosse uma varredura sequencial levaria hm.... er....", 0.04)
        fala("Roric", f"levaria cerca de {tempo_sequencial_estimado:.2f} segundos.", 0.04)
        fala("Kaelen", "Isso! Isso mesmo!.", 0.04)
        fala("Elara", "É fascinante... o que antes demandava esforço linear, agora se resolve em poucos passos.", 0.04)


        if sucesso:
            fala("Elara", "A razão venceu o ruído. Cada iteração nos aproximou da verdade.")
        else:
            fala("Roric", "Mesmo a ordem pode falhar quando o ruído se esconde nos detalhes.")

        fala("Kaelen", "Em conjuntos gigantescos, essa técnica reduz exponencialmente o esforço de busca.")
        pausa(0.6)

        console.print(f"\n[bold yellow]📊 Métricas - Busca Binária[/bold yellow]")
        console.print(f"[dim]• Passos: {passos}[/dim]")
        console.print(f"[dim]• Total de registros: {total}[/dim]")
        console.print(f"[dim]• Tempo medido: {tempo:.2f}s[/dim]")
        console.print(f"[dim]• Eficiência: {eficiencia:.1%} do total consultado[/dim]")
        console.print(f"[dim]• Complexidade teórica: O(log n)[/dim]")



    def busca_binaria_interativa(self, alvo_int):
        
        
        console.print(f"\n[bold cyan]🔍 Iniciando rastreamento binário - alvo: [magenta]{alvo_int}[/magenta][/bold cyan]")

        esquerda, direita = 0, len(self.catalogos) - 1
        passos = 0
        inicio = time.time()

        while esquerda <= direita:
            passos += 1
            meio = (esquerda + direita) // 2
            codigo_atual, nome_atual = self.catalogos[meio]

            status = f"[dim]Analisando posição {meio}: código {codigo_atual} - {nome_atual}[/dim]"

            if codigo_atual == alvo_int:
                fala("Elara", "O pulso estabilizou. Encontramos o nó central - a assinatura Zephyriana responde.")
                console.print(f"{status} [green]→ CORRESPONDÊNCIA DETECTADA[/green]")
                tempo_total = time.time() - inicio
                return True, passos, tempo_total

            elif codigo_atual > alvo_int:
                fala("Roric", "Valor acima do esperado. Reduzindo o espectro de busca.")
                console.print(f"{status} [yellow]↶ Intervalo acima do alvo - reduzindo espaço de busca[/yellow]")
                direita = meio - 1
            else:
                fala("Kaelen", "Valor abaixo. Expanda para a direita, o conhecimento cresce em ondas.")
                console.print(f"{status} [blue]↷ Intervalo abaixo do alvo - expandindo para direita[/blue]")
                esquerda = meio + 1

            pausa(0.6)

        tempo_total = time.time.perf_counter() - inicio
        return False, passos, tempo_total


    # ============================================================
    # EXECUÇÃO PRINCIPAL - DESAFIO BINÁRIO
    # ============================================================

    def executar_desafio(self):

        limpar_tela()
        self.explorar_catalogos_ordenados()
        esperar_enter()

        limpar_tela()
        console.print(Panel.fit(
            "[bold green]🧩 Banco de Dados Zephyriano[/bold green]",
            border_style="green"
        ))

        self._gerar_catalogos()
        self.mostrar_catalogos_interativo()

        fala("Kaelen", "Aqui o caos cede espaço à lógica. O catálogo é ordenado. Nosso método deve ser também.")
        fala("Roric", "Implementando busca binária. Metade descartada a cada passo, uma dança de precisão.")
        fala("Elara", "Uma mente ordenada pensa como o logaritmo: reduz o caos a harmonia.")
        pausa(0.5)

        sucesso = False
        tentativas = 0

        while not sucesso:
            tentativas += 1
            if tentativas == 1:
                resposta = questionary.text(
                    f"Digite o código a buscar:",
                    default=self.codigo_alvo
                ).ask()
            else:
                resposta = questionary.text(
                    f"Tente novamente (dica: {self.codigo_alvo}):",
                    default=self.codigo_alvo
                ).ask()

            if resposta is None or resposta.lower() in ["sair", "exit", "quit"]:
                fala("Kaelen", "Encerrar o protocolo. A simetria pode esperar outro ciclo.")
                return

            try:
                codigo_busca = int(resposta)
                encontrado, passos, tempo = self.busca_binaria_interativa(codigo_busca)
                self.analise_eficiencia_binaria(passos, tempo, sucesso=encontrado)

                if encontrado:
                    sucesso = True
                    console.print(Panel.fit(
                        f"[bold green]✅ TRATADO DE CONVERGÊNCIA DECIFRADO[/bold green]\n"
                        f"Código: [magenta]{self.codigo_alvo}[/magenta]\n"
                        f"Passos: {passos} | Catálogo: {len(self.catalogos)} entradas",
                        border_style="green"
                    ))

                    fala("Roric", "Decodificação completa. Cada iteração dobrou o espaço da incerteza sobre si mesma.")
                    fala("Elara", "O logaritmo é pensamento condensado - a forma mais pura de raciocínio ordenado.")
                    fala("Kaelen", f"O {self.nome_tratado} foi restaurado. A linguagem voltou a respirar... e agora pensa.")
                else:
                    console.print(f"\n[red]❌ Código {resposta} não encontrado[/red]")
                    fala("Lin", "Mesmo entre ordens, ainda há falhas de sintonia. Tente novamente.")

            except ValueError:
                console.print("[red]❌ Entrada inválida - forneça apenas números[/red]")
                fala("Elara", "Apenas códigos numéricos são aceitos nos Catálogos Zephyrianos.")

        fala("Roric", "Vamos empregar o método de correlação Rabin-Karp. Ele nos permitirá rastrear padrões em textos.")
        fala("Lin", "Então seguimos - das ordens numéricas para as tramas do significado.")
        
        

