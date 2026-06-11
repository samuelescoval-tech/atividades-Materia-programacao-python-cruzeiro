# Projeto 2 - Sistema de Controle de Estoque

Este projeto foi desenvolvido como parte da disciplina de Programação de Computadores.

## Objetivo

Criar um sistema simples de controle de estoque em Python, permitindo visualizar produtos cadastrados, registrar entrada de produtos, registrar saída de produtos e encerrar o sistema.

## Funcionalidades

- Visualizar o estoque atual.
- Registrar entrada de produtos.
- Registrar saída de produtos.
- Verificar se o produto existe no estoque.
- Verificar se há quantidade suficiente antes da saída.
- Encerrar o sistema pelo menu.
- Tratar opções inválidas digitadas pelo usuário.

## Tecnologias utilizadas

- Python
- Dicionários
- Listas
- Estruturas condicionais `if`, `elif` e `else`
- Laço de repetição `while True`
- Entrada de dados com `input()`
- Conversão de tipos com `int()`
- Saída de dados com `print()`
- F-strings

## Estrutura inicial do estoque

O estoque foi criado usando um dicionário, onde cada produto possui uma lista com duas informações:

```python
estoque = {
    "Notebook": [10, 3500.00],
    "Mouse": [50, 80.00],
    "Teclado": [30, 150.00]
}