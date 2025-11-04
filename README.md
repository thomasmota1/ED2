# Lazarus: Uma Jornada Interativa por Algoritmos

Lazarus é um jogo narrativo interativo, executado no terminal, criado para a disciplina de Estrutura de Dados 2. O objetivo é demonstrar a implementação, aplicação e análise de performance de algoritmos clássicos (até o momento: Busca Sequencial e Busca Binária ) em um formato de ficção científica.

## Análise Técnica da Fase 1 (Busca)

Esta seção detalha a arquitetura, implementação e análise de complexidade dos algoritmos de busca utilizados.

### Arquitetura Geral

A arquitetura do projeto é construída em um modelo **Orientado a Objetos (OO)**, onde cada desafio de algoritmo é encapsulado em sua própria Classe.

1.  **Ponto de Entrada e Orquestração (`main.py`):**
    * O `main.py` serve como o **orquestrador central** do projeto. Ele é responsável por:
        1. Chamar a introdução visual (`intro_lazarus()`).
        2. **Instanciar** a classe de cada desafio (ex: `desafio_parte1 = DesafioSequencial()`).
        3. **Executar** o método principal de cada desafio (ex: `desafio_parte1.executar_desafio()`).

2.  **Fluxo de Controle Centralizado:**
    * O fluxo de controle do jogo é gerenciado inteiramente pelo `main.py`.
    * Ao contrário de um fluxo "encadeado" (onde a Fase 1 chamaria a Fase 2), o `main.py` espera `desafio_parte1.executar_desafio()` terminar completamente.
    * Somente após o término da Parte 1, o `main.py` instancia e executa a `desafio_parte2`. Isso torna o `main.py` o roteiro principal do jogo, facilitando a adição, remoção ou reordenação de fases.

3.  **Módulos de Desafio (Classes):**
    * O núcleo da lógica de cada desafio permanece encapsulado em sua respectiva Classe (ex: `DesafioSequencial` e `DesafioBinario`).
    * O estado de cada desafio (variáveis, listas de dados, etc.) é gerenciado internamente usando `self` (ex: `self.estado_nucleo`, `self.catalogos`).
    * A lógica principal de jogo para cada parte é contida em um método padrão `executar_desafio()`.

4.  **Pacote de Utilitários (`utils/core.py`):**
    * Este módulo centraliza todas as funções de interação e diálogo. Funções como `fala()`, `pensar()` e `nucleo()` recebem o nome do personagem e o texto, aplicando automaticamente as cores e a formatação corretas.

### Implementação e Integração dos Algoritmos

A lógica de cada algoritmo é implementada como um método dentro de sua respectiva classe de desafio.

#### 1. Busca Sequencial (Parte 1)

* **Implementação (`busca_sequencial` em `fase1_seq.py`):**
    * O algoritmo é um **método de classe**: `busca_sequencial(self, fragmentos, alvo)`.
    * Utiliza um loop `for` padrão para iterar pela lista, um contador `comparacoes` para análise de desempenho, e a instrução `break` para sair do loop assim que o alvo é encontrado.

* **Integração (Método `executar_desafio`):**
    * O método `executar_desafio()` gerencia todo o fluxo de jogo da Parte 1.
    * Ele chama `self.dialogo_com_resonador()` para a narrativa, prepara a lista de `fragmentos` (embaralhando `self.fragmentos_base`), e entra em um loop `while not encontrado` para coletar a entrada do usuário e invocar o método de busca.

#### 2. Busca Binária (Parte 2)

* **Implementação (`busca_binaria_interativa` em `fase1_bin.py`):**
    * O algoritmo é o método de classe `busca_binaria_interativa(self, alvo_int)`.
    * Ele inicializa os ponteiros `esquerda, direita = 0, len(self.catalogos) - 1`.
    * O núcleo é um loop `while esquerda <= direita`, que calcula o `meio = (esquerda + direita) // 2`.
    * O `codigo_atual` (no índice `meio`) é comparado ao `alvo_int`:
        * Se `codigo_atual > alvo_int`, a metade direita é descartada (`direita = meio - 1`).
        * Se `codigo_atual < alvo_int`, a metade esquerda é descartada (`esquerda = meio + 1`).
    * O método é "interativo" pois chama `fala(...)` a cada passo para narrar a decisão ("Valor acima", "Valor abaixo").

* **Integração (Método `executar_desafio`):**
    * O método `executar_desafio()` chama `self._gerar_catalogos()` para criar a lista de dados.
    * **Ponto-chave:** Dentro de `_gerar_catalogos()`, o pré-requisito da busca binária é garantido com a chamada de `self.catalogos.sort()`, que ordena a lista.
    * Após cada tentativa, `self.analise_eficiencia_binaria(...)` é chamada para exibir os resultados.

### Análise de Complexidade e Eficiência

A análise de complexidade é um elemento central da narrativa, explicada ao jogador pelos personagens.

#### 1. Busca Sequencial

* **Complexidade Teórica:** $O(n)$ (Linear).
* **Análise no Código:** Os personagens explicam a natureza $O(n)$:
    > `fala("Elara", "Complexidade teórica: O(n). Crescimento linear — a cada novo dado, uma nova leitura.")`
* **Eficiência Observada:** A eficiência é visivelmente lenta, com o jogo pausando a cada verificação (`time.sleep`). Isso demonstra ao jogador a ineficiência do método em conjuntos de dados não ordenados.

#### 2. Busca Binária

* **Complexidade Teórica:** $O(\log n)$ (Logarítmica).
* **Análise no Código:** A análise é realizada por um método dedicado, `analise_eficiencia_binaria(...)`. Este método não apenas exibe as métricas (Passos, Total, Tempo), mas também faz uma **comparação direta** com a Busca Sequencial.
    * Ele usa a performance da Busca Binária (tempo/passos) para **estimar** o tempo que uma Busca Sequencial ($O(n)$) levaria, através da fórmula: `tempo_sequencial_estimado = tempo * (len(self.catalogos) / passos)`.
    * Os personagens (Roric, Kaelen) discutem essa estimativa, fornecendo ao jogador uma comparação de tempo concreta (ex: 0.5s vs 5s).
* **Eficiência Observada:** O contraste é o ponto principal. O jogador vê em tempo real que a busca $O(\log n)$ é encontrada em poucos passos. O código então **calcula e narra** a economia de tempo exponencial em comparação com a busca $O(n)$, provando a teoria na prática.

---