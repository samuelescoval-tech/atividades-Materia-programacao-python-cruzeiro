# Projeto 3 - Jogo da Forca em Python

Este projeto foi desenvolvido como parte da disciplina de Programação de Computadores, na Experiência Prática 3.

## Objetivo

Criar um jogo da forca em Python utilizando lógica de programação, estruturas de dados, funções, laços de repetição e interação com o usuário pelo terminal.

## Funcionalidades

- Sorteio aleatório de uma palavra secreta.
- Exibição da palavra com letras ocultas.
- Entrada de letras pelo usuário.
- Verificação de letras corretas e incorretas.
- Controle de tentativas restantes.
- Exibição visual da forca no terminal.
- Bloqueio de letras repetidas.
- Mensagem de vitória ou derrota.
- Opção de jogar novamente ao final da partida.

## Tecnologias utilizadas

- Python
- Biblioteca nativa `random`
- Listas
- Conjuntos com `set()`
- Laços de repetição `while`
- Estruturas condicionais `if`, `elif` e `else`
- Funções com `def`
- Docstrings
- Entrada de dados com `input()`
- Saída de dados com `print()`

## Como o jogo funciona

O programa possui uma lista de palavras possíveis:

```python
palavras = [
    "PYTHON",
    "PROGRAMACAO",
    "ESTRUTURA",
    "DEPURACAO",
    "SNAKECASE"
]