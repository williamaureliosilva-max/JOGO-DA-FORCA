# Projeto: Jogo da Forca

## Formulação do Problema
Este projeto é uma implementação em Python do jogo da forca para demonstrar lógica de programação e manipulação de strings.

### Definição do Jogo
*   **Objetivo:** Adivinhar a palavra secreta letra a letra antes de esgotar as 6 tentativas.
*   **Regras Principais:** O jogador insere uma letra; se errar, o boneco é desenhado; se acertar, a letra é revelada na posição correta.
*   **Entrada (Input):** Caracteres (letras) inseridos via teclado.
*   **Saída (Output):** Visualização da forca em arte ASCII e estado atual da palavra oculta.
*   **Condição de Vitória:** Revelar todas as letras da palavra.
*   **Condição de Derrota:** Esgotar as 6 tentativas (boneco completo na forca).

## Requisitos do Sistema

### Requisitos Funcionais
1. O sistema deve escolher uma palavra aleatória de uma lista pré-definida.
2. O sistema deve permitir que o utilizador introduza uma letra por vez.
3. O sistema deve verificar se a letra introduzida existe na palavra secreta.
4. O sistema deve exibir o progresso da palavra (letras acertadas e espaços vazios).
5. O sistema deve contabilizar os erros e desenhar a forca em arte ASCII.
6. O sistema deve informar o resultado final (Vitória ou Derrota).

### Requisitos Não Funcionais
1. **Usabilidade:** A interface deve ser simples e clara via consola de texto.
2. **Robustez:** O sistema deve validar entradas inválidas sem encerrar o programa.
3. **Compatibilidade:** O código deve ser executável em ambiente Python 3.
```mermaid
 graph TD
    A([Início]) --> B[Escolher Palavra e Definir 6 Tentativas]
    B --> C{Palavra completa ou <br>tentativas == 0?}
    C -- Sim --> D{Ganhou?}
    D -- Sim --> E([Vitória])
    D -- Não --> F([Derrota])
    C -- Não --> G[/Pedir Letra/]
    G --> H{Letra na Palavra?}
    H -- Sim --> I[Revelar Letra]
    H -- Não --> J[Remover 1 Tentativa]
    I --> C
    J --> C
```


