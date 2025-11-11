# Lazarus: Uma Jornada Interativa por Algoritmos

Lazarus é um jogo narrativo interativo, executado no terminal, criado para a disciplina de Estrutura de Dados 2. O objetivo é demonstrar a implementação, aplicação e análise de performance de algoritmos clássicos (até o momento: Busca Sequencial e Busca Binária ) em um formato de ficção científica.

## Análise Técnica do Modulo/Fase 1 (Busca)

Esta seção detalha a arquitetura, implementação e análise de complexidade dos algoritmos de busca utilizados.

### Arquitetura Geral

A arquitetura do projeto é construída em um modelo **Orientado a Objetos (OO)**, onde cada desafio de algoritmo é encapsulado em sua própria Classe.

1.  **Menu Principal e Navegação (`main.py`):**
    * O `main.py` evoluiu de um *script* linear para um **menu interativo** que controla a navegação, utilizando a biblioteca `questionary` para a interface do usuário no terminal.
    * Ele agora é responsável por gerenciar o ciclo de vida da aplicação (o loop `while True` principal) e apresentar os menus de navegação.
    * As principais funções do `main.py` são:
        1.  Apresentar o `menu_principal()` (Jogo Completo, Carregar Fase, Sair).
        2.  Apresentar o `menu_carregar_fase_parte()` para seleção de pontos de entrada específicos.
        3.  Delegar a execução com base na escolha do usuário.

2.  **Fluxo de Controle :**
    * O `main.py` controla o fluxo através de duas funções de execução principais:
    * **`executar_fase1_completa()`**: Esta função encapsula o fluxo linear original do jogo (Introdução -> Sequencial -> Binária -> Rabin-Karp) para quem escolhe "Iniciar Jogo Completo".
    * **`executar_parte_especifica(escolha)`**: Esta função, controlada pelo `menu_carregar_fase_parte()`, permite **isolar e executar** qualquer desafio de forma independente (ex: pular direto para "Fase 1 - Rabin-Karp"). Isso facilita o *debug*, o teste e a rejogabilidade de partes específicas.

3.  **Módulos de Desafio (Classes):**
    * O núcleo de cada desafio permanece encapsulado em sua respectiva Classe (ex: `DesafioSequencial`, `DesafioBinario`, `FaseRabinTempoReal`).
    * O `main.py` agora **instancia** essas classes sob demanda, seja em sequência (em `executar_fase1_completa`) ou individualmente (em `executar_parte_especifica`).
    * O estado de cada desafio (variáveis, listas de dados, etc.) é gerenciado internamente usando `self` dentro de cada classe.

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

#### 3. Rabin-Karp (Parte 3)

* **Implementação (`busca_rabin` em `fase3_rabin.py`):**
    * O algoritmo é implementado na classe `FaseRabinTempoReal` como o método `busca_rabin(self, texto, padrao)`.
    * Ele utiliza um **rolling hash** (hash deslizante) para encontrar uma sub-string (padrão) dentro de um texto maior.
    * Ele calcula um hash inicial para o `padrao` (`p_hash`) e para a primeira "janela" do `texto` (`t_hash`).
    * Em um loop, ele desliza a janela de texto, calculando o novo `t_hash` em tempo constante O(1) (subtraindo o caractere que saiu e adicionando o que entrou).
    * **Tratamento de Colisão:** Quando `p_hash == t_hash`, o algoritmo realiza uma verificação ingênua (caractere por caractere) para garantir que não é um "falso eco" (uma colisão de hash).
    * **Normalização:** O método `normalizar(self, texto)` é usado para remover acentos e converter para maiúsculas, tornando a busca *case-insensitive* e *accent-insensitive*.

* **Integração (Método `executar`):**
    * O método `executar()` gerencia o fluxo da Parte 3, pedindo ao usuário uma "palavra de sintonia".
    * A cada tentativa, `self.busca_rabin` é chamado.
    * Se `resultados` for encontrado, o jogo verifica if é a palavra-chave correta (`self.palavra_chave = "RESSONANCIA"`).
    * Falhas na busca (sem resultados) ou encontrar a palavra errada disparam animações de "instabilidade" (`animacao_instavel`), guiando o jogador.

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
* **Eficiência Observada:** O contraste é o ponto principal. O jogador vê em tempo real que a busca $O(\log n)$ é encontrada em poucos passos. O código então calcula e narra a economia de tempo exponencial em comparação com a busca $O(n)$, provando a teoria na prática.

#### 3. Rabin-Karp

* **Complexidade Teórica:**
    * **Melhor Caso/Caso Médio:** $O(n + m)$ (Linear). Onde 'n' é o tamanho do texto e 'm' o do padrão. O pré-processamento do hash é $O(m)$ e a busca é $O(n)$ graças ao *rolling hash*.
    * **Pior Caso:** $O(n \times m)$. Isso ocorre em um cenário adverso onde ocorrem muitas colisões de hash ("falsos ecos"), forçando o algoritmo a fazer $O(m)$ comparações ingênuas em quase $O(n)$ posições.

* **Análise no Código:** A análise é feita pelo método `analise_complexidade(self, n, m, tempo, sucesso)`.
    * Os personagens discutem explicitamente os casos:
        > `fala("Kaelen", "Melhor caso aproximado: O(n + m). Rolamento de hash evita comparações desnecessárias.")`
        > `fala("Lin", "Pior caso: O(n × m) se houver muitos falsos ecos (colisões).")`
* **Eficiência Observada:** A narrativa do jogo transforma a complexidade em gameplay. Os "falsos ecos" (palavras encontradas que não são a chave) e as "falhas" (palavras não encontradas) são tratadas como "ruído" e "instabilidade" do Núcleo. O sucesso em $O(n+m)$ é a "sintonia" que estabiliza o sistema. O tempo de execução real (`{tempo:.4f}s`) é sempre exibido, mostrando a velocidade do algoritmo na prática.
  
---