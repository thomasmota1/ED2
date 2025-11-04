# main.py

from utils.core import esperar_enter, narrar
from utils.intro import intro_lazarus
from fases.fase01_busca.introducao import introducao_fase1
from fases.fase01_busca.busca_sequencial import DesafioSequencial, desafio_sequencial
from fases.fase01_busca.busca_binaria import DesafioBinario

if __name__ == "__main__":
    intro_lazarus()
    
    #FASE 1 - BUSCA SEQUENCIAL E BINÁRIA
    introducao_fase1()
    desafio_parte1 = DesafioSequencial() 
    desafio_parte1.executar_desafio()
    desafio_parte2 = DesafioBinario()
    desafio_parte2.executar_desafio()
    narrar("Continua...")
    esperar_enter()

