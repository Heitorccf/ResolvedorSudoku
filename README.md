# Sudoku Game and Solver

Este é um programa simples de Sudoku implementado em Python. Ele oferece duas funcionalidades principais: jogar um jogo de Sudoku ou resolver um tabuleiro automaticamente usando força bruta com visualização. O tabuleiro de Sudoku é gerado aleatoriamente a cada execução, garantindo uma nova experiência toda vez.

## Funcionalidades

1. **Jogar Sudoku**: O jogador pode tentar resolver o tabuleiro manualmente, inserindo valores nas posições vazias. O programa verificará se as inserções são válidas de acordo com as regras do Sudoku.
2. **Resolver Sudoku por Força Bruta**: O programa usa um algoritmo de backtracking para resolver o tabuleiro automaticamente. A solução é exibida gradualmente, mostrando o processo de preenchimento do Sudoku em tempo real.

## Requisitos

- Python 3.x
- Sistema operacional compatível com o comando `clear` (Linux/macOS) ou `cls` (Windows).

## Como Executar

1. **Clone o repositório** ou copie o código-fonte para um arquivo local chamado `sudoku.py`.
2. Execute o programa com o seguinte comando:
    ```bash
    python sudoku.py
    ```

3. O programa abrirá um menu com as seguintes opções:

    - **1. Jogar Sudoku**: Inicia um jogo de Sudoku onde você pode inserir manualmente números no tabuleiro.
    - **2. Resolver por força bruta**: Gera um tabuleiro de Sudoku e resolve automaticamente usando força bruta, mostrando o processo.
    - **3. Sair**: Sai do jogo.

## Como Jogar

1. Selecione a opção **1** no menu para jogar.
2. O tabuleiro será exibido com alguns números já preenchidos e outros espaços vazios (representados por `0`).
3. Insira a linha, coluna e número que deseja colocar, garantindo que seu movimento siga as regras do Sudoku.
4. O jogo verifica a validade do seu movimento e atualiza o tabuleiro. Continue até completar o jogo.

### Exemplo de tabuleiro

```
5 3 0 | 0 7 0 | 0 0 0
6 0 0 | 1 9 5 | 0 0 0
0 9 8 | 0 0 0 | 0 6 0
- - - - - - - - - - - 
8 0 0 | 0 6 0 | 0 0 3
4 0 0 | 8 0 3 | 0 0 1
7 0 0 | 0 2 0 | 0 0 6
- - - - - - - - - - - 
0 6 0 | 0 0 0 | 2 8 0
0 0 0 | 4 1 9 | 0 0 5
0 0 0 | 0 8 0 | 0 7 9
```

## Lógica de Resolução

A função de resolução do Sudoku utiliza **backtracking** para resolver o tabuleiro. O algoritmo tenta números de 1 a 9 em cada célula vazia e avança quando encontra um número válido. Se ficar preso, ele volta para a célula anterior e tenta outro número.

## Visualização

Ao escolher a opção **Resolver por força bruta**, o tabuleiro é resolvido passo a passo, com uma pequena pausa entre as atualizações, permitindo que você veja o progresso da solução em tempo real.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias ou novas funcionalidades.

---

### Licença

Este projeto não possui uma licença específica.

---

### Contato

Se você tiver alguma dúvida ou sugestão, fique à vontade para entrar em contato.
