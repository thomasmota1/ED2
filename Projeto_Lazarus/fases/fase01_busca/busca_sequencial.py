
import random
import time
import questionary
from rich.console import Console
from rich.panel import Panel
from utils.core import narrar, pausa, progresso_ritual, limpar_tela, esperar_enter
from fases.fase01_busca.busca_binaria import desafio_binario

console = Console()
estado_nucleo = 0  # 0 = calmo, 1 = cansado, 2 = irritado, 3 = instável



def pulso_de_luz():
   
    global estado_nucleo

    respostas = {
        0: [
            "💫 O núcleo responde suavemente: 'Padrões restaurados.'",
            "💫 Uma voz cristalina sussurra: 'Ressonância estável. Leitura limpa.'",
            "💫 O núcleo emite um tom harmônico: 'Código parcial detectado: 4 e 7.'"
        ],
        1: [
            "💫 O núcleo vibra com leve esforço: 'Repetindo o sinal... é o mesmo padrão: 4_7.'",
            "💫 Um eco digital murmura: 'Já conversamos sobre isso... 4 e 7, sempre eles.'",
            "💫 Luzes tremulam: 'A sintonia se repete. O padrão não mudou.'"
        ],
        2: [
            "💫 O núcleo chia: 'De novo isso? O padrão é 4 e 7! Anote dessa vez!'",
            "💫 Faíscas surgem: 'Vocês humanos têm memória curta. 4 e 7, nada mais.'",
            "💫 Um ruído sarcástico vibra: 'Sim, o mesmo código. Surpreso?'"
        ],
        3: [
            "💫 O núcleo treme violentamente: 'CHEGA! MAS TUDO BEM... 4 e 7... é sempre 4 e 7!'",
            "💫 Pulsos caóticos ecoam: 'Vocês vão me desintegrar se continuarem assim!'",
            "💫 Um grito eletrônico reverbera: 'O padrão é o mesmo! O universo não mudou! 4....?.....7'"
        ]
    }

    cores_base = ["magenta", "bright_magenta", "white", "bright_blue"]
    console.print("\n[bold magenta]O núcleo começa a pulsar lentamente...[/bold magenta]")
    time.sleep(0.5)

    for _ in range(2 + estado_nucleo):
        for cor in cores_base:
            console.print(f"[bold {cor}]💠💠💠💠💠[/bold {cor}]", end="\r")
            time.sleep(0.12)
    console.print(" " * 20, end="\r")

    fala = random.choice(respostas[estado_nucleo])
    console.print(f"[bold cyan]{fala}[/bold cyan]\n")
    pausa(0.5)



def dialogo_com_resonador():

    global estado_nucleo
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
    narrar(narrativas[min(estado_nucleo, 3)], 0.04)
    pausa(0.6)

    escolha = questionary.select(
        "O que deseja fazer?",
        choices=[
            "Tentar se comunicar com o Núcleo",
            "Ignorar e prosseguir com a busca"
        ]
    ).ask()

    if "Ignorar" in escolha:
        narrar("Elara: “Sem consultar o núcleo? Muito bem... prepare-se para procurar às cegas.”", 0.04)
        return True

    pulso_de_luz()
    narrar("Lin Zhao: “Sincronizando... há um eco de padrão numérico — quatro e sete.”", 0.04)
    narrar("Kaelen: “O dígito central está perdido. Pista parcial: 4_7.”", 0.04)
    narrar("Roric: “Nada mal. Com isso, já temos um vetor inicial para a varredura.”", 0.04)

    console.print(f"\n[bold yellow]💡 Pista registrada: padrão parcial 4_7[/bold yellow]")
    pausa(0.6)

    estado_nucleo = min(estado_nucleo + 1, 3)
    return True



def busca_sequencial(fragmentos, alvo):

    narrar("Roric: “Iniciando varredura sequencial. Um fragmento por vez…”", 0.04)
    pausa(0.6)
    encontrado = False
    comparacoes = 0

    for fragmento in fragmentos:
        comparacoes += 1
        console.print(f"[dim]Verificando fragmento {comparacoes}: [cyan]{fragmento}[/cyan][/dim]")
        time.sleep(0.25)

        if fragmento == alvo:
            narrar(f"Lin Zhao: “Hm… este parece correto. {fragmento} reage à ressonância.”", 0.04)
            console.print(f"[green]✅ Fragmento localizado após {comparacoes} verificações.[/green]")
            encontrado = True
            break
        else:
            narrar(f"Kaelen: “Hm… não é este. ({fragmento})”", 0.04)
            time.sleep(0.15)

    narrar(f"Roric: “Telemetria: {comparacoes} comparações realizadas.”", 0.04)
    narrar("Elara: “Complexidade teórica: O(n). Crescimento linear — a cada novo dado, uma nova leitura.”", 0.04)
    narrar("Kaelen: “Para conjuntos pequenos é viável, mas em volumes gigantes, esse processo seria exaustivo.”", 0.04)
    pausa(0.5)

    if not encontrado:
        console.print(f"[red]❌ Nenhum fragmento correspondente encontrado após {comparacoes} verificações.[/red]")
    return encontrado


def desafio_sequencial():
    
    limpar_tela()
    console.print(Panel.fit(
        "[bold yellow]🌐 Parte 1 — A Ressonância dos Fragmentos Perdidos[/bold yellow]",
        border_style="yellow"
    ))

    narrar("Kaelen: “A Cripta de Dados pulsa com ruído. Ecos de informação lutam para se manter íntegros.”", 0.04)
    narrar("Elara: “Entre esses ecos, há um fragmento vital que precisamos encontrar.”", 0.04)
    narrar("Roric: “Sem estrutura, resta-nos o método mais primitivo — a busca sequencial.”", 0.04)
    pausa(0.8)

    dialogo_com_resonador()

    codigo_correto = 457
    alvo_correto = f"FRG-Nova-{codigo_correto}-Vital"

    fragmentos = [
        "FRG-Aether-231-Fragmentado",
        "FRG-Chronos-789-Parcial",
        "FRG-Nova-123-Secundario",
        "FRG-Sigma-654-Integro",
        "FRG-Nova-457-Vital",
        "FRG-Zeta-985-Degenerado",
        "FRG-Omega-332-Parcial",
        "FRG-Nova-999-Secundario",
        "FRG-Alpha-101-Fragmentado",
        "FRG-Nova-888-Secundario"
    ]
    random.shuffle(fragmentos)

    console.print(Panel.fit(
        "[bold blue]🎯 Campo de Varredura — Fragmentos Ressonantes[/bold blue]",
        border_style="blue"
    ))
    console.print(f"[dim]Total de fragmentos carregados: {len(fragmentos)}[/dim]\n")

    encontrado = False

    while not encontrado:
        entrada = console.input("[white]Digite o número (ex: 457) ou nome completo do fragmento:[/white]\n> ").strip()

        if entrada.isdigit():
            alvo = f"FRG-Nova-{entrada}-Vital"
        else:
            alvo = entrada

        progresso_ritual("Sintonizando sensores e iniciando varredura...", passos=5, atraso=0.3)
        encontrado = busca_sequencial(fragmentos, alvo)

        if encontrado:
            if alvo == alvo_correto:
                narrar("Kaelen: “Excelente. O fragmento vital foi restaurado. Sinal estabilizado.”", 0.04)
                console.print(Panel.fit("[bold green]✅ FRAGMENTO VITAL RECUPERADO[/bold green]", border_style="green"))
                narrar("Elara: “Mesmo em pequena escala, a varredura foi lenta. Em um banco real, levaria horas.”", 0.04)
                narrar("Roric: “Hora de seguir para métodos mais eficientes — os Catálogos Ordenados.”", 0.04)
            else:
                narrar("Elara: “Esse arquivo existe, mas não é o vital. Continue buscando o código 457.”", 0.04)
                encontrado = False
        else:
            escolha = questionary.select(
                "Nada encontrado. O que deseja fazer?",
                choices=[
                    "Conversar novamente com o Núcleo Ressonante",
                    "Tentar outro código manualmente",
                    "Encerrar a busca"
                ]
            ).ask()

            if "Núcleo" in escolha:
                dialogo_com_resonador()
            elif "Encerrar" in escolha:
                narrar("Kaelen: “Encerrando a varredura. Salvando registros parciais.”", 0.04)
                return
            # Continua o loop

    console.print("\n" + "═" * 60)
    narrar("Kaelen: “A primeira camada está completa. Agora, avançaremos aos Catálogos Digitais Ordenados.”", 0.04)
    esperar_enter()
    desafio_binario()
