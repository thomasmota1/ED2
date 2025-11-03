##  Arquitetura Geral (Fase 01: Busca)

A arquitetura do projeto é modular e segue uma progressão linear de desafios, encapsulados dentro do pacote `fases/fase01_busca`.

1.  **Ponto de Entrada (`main.py`):**
    * O `main.py` atua como o inicializador. Ele primeiro chama `utils/intro.py` para exibir a introdução narrativa e o logo "LAZARUS".
    * Em seguida, ele (presumivelmente) inicia a primeira fase chamando uma função de introdução (`introducao_fase1()`) que, por sua vez, deve acionar o primeiro desafio.

2.  **Módulos de Desafio Encadeados:**
    * A estrutura não retorna ao `main.py` após cada desafio. Em vez disso, cada módulo de desafio é responsável por chamar o próximo, criando uma "corrente".
    * `fases/fase01_busca/busca_sequencial.py`: Contém o `desafio_sequencial()`. Ao final de sua execução bem-sucedida, este arquivo chama diretamente `desafio_binario()`.
    * `fases/fase01_busca/busca_binaria.py`: Contém o `desafio_binario()`. Ao final de sua execução, ele chama `desafio_rabin_karp()` (que, como você mencionou, ainda será implementada, mas a estrutura de chamada já existe).

3.  **Pacote de Utilitários (`utils/`):**
    * `utils/intro.py`: Responsável puramente pela apresentação inicial e configuração da narrativa principal.
    * `utils/core.py` (inferido): Este módulo (referenciado, mas não fornecido) centraliza funções comuns usadas em todos os desafios, como `narrar()`, `pausa()`, `limpar_tela()` e `progresso_ritual()`, mantendo o código dos desafios focado na lógica e narrativa.

## Implementação e Integração dos Algoritmos

Cada algoritmo é implementado como uma função central de busca, que é então "envolvida" por uma função de desafio (`desafio_...`) que cuida da narrativa, coleta de entrada do usuário e preparação dos dados.

### 1. Busca Sequencial (Parte 1)

* **Implementação (`busca_sequencial` em `busca_sequencial.py`):**
    * O algoritmo é implementado na função `busca_sequencial(fragmentos, alvo)`.
    * Ele utiliza um loop `for` simples para iterar sobre cada `fragmento` na lista `fragmentos`.
    * Um contador `comparacoes` é incrementado a cada iteração para fins de análise.
    * A cada passo, ele imprime o fragmento sendo verificado (`[dim]Verificando fragmento...`).
    * Se `fragmento == alvo`, a função define `encontrado = True`, imprime uma mensagem de sucesso e usa `break` para sair do loop.
    * A própria função inclui chamadas narrativas (`narrar(...)`) que explicam sua complexidade teórica ($O(n)$) ao final da execução.

* **Integração (`desafio_sequencial`):**
    * O desafio prepara a lista de `fragmentos` (incluindo o `alvo_correto`) e a embaralha (`random.shuffle(fragmentos)`) para garantir que a busca não encontre o item na primeira posição (pior caso ou caso médio).
    * Ele entra em um loop `while not encontrado`, solicitando a entrada do usuário.
    * A função `busca_sequencial` é chamada com a lista e o alvo fornecido pelo usuário.
    * A narrativa (`dialogo_com_resonador`) é usada para fornecer pistas (4_7) ao jogador.

### 2. Busca Binária (Parte 2)

* **Implementação (`busca_binaria_interativa` em `busca_binaria.py`):**
    * Implementada na função `busca_binaria_interativa(catalogos, alvo)`.
    * **Pré-requisito:** O algoritmo assume que a lista `catalogos` já está ordenada numericamente (o que é garantido pela função `desafio_binario` usando `catalogos.sort()`).
    * Ele inicializa os ponteiros `esquerda, direita = 0, len(catalogos) - 1`.
    * O núcleo é um loop `while esquerda <= direita`.
    * A cada iteração, calcula o índice `meio = (esquerda + direita) // 2`.
    * Ele compara o `codigo_atual` (em `catalogos[meio]`) com o `alvo`.
    * **Se `== alvo`**: Retorna `True`.
    * **Se `> alvo`**: Descarta a metade direita, definindo `direita = meio - 1`.
    * **Se `< alvo`**: Descarta a metade esquerda, definindo `esquerda = meio + 1`.
    * A função é "interativa" pois narra cada passo, explicando se o valor está "acima" ou "abaixo" e como o espaço de busca está sendo reduzido.

* **Integração (`desafio_binario`):**
    * O desafio primeiro gera uma lista de `catalogos` (tuplas de `(codigo, nome)`) e **garante que ela esteja ordenada** com `catalogos.sort()`.
    * Ele solicita ao usuário o código a ser buscado (`codigo_busca`).
    * Chama `busca_binaria_interativa` com a lista ordenada e o código.
    * Após a execução, ele chama `analise_eficiencia_binaria`, uma função dedicada a imprimir as métricas de desempenho (passos, tempo, total) e reforçar a complexidade $O(\log n)$.

## Análise de Complexidade e Eficiência

A análise de complexidade é um elemento central da narrativa do jogo, com os personagens explicando explicitamente o desempenho de cada algoritmo.

### 1. Busca Sequencial

* **Complexidade Teórica:** $O(n)$ (Linear).
* **Análise no Código:** O próprio código verbaliza isso através dos personagens:
    > `narrar("Elara: “Complexidade teórica: O(n). Crescimento linear — a cada novo dado, uma nova leitura.”")`
* **Eficiência Observada:** A eficiência é diretamente proporcional ao tamanho da lista ($n$) e à posição do alvo. Nos testes (o jogo), o jogador experimenta uma varredura item por item, que é visivelmente lenta (pausada por `time.sleep`). A narrativa reforça que este método é "exaustivo" para conjuntos de dados grandes.

### 2. Busca Binária

* **Complexidade Teórica:** $O(\log n)$ (Logarítmica).
* **Análise no Código:** A análise é feita na função `analise_eficiencia_binaria` e verbalizada pelos personagens:
    > `narrar("Kaelen: “A complexidade é O(log n) — o ganho de eficiência é exponencial frente à varredura linear.”")`
* **Eficiência Observada:** A eficiência é demonstrada drasticamente. O algoritmo encontra o alvo em um número muito pequeno de `passos`, mesmo em um catálogo de 50+ itens. A função de análise exibe métricas concretas (ex: `Passos: 6`, `Total de registros: 51`), provando visualmente ao jogador como a estratégia de "dividir para conquistar" reduz o tempo de busca.