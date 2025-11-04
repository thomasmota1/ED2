import random
import time
import questionary
from rich.console import Console
from rich.panel import Panel
from utils.core import fala, pensar, nucleo, narrar, pausa, progresso_ritual, limpar_tela, esperar_enter
from fases.fase01_busca.busca_binaria import DesafioBinario

console = Console()

class DesafioSequencial:

    def __init__(self):
        self.estado_nucleo = 0  # 0 = calmo, 1 = cansado, 2 = irritado, 3 = instável
        self.codigo_correto = 457
        self.alvo_correto = f"FRG-Nova-{self.codigo_correto}-Lexicon_Core"
        self.fragmentos_base = [
            "FRG-Aether-231-Fragmentado",
            "FRG-Chronos-789-Parcial",
            "FRG-Nova-123-Secundario",
            "FRG-Sigma-654-Integro",
            "FRG-Nova-457-Lexicon_Core",
            "FRG-Zeta-985-Degenerado",
            "FRG-Omega-332-Parcial",
            "FRG-Nova-999-Secundario",
            "FRG-Alpha-101-Fragmentado",
            "FRG-Nova-888-Secundario"
        ]


    def pulso_de_luz(self):
        respostas = {
            0: [
                "💫 O núcleo responde suavemente: 'Padrões restaurados.'",
                "💫 Uma voz cristalina sussurra: 'Ressonância estável. Leitura limpa.'",
                "💫 O núcleo emite um tom harmônico: 'Código parcial detectado: 4 e 7.'"
            ],
            1: [
                "💫 O núcleo vibra com leve esforço: 'Repetindo o sinal... é o mesmo padrão: 4_7.'",
                "💫 Um eco digital murmura: 'Já conversamos sobre isso... 4 e 7, sempre eles.'"
            ],
            2: [
                "💫 O núcleo chia: 'De novo isso? O padrão é 4 e 7! Anote dessa vez!'",
                "💫 Faíscas surgem: 'Vocês humanos têm memória curta. 4 e 7, nada mais.'"
            ],
            3: [
                "💫 O núcleo treme violentamente: 'CHEGA! MAS TUDO BEM... 4 e 7... é sempre 4 e 7!'",
                "💫 Pulsos caóticos ecoam: 'Vocês vão me desintegrar se continuarem assim!'"
            ]
        }

        cores_base = ["magenta", "bright_magenta", "white", "bright_blue"]
        console.print("\n[bold magenta]O núcleo começa a pulsar lentamente...[/bold magenta]")
        for _ in range(2 + self.estado_nucleo):
            for cor in cores_base:
                console.print(f"[bold {cor}]💠💠💠💠💠[/bold {cor}]", end="\r")
                time.sleep(0.12)
        console.print(" " * 20, end="\r")

        fala_nucleo = random.choice(respostas[self.estado_nucleo])
        nucleo(fala_nucleo)
        pausa(0.5)


    def dialogo_com_resonador(self):
        

        console.print(Panel.fit(
            "[bold magenta]🔭 Comunicação com o Núcleo Ressonante[/bold magenta]",
            border_style="magenta"
        ))

        narrativas = [
            "Ondas de luz percorrem o laboratório. Um núcleo vibra com timidez e ecos harmônicos...",
            "O núcleo parece hesitar, como se já conhecesse essa conversa.",
            "Uma centelha de impaciência percorre o núcleo. Ele emite um ruído grave.",
            "O núcleo está instável. Faíscas dançam no ar como se fossem pensamentos em colapso."
        ]
        pensar(narrativas[min(self.estado_nucleo, 3)])
        pausa(0.6)

        escolha = questionary.select(
            "O que deseja fazer?",
            choices=[
                "Tentar se comunicar com o Núcleo",
                "Ignorar e prosseguir com a busca"
            ]
        ).ask()

        if "Ignorar" in escolha:
            fala("Elara", "Sem consultar o núcleo? Muito bem... prepare-se para procurar às cegas.")
            return True

        self.pulso_de_luz()
        fala("Lin", "Sincronizando... há um eco de padrão numérico ... quatro e sete.")
        fala("Kaelen", "O dígito central está perdido. Pista parcial: 4_7.")
        fala("Roric", "Nada mal. Com isso, já temos um vetor inicial para a varredura.")

        console.print(f"\n[bold yellow]💡 Pista registrada: padrão parcial 4_7[/bold yellow]")
        self.estado_nucleo = min(self.estado_nucleo + 1, 3)
        return True
    

    def busca_sequencial(self, fragmentos, alvo):

        fala("Roric", "Iniciando varredura sequencial. Um fragmento por vez…")
        pausa(0.6)
        encontrado = False
        comparacoes = 0
        
        tempo_inicio_simulacao = time.perf_counter() 

        for fragmento in fragmentos:
            comparacoes += 1
            
            console.print(f"[dim]Verificando fragmento {comparacoes}: [cyan]{fragmento}[/cyan][/dim]")
            time.sleep(0.25)

            if fragmento == alvo:
                fala("Lin", f"Hm… este parece correto. {fragmento} reage à ressonância.")
                console.print(f"[green]✅ Fragmento localizado após {comparacoes} verificações.[/green]")
                encontrado = True
                break 
            else:
                fala("Kaelen", f"Hm… não é este. ({fragmento})")
                time.sleep(0.15) 
        
        tempo_fim_simulacao = time.perf_counter()
        tempo_total_simulacao = tempo_fim_simulacao - tempo_inicio_simulacao

        if not encontrado:
            console.print(f"[red]❌ Nenhum fragmento correspondente encontrado após {comparacoes} verificações.[/red]")
        
        pausa(0.5)
        
        return encontrado, comparacoes, tempo_total_simulacao

    def analise_busca_sequencial(self, encontrado, comparacoes, tempo_total, total_fragmentos):
        """
        Recebe os resultados da busca sequencial e gera os diálogos de análise.
        """
        fala("Roric", f"Telemetria: {comparacoes} comparações realizadas.")
        fala("Elara", f"O tempo total da varredura simulada foi de {tempo_total:.2f} segundos.")
        fala("Elara", "Complexidade teórica: O(n). Crescimento linear - a cada novo dado, uma nova leitura.")

        
        if encontrado:
            if comparacoes == 1:
                fala("Lin", "Estava bem no topo da pilha. Que sorte.")
                pensar("Análise: Melhor Caso (Best Case) O(1). Encontrado na primeira tentativa.")
            elif comparacoes == total_fragmentos:
                fala("Kaelen", f"Típico. Era o último. Verificamos todos os {total_fragmentos} fragmentos.")
                pensar(f"Análise: Pior Caso (Worst Case) O(n). Encontrado na última posição ({comparacoes} comparações).")
            else:
                fala("Elara", f"Posição {comparacoes} de {total_fragmentos}. Não foi o melhor, mas também não foi o pior.")
                pensar(f"Análise: Caso Médio (Average Case) O(n). {comparacoes} comparações.")
        else:
             fala("Kaelen", f"Verificamos todos os {total_fragmentos} itens e nada. Uma falha completa, e com o custo máximo.")
             pensar(f"Análise: Pior Caso (Worst Case) O(n). Alvo não encontrado após {comparacoes} comparações.")

        fala("Kaelen", "Para conjuntos pequenos é viável, mas em volumes gigantes, esse processo seria exaustivo.")
        pausa(0.5)

        eficiencia = comparacoes / total_fragmentos
        console.print("\n[bold yellow]📊 Métricas — Busca Sequencial[/bold yellow]")
        console.print(f"[dim]• Comparações: {comparacoes}[/dim]")
        console.print(f"[dim]• Total de fragmentos: {total_fragmentos}[/dim]")
        console.print(f"[dim]• Tempo estimado: {tempo_total:.2f}s[/dim]")
        console.print(f"[dim]• Eficiência: {eficiencia:.1%} do total consultado[/dim]")
        console.print(f"[dim]• Complexidade teórica: O(n)[/dim]")

        fala("Roric", "A varredura sequencial exige uma leitura por elemento - linear, implacável.", 0.04)
        fala("Elara", " 'Implacável' não é bem a palavra que eu usaria. Para dez fragmentos é aceitável, mas imagine um milhão. O tempo cresce junto com o caos.", 0.04)

     # ============================================================
    # EXECUÇÃO PRINCIPAL
    # ============================================================    
    def executar_desafio(self):


        limpar_tela()
        console.print(Panel.fit(
            "[bold yellow]🌐 Parte 1 — A Ressonância dos Fragmentos Perdidos[/bold yellow]",
            border_style="yellow"
        ))

        fala("Kaelen", "A Cripta de Dados pulsa com ruído. Ecos de informação lutam para se manter íntegros.")
        fala("Elara", "Entre esses ecos, há um Lexicon_Core que precisamos encontrar.")
        fala("Roric", "Sem estrutura, resta-nos o método mais primitivo, a busca sequencial.")
        pausa(0.8)

        self.dialogo_com_resonador()

        fragmentos = self.fragmentos_base.copy()
        random.shuffle(fragmentos)

        console.print(Panel.fit(
            "[bold blue]🎯 Campo de Varredura — Fragmentos Ressonantes[/bold blue]",
            border_style="blue"
        ))
        console.print(f"[dim]Total de fragmentos carregados: {len(fragmentos)}[/dim]\n")

        encontrado = False
        while not encontrado:
            entrada = console.input("[white]Digite o número (ex: 457) ou nome completo do fragmento:[/white]\n> ").strip()
            alvo = f"FRG-Nova-{entrada}-Lexicon_Core" if entrada.isdigit() else entrada

            progresso_ritual("Sintonizando sensores e iniciando varredura...", passos=5, atraso=0.3)
            encontrado_bool, comparacoes, tempo = self.busca_sequencial(fragmentos, alvo)
            self.analise_busca_sequencial(encontrado_bool, comparacoes, tempo, len(fragmentos))

            if encontrado_bool:
                if alvo == self.alvo_correto:
                    fala("Kaelen", "Excelente. O Núcleo Lexicônico foi restaurado. Sinal estabilizado.")
                    console.print(Panel.fit("[bold green]✅ Lexicon_Core RECUPERADO[/bold green]", border_style="green"))
                    fala("Elara", "Mesmo em pequena escala, a varredura foi lenta. Em um banco real, levaria horas.")
                    fala("Roric", "Hora de seguir para métodos mais eficientes : os Catálogos Ordenados.")
                    encontrado = True
                else:
                    fala("Elara", f"Esse arquivo existe, mas não é o Lexicon_Core. Continue buscando o código {self.codigo_correto}.")
                    encontrado = False
            else:
                escolha = questionary.select(
                    "Nada encontrado. O que deseja fazer?",
                    choices=[
                        "Conversar com o Núcleo Ressonante",
                        "Tentar outro código manualmente",
                        
                    ]
                ).ask()

                if "Núcleo" in escolha:
                    self.dialogo_com_resonador()
                

        console.print("\n" + "═" * 60)
        fala("Kaelen", "A primeira camada está completa. Agora, avançaremos aos Catálogos Digitais Ordenados.")
        esperar_enter()

        
def desafio_sequencial():
    desafio = DesafioSequencial()
    return desafio.executar_desafio()
