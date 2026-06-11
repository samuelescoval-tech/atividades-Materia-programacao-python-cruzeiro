# Atividades de Programação em Python - Cruzeiro do Sul

Este repositório reúne atividades práticas desenvolvidas durante a disciplina de **Programação de Computadores**, no curso de **Análise e Desenvolvimento de Sistemas**.

O objetivo deste conjunto de projetos foi praticar conceitos fundamentais da linguagem Python, começando por scripts simples e avançando gradualmente para estruturas mais completas, com organização de código, funções, orientação a objetos, documentação e testes.

## Sobre o repositório

As atividades foram organizadas em quatro projetos principais:

```text
projeto-1-programacao-python/
projeto-2-programacao-python/
projeto-3-programacao-python/
projeto-4-programacao-python/
```

Cada pasta contém os arquivos relacionados à atividade, incluindo o código-fonte, o README específico do projeto e o PDF/documentação da entrega.

## Projetos desenvolvidos

### Projeto 1 - Conversão de Temperatura e Cálculo de Fatorial

O primeiro projeto contém dois scripts simples em Python:

* Conversão de temperatura de Celsius para Fahrenheit.
* Cálculo de fatorial utilizando a biblioteca nativa `math`.

Neste projeto foram praticados conceitos iniciais da linguagem, como:

* Variáveis
* Tipos primitivos
* Entrada de dados com `input()`
* Conversão de tipos com `float()` e `int()`
* Operadores matemáticos
* Saída de dados com `print()`
* Uso de biblioteca nativa

### Projeto 2 - Sistema Simples de Controle de Estoque

O segundo projeto consiste em um sistema de controle de estoque pelo terminal.

O sistema permite:

* Visualizar produtos cadastrados.
* Registrar entrada de produtos.
* Registrar saída de produtos.
* Atualizar quantidades em estoque.
* Validar se o produto existe.
* Encerrar o sistema pelo menu.

Neste projeto foram praticados conceitos como:

* Dicionários
* Listas
* Estruturas condicionais
* Laço `while`
* Menus interativos
* Manipulação dinâmica de dados
* Organização básica de regras de negócio

### Projeto 3 - Jogo da Forca

O terceiro projeto é um jogo da forca desenvolvido em Python.

O sistema sorteia uma palavra aleatória, recebe letras digitadas pelo usuário, verifica acertos e erros, controla tentativas e exibe uma representação visual da forca no terminal.

Neste projeto foram praticados conceitos como:

* Biblioteca `random`
* Listas
* Conjuntos com `set()`
* Laços de repetição
* Condicionais
* Funções
* Modularização
* Controle de tentativas
* Interação com o usuário

Este projeto também ajudou a reforçar a importância da organização lógica do código, principalmente no controle do fluxo do jogo e na separação das responsabilidades em funções.

### Projeto 4 - Sistema de Gerenciamento de Notas de Estudantes

O quarto projeto é um sistema acadêmico mais completo para gerenciamento de estudantes.

O sistema permite:

* Cadastrar alunos.
* Calcular média inicial.
* Calcular média final com recuperação.
* Verificar situação acadêmica.
* Classificar faixa etária.
* Verificar repetência.
* Prever ano de conclusão do curso.
* Gerar relatório completo da turma.
* Buscar relatório individual por nome.
* Pesquisar alunos por nome ou característica.
* Gerar estatísticas gerais da turma.
* Executar testes unitários.

Neste projeto, embora fosse possível utilizar uma lista de dicionários, optei por organizar os dados utilizando uma lista de objetos da classe `Aluno`. Essa escolha deixou o sistema mais organizado, pois cada aluno passou a ter seus próprios atributos e métodos.

Foram praticados conceitos como:

* Programação Orientada a Objetos
* Classes e objetos
* Métodos
* Funções auxiliares
* Validação de entradas
* Tratamento de erros com `try` e `except`
* Testes unitários com `unittest`
* Docstrings
* Organização de código
* Boas práticas de nomenclatura

## Tecnologias utilizadas

* Python 3
* Biblioteca `math`
* Biblioteca `random`
* Biblioteca `datetime`
* Biblioteca `unittest`
* Git e GitHub
* VS Code

## Estrutura do repositório

```text
atividades-Materia-programacao-python-cruzeiro/
│
├── projeto-1-programacao-python/
│   ├── calculo_fatorial.py
│   ├── conversor_temperatura.py
│   ├── projeto_1.pdf
│   └── README.md
│
├── projeto-2-programacao-python/
│   ├── sistema_estoque.py
│   ├── projeto_2.pdf
│   └── README.md
│
├── projeto-3-programacao-python/
│   ├── Jogo-da-forca-Atividade-cruzeiro.py
│   ├── projeto_3.pdf
│   └── README.md
│
├── projeto-4-programacao-python/
│   ├── main.py
│   ├── test_aluno.py
│   ├── projeto_4.pdf
│   └── README.md
│
├── .gitignore
└── README.md
```

## Como executar os projetos

Para executar qualquer projeto, acesse a pasta correspondente pelo terminal.

Exemplo:

```bash
cd projeto-4-programacao-python
python main.py
```

Dependendo do sistema, pode ser necessário usar:

```bash
python3 main.py
```

## Como executar os testes do Projeto 4

Dentro da pasta do Projeto 4, execute:

```bash
python -m unittest test_aluno.py
```

Ou:

```bash
python3 -m unittest test_aluno.py
```

## Aprendizados

Durante o desenvolvimento dessas atividades, consegui perceber uma evolução gradual na minha forma de pensar e escrever código.

Nos primeiros projetos, o foco estava em compreender a base da linguagem, como variáveis, entradas, saídas, conversões de tipo e operações matemáticas. Com o avanço das atividades, comecei a trabalhar com estruturas de dados, menus, validações, funções, modularização e orientação a objetos.

Um dos principais desafios foi transformar a lógica do exercício em código Python de forma clara e organizada. Em alguns momentos, encontrei dificuldades com indentação, controle de loops, organização das funções e escolha da melhor estrutura para representar os dados. Mesmo assim, a prática ajudou a tornar esses conceitos mais compreensíveis.

Também percebi a importância de revisar o código, testar as funcionalidades, documentar melhor os projetos e organizar os arquivos de forma adequada para publicação no GitHub.

## Objetivo no portfólio

Este repositório faz parte da construção do meu portfólio acadêmico e profissional na área de tecnologia.

Ele representa meus primeiros passos práticos com Python e mostra minha evolução entre atividades simples e projetos um pouco mais estruturados, com uso de funções, classes, testes e documentação.

A ideia é manter esses projetos públicos como registro de aprendizado e como base para projetos futuros mais completos.

## Autor

Samuel dos Santos Escoval

Estudante de Análise e Desenvolvimento de Sistemas
Projetos desenvolvidos como atividades práticas da disciplina de Programação de Computadores.
