# fases/buscas.py

import time

def busca_sequencial(fragmentos, alvo):
    """Busca sequencial com visualização melhorada"""
    comparacoes = 0
    inicio = time.time()
    
    for i, fragmento in enumerate(fragmentos):
        comparacoes += 1
        
        # Verificação com possível lógica adicional
        if fragmento == alvo:
            fim = time.time()
            return True, comparacoes, fim - inicio
            
        # Pequena pausa para efeito dramático
        time.sleep(0.1)
    
    fim = time.time()
    return False, comparacoes, fim - inicio

def busca_binaria(lista, alvo):
    comparacoes = 0
    inicio = time.time()
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        comparacoes += 1
        if lista[meio] == alvo:
            tempo = time.time() - inicio
            return True, comparacoes, tempo
        elif lista[meio] < alvo:
            baixo = meio + 1
        else:
            alto = meio - 1
    tempo = time.time() - inicio
    return False, comparacoes, tempo

def rabin_karp(texto, padrao):
    d = 256
    q = 101
    n = len(texto)
    m = len(padrao)
    comparacoes = 0
    inicio = time.time()
    h = pow(d, m-1) % q
    p = 0
    t = 0
    for i in range(m):
        p = (d*p + ord(padrao[i])) % q
        t = (d*t + ord(texto[i])) % q
    for s in range(n - m + 1):
        comparacoes += 1
        if p == t:
            if texto[s:s+m] == padrao:
                tempo = time.time() - inicio
                return True, s, comparacoes, tempo
        if s < n - m:
            t = (d*(t - ord(texto[s])*h) + ord(texto[s+m])) % q
            if t < 0:
                t += q
    tempo = time.time() - inicio
    return False, None, comparacoes, tempo
