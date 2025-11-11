import time
import random
import unicodedata
from rich.console import Console
from rich.panel import Panel
from utils.core import narrar, fala, pausa, progresso_ritual, limpar_tela, esperar_enter

console = Console()

class FaseRabinTempoReal:
    def __init__(self):
        self.texto = (
            "= TRATADO DE CONVERGÊNCIA ZEPHYRIANA =\n"
            "Seção VII - A Instabilidade do Núcleo.\n"
            "‘Toda energia precisa vibrar em sintonia com o código que a originou.’\n"
            "Os antigos relatam que uma palavra de sintonia pode acalmar o Núcleo.\n"
            "Ela foi perdida entre ironias e repetições; a pista fala em harmonia e frequência.\n"
            "...\n"
            "RESSONANCIA: Executar Compressão Harmônica. Aplicar algoritmo de Huffman.\n"
            "Indexar resultado com HASH-42. Transmitir ao Núcleo Lexicônico.\n"
            "Evitar eco e repetição. O silêncio é estabilidade.\n"
            "...\n"
            "Fim do Tratado."
        )
        self.d = 256
        self.q = 101
        self.palavra_chave = "RESSONANCIA"

    def normalizar(self, texto):
        t = texto.upper()
        t = unicodedata.normalize("NFD", t)
        t = "".join(c for c in t if unicodedata.category(c) != "Mn")
        return t

    def hash_inicial(self, s, m):
        h = 0
        for i in range(m):
            h = (self.d * h + ord(s[i])) % self.q
        return h

    def animacao_hash(self, texto, padrao):
        console.print("\n[bold yellow] Iniciando calculo de hashes...[/bold yellow]")
        barras = ["▁▂▃▄▅▆▇█", "▂▃▄▅▆▇█▇", "▃▄▅▆▇█▇▅", "▄▅▆▇█▇▅▄"]
        for i in range(8):
            bloco = random.choice(barras)
            console.print(f"[magenta]Rolando janela {i+1}...[/magenta] [dim]{bloco}[/dim]", end="\r")
            time.sleep(0.2)
        console.print("\n[bold green]✔ Hashes iniciais calculados e sincronizados[/bold green]\n")
        pausa(0.5)

    def busca_rabin(self, texto, padrao):
        texto_n = self.normalizar(texto)
        padrao_n = self.normalizar(padrao)
        n, m = len(texto_n), len(padrao_n)
        if m > n:
            return [], 0.0
        h = pow(self.d, m - 1, self.q)
        p_hash = self.hash_inicial(padrao_n, m)
        t_hash = self.hash_inicial(texto_n, m)
        resultados = []
        tempo_inicio = time.perf_counter()
        for s in range(n - m + 1):
            if p_hash == t_hash:
                if texto_n[s:s + m] == padrao_n:
                    resultados.append(s)
            if s < n - m:
                t_hash = (self.d * (t_hash - ord(texto_n[s]) * h) + ord(texto_n[s + m])) % self.q
                if t_hash < 0:
                    t_hash += self.q
        tempo_total = time.perf_counter() - tempo_inicio
        return resultados, tempo_total

    def animacao_instavel(self, intensidade=6):
        for i in range(intensidade):
            offset = random.randint(0, 6)
            vazio = " " * offset
            console.print(vazio + Panel.fit("[bold red]⚠ Núcleo instável . Vibração detectada[/bold red]", border_style="red"))
            time.sleep(0.12)
            limpar_tela()
        console.print(Panel.fit("[red]⚠ Instabilidade crescente... ajuste a busca.[/red]", border_style="red"))
        pausa(0.6)

    def animacao_estabiliza(self):
        barras = ["▁▂▃▄▅▆▇█", "▂▃▄▅▆▇█▇", "▃▄▅▆▇█▇▅", "▄▅▆▇█▇▅▄", "▅▆▇█▇▅▄▃", "▇█▇▅▄▃▂▁"]
        for i in range(len(barras)):
            console.print(Panel.fit(f"[green]Sintonia: {barras[i]}[/green]"))
            time.sleep(0.18)
        console.print(Panel.fit("[bold green]✔ Núcleo estabilizado[/bold green]", border_style="green"))
        pausa(0.6)

    def analise_complexidade(self, n, m, tempo, sucesso):
        resultado = "SUCESSO" if sucesso else "FALHA"
        fala("Roric", "Calculando métricas da varredura...")
        fala("Elara", f"Tamanho do texto: {n} | Padrão: {m}")
        fala("Kaelen", "Melhor caso aproximado: O(n + m). Rolamento de hash evita comparações desnecessárias.")
        fala("Lin", "Pior caso: O(n × m) se houver muitos falsos ecos (colisões).")
        console.print(Panel.fit(
            f"[bold yellow]📊 Métricas Rabin-Karp ({resultado})[/bold yellow]\n"
            f"Tamanho do texto: {n}\n"
            f"Tamanho do padrão: {m}\n"
            f"Tempo de execução: {tempo:.4f}s\n"
            f"Melhor caso: O(n + m)\n"
            f"Pior caso: O(n × m)",
            border_style="yellow"
        ))
        pausa(0.8)

    def reacao_erro(self, tentativa, tentativas):
        opcoes = [
            [("Kaelen", f"'{tentativa.upper()}'? Isso... definitivamente não soou em sintonia."),
             ("Elara", "Talvez se focássemos em algo mais... harmônico."),
             ("Roric", "Ou menos inventado.")],
            [("Lin", "O núcleo fez um barulho estranho. Acho que ele riu."),
             ("Kaelen", "Se ele rir mais, explode."),
             ("Elara", "Ok, sem pânico. Só... pense em vibrações.")],
            [("Roric", "Nada ainda. O núcleo parece ofendido."),
             ("Kaelen", "Isso foi quase doloroso de ver."),
             ("Lin", "Tenta alguma coisa que lembre som, frequência... ou música.")],
            [("Elara", "Já testamos quase tudo. Quer tentar 'RESSONANCIA' logo?"),
             ("Roric", "Sim, talvez algo nessa linha... sem acento, talvez?"),
             ("Kaelen", "Vai que é isso. Pior que isso não fica.")],
        ]
        reacoes = opcoes[min(tentativas - 1, len(opcoes) - 1)]
        for nome, fala_texto in reacoes:
            fala(nome, fala_texto)

    def executar(self):
        limpar_tela()
        console.print(Panel.fit("[bold cyan]📜 Parte 3 - A Busca pela Palavra de Sintonia[/bold cyan]", border_style="cyan"))
        fala("Kaelen", "O Tratado voltou a nós, mas o Núcleo vibra com instabilidade crescente.")
        fala("Elara", "Entre os trechos, há menções a harmonia e frequência. Pode haver uma palavra de sintonia escondida.")
        fala("Roric", "Se ela estiver lá, o Rabin-Karp pode encontrá-la entre o ruído.")
        fala("Lin", "O Núcleo está quase colapsando. Precisamos agir.")
        progresso_ritual("Conectando scanners lexicais ao Núcleo...", 4, 0.25)
        tentativas = 0

        while True:
            tentativa = console.input("\n[cyan]Digite a palavra que deseja procurar no Tratado (dica: pense em 'harmonia'):[/cyan] ").strip()
            if not tentativa:
                fala("Elara", "Precisamos de uma palavra concreta para vasculhar o texto.")
                continue

            tentativas += 1
            self.animacao_hash(self.texto, tentativa)
            resultados, tempo_total = self.busca_rabin(self.texto, tentativa)
            n = len(self.texto)
            m = len(tentativa)

            if resultados:
                fala("Kaelen", f"'{tentativa.upper()}' localizado. O núcleo emite um eco harmônico.")
                for pos in resultados:
                    contexto = self.texto[max(0, pos - 60):min(len(self.texto), pos + 160)]
                    console.print(Panel.fit(f"[bold magenta]Trecho identificado:[/bold magenta]\n{contexto}", border_style="magenta"))
                self.analise_complexidade(n, m, tempo_total, sucesso=True)

                if self.normalizar(tentativa) == self.normalizar(self.palavra_chave):
                    self.animacao_estabiliza()
                    fala("Elara", "O trecho revela instruções de restauração: Compressão Harmônica com Huffman e indexação via HASH-42.")
                    fala("Roric", "Não é magia. É o protocolo de recuperação Zephyriano. Vamos aplicar.")
                    console.print(Panel.fit("[bold cyan]🚀 Próxima Fase: Compressão e Indexação (Huffman & Hashing)[/bold cyan]", border_style="cyan"))
                    esperar_enter()
                    break
                else:
                    fala("Roric", "Há eco, mas não a sintonia certa. Continuem.")
                    self.reacao_erro(tentativa, tentativas)
            else:
                fala("Lin", f"'{tentativa.upper()}' não provocou resposta. O Núcleo se distorce.")
                self.animacao_instavel()
                self.analise_complexidade(n, m, tempo_total, sucesso=False)
                self.reacao_erro(tentativa, tentativas)
