# utils/core.py

from rich.console import Console
from rich.progress import track
from asciimatics.screen import Screen
from asciimatics.effects import Stars, Print, Cycle
from asciimatics.renderers import FigletText, Rainbow, StaticRenderer
from asciimatics.scene import Scene
import time, sys, os, random

console = Console()

CORES_PERSONAGENS = {
    "Kaelen": "bold blue",
    "Elara": "bold magenta",
    "Roric": "bold yellow",
    "Lin": "bold cyan",
    "Núcleo": "bold bright_magenta"
}

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

def esperar_enter(msg: str = "\n[dim][ENTER para continuar][/dim]"):
    console.input(msg)

def fala(personagem: str, texto: str, velocidade: float = 0.03):
    cor = CORES_PERSONAGENS.get(personagem, "white")
    console.print(f"[{cor}]{personagem}:[/] ", end="")
    for c in texto:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()
    pausa(0.3)

def nucleo(texto: str, velocidade: float = 0.03):
    console.print(f"[bold bright_magenta]💫 Núcleo Ressonante:[/] ", end="")
    for c in texto:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()
    pausa(0.3)

def pensar(texto: str, velocidade: float = 0.03):
    console.print(f"[italic dim white]{texto}[/italic dim white]")
    pausa(0.4)

def _efeito_glitch(texto, intensidade=3):
    resultado = ""
    for c in texto:
        if random.random() < 0.05 * intensidade:
            resultado += random.choice(["@", "#", "%", "&", "?", "ø", "∎"])
        else:
            resultado += c
    return resultado

def animacao_intro(titulo: str, subtitulo: str, duracao: int = 120):
    def _inner(screen):
        glitch_frames = [
            StaticRenderer([_efeito_glitch(titulo, i)]) for i in range(1, 5)
        ]
        efeitos = [
            Stars(screen, screen.width // 2),
            Print(screen, Rainbow(screen, FigletText(titulo, font="big")), 
                  screen.height // 2 - 5, speed=1, start_frame=0),
            Cycle(screen, FigletText(subtitulo, font="small"), 
                  screen.height // 2 + 5),
            Print(screen, glitch_frames[0], screen.height // 2 - 5, speed=3, start_frame=15),
            Print(screen, glitch_frames[1], screen.height // 2 - 5, speed=3, start_frame=25),
            Print(screen, glitch_frames[2], screen.height // 2 - 5, speed=3, start_frame=35),
            Print(screen, glitch_frames[3], screen.height // 2 - 5, speed=3, start_frame=45)
        ]
        screen.play([Scene(efeitos, duracao)], stop_on_resize=True, repeat=False)
    Screen.wrapper(_inner)


if __name__ == "__main__":
    limpar_tela()
    animacao_intro("LAZARUS", "SISTEMA RESSURGENTE")
    narrar("🔧 Teste de narrativa do Sistema Lazarus...")
    fala("Kaelen", "A ordem deve prevalecer.")
    fala("Elara", "Os padrões retornam, mas em nova forma.")
    fala("Roric", "O cálculo é exato, mas a mente... não.")
    fala("Lin", "A harmonia surge da iteração.")
    nucleo("Ressonância detectada... padrão 4_7 estável.")
    pensar("Talvez o código seja mais do que um número.")
    progresso_ritual("Sincronizando camadas cognitivas", 5, 0.15)
    esperar_enter()


''''
rascunho de emojis p usar

# 🚀 💾 🛑 ⚙️ 🌌 💠 ➤ ⚡ 🎮 🧠 💻 🔐 🧩 📡 📜 🧮 📊 🔍 💫 🔥 🌠 ❄️ ⚠️ ✅ ❌ 🌀 🔄 
# 🧙‍♂️ 🤖 🗿 😅 😎 😵‍💫 👁️   🧨 ✨ 🌙 🌑 🌕 🌈 💭 🪐 🌌 🧬 🔭 🛰️ ⚛️ 🧪 
# 🔋 💡 💎 ⚔️ 🛸  🧫 🧰 🧱 🧯 🧲 ⚗️ ⏳ ⌛ ⏰ 🕰️ 🧭 🧾 📂 📁 🗃️ 📈 📉 
# 📅 📖 🗒️ 🗓️ 📚 🧾  ✏️ 🖋️  🧮 💬 🗨️ 💭 🔊 🔈 🔉 🔇 🎵 🎶 🎧 
# 🧱  🧩  💠 🔮  🌫️ 🌬️ 🌩️ ⚡ 🔱 🔰 🛡️ 🕳️ 🧿 🌌 🪐  🌟 ✨ 
#  🔋 💡 💎 🧬 ⚛️ 🔭 🛰️ 🧪 💫 🪐  🪄 🪶 🕯️ 🧭 ⏳ 🔮  🧲 
# 💀 👾 👽 🤖 🧟‍♂️ 👁️ 🕳️ 🪐 🌀  🌠 💫 🌟 ✨ 🔆 🌌 🌙 🧿 🔮  
# 💬 🗨️ 🗯️ 🪶 🖋️ ✏️ 📜 📖 🧾 📚 📓 📒 📘 📗 📙 📕 ⬅⬅
# 🎛️ 🧰 🧩 🧪 🔬 🧫 🧬 ⚙️ 🧲 🧮 🛠️ 🔧 🔩 🔗 ⛓️ ⚗️  🔋 
# 🕹️ 🎚️ 🎛️ 🧭 ⏱️ ⏳ ⌛ 🕰️ ⏲️ 🕒 🕓 🕕 🕗 🕘 🕙 🕚 🕛 
# 🪙 💠 🔹 🔷 🔶 🔸 🔺 🔻 ⚫ ⚪ 🔵 🟣 🟡 🟢 🟤 🔴 🟧 
# ✦ ✧ ✩ ✪ ✫ ✬ ✭ ✮ ✯ ✰ ░▒▓█ ▁▂▃▄▅▆▇█▇▆▅▄▃▂▁ ╔═╗ ╚═╝ ═║
# ░▒▓█▇▆▅▄▃▂▁ ╔═╗ ╚═╝ ═║ ─│┌┐└┘├┤┬┴┼ ╔╦╗ ╚╩╝ ═╬═

'''