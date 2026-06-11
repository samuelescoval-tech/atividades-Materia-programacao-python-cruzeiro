# Sistema de Gerenciamento de Notas de Estudantes

## Descrição

Este projeto é um sistema simples de gerenciamento acadêmico desenvolvido em Python.

O sistema permite cadastrar estudantes, calcular médias, verificar a situação acadêmica, considerar nota de recuperação, classificar faixa etária, verificar repetência, prever o ano de conclusão do curso, pesquisar alunos, buscar relatório individual e gerar estatísticas da turma.

O projeto foi estruturado com foco em modularidade, organização do código, uso de docstrings, testes unitários e aplicação de boas práticas de nomenclatura em Python.

## Funcionalidades

* Cadastro de alunos
* Cálculo da média inicial
* Cálculo da média final com recuperação
* Verificação da situação acadêmica
* Classificação por faixa etária
* Verificação de repetência
* Previsão do ano de conclusão do curso
* Exibição de relatório completo de todos os alunos
* Busca de relatório individual por nome
* Pesquisa por nome ou característica
* Estatísticas gerais da turma
* Validação de notas, idade e ano de entrada
* Testes unitários com `unittest`

## Requisitos

Para executar o projeto, é necessário ter o Python instalado na máquina.

Versão recomendada:

```bash
Python 3.10 ou superior
```

## Estrutura do Projeto

A estrutura sugerida para o projeto é:

```text
projeto-4-sistema-notas-python/
│
├── main.py
├── test_aluno.py
└── README.md
```

O arquivo `main.py` contém o código principal do sistema.
O arquivo `test_aluno.py` contém os testes unitários.
O arquivo `README.md` contém a documentação do projeto.

## Como executar o sistema

1. Abra o terminal ou prompt de comando.

2. Acesse a pasta onde o projeto está salvo:

```bash
cd projeto-4-sistema-notas-python
```

3. Execute o arquivo principal:

```bash
python main.py
```

Ou, dependendo do sistema:

```bash
python3 main.py
```

4. Após executar o programa, será exibido um menu com as seguintes opções:

```text
===== SISTEMA ESCOLAR =====
1 - Ver relatório de todos os alunos
2 - Adicionar aluno
3 - Pesquisar alunos por nome ou característica
4 - Buscar relatório individual por nome
5 - Estatísticas da turma
6 - Sair
```

## Como usar o menu

### 1 - Ver relatório de todos os alunos

Exibe o relatório completo de todos os alunos cadastrados, mostrando nome, idade, faixa etária, notas, média inicial, nota de recuperação, média final, situação acadêmica, repetência, tempo total do curso e ano previsto de conclusão.

### 2 - Adicionar aluno

Permite cadastrar um novo aluno informando:

* Nome
* Idade
* Nota 1
* Nota 2
* Ano de entrada
* Nota de recuperação, caso exista

O sistema valida notas entre 0 e 10, idade entre 1 e 120 anos e ano de entrada dentro de um intervalo válido.

### 3 - Pesquisar alunos por nome ou característica

Permite pesquisar alunos por nome ou por características, como:

```text
aprovados
reprovados
adultos
jovens
idosos
```

Essa opção exibe um resumo com nome, média, situação acadêmica e faixa etária.

### 4 - Buscar relatório individual por nome

Permite buscar um aluno específico pelo nome e exibir o relatório completo desse aluno.

### 5 - Estatísticas da turma

Exibe informações gerais da turma, como:

* Total de alunos
* Quantidade de aprovados
* Quantidade de reprovados
* Média geral da turma
* Melhor aluno

### 6 - Sair

Encerra a execução do programa.

## Como executar os testes

Os testes unitários estão no arquivo `test_aluno.py`.

Para executar os testes, use o comando:

```bash
python -m unittest test_aluno.py
```

Ou, dependendo do sistema:

```bash
python3 -m unittest test_aluno.py
```

## Testes implementados

O arquivo de testes verifica os principais comportamentos da classe `Aluno`, incluindo:

* Cálculo da média inicial
* Cálculo da média final sem recuperação
* Cálculo da média final com recuperação
* Situação de aluno aprovado
* Situação de aluno em recuperação
* Situação de aluno aprovado após recuperação
* Situação de aluno reprovado
* Classificação de faixa etária jovem
* Classificação de faixa etária adulto
* Classificação de faixa etária idoso
* Verificação de repetência
* Previsão de conclusão do curso

## Boas práticas aplicadas

Durante o desenvolvimento foram aplicadas boas práticas de programação, como:

* Uso de nomes em `snake_case`
* Organização do sistema em funções e métodos
* Uso de docstrings
* Separação de responsabilidades
* Validação de entradas
* Tratamento de erros com `try` e `except`
* Uso de classe para organizar os dados dos alunos
* Uso de lista para armazenar a turma
* Proteção da execução principal com `if __name__ == "__main__"`
* Criação de testes unitários com `unittest`

## Observação sobre a estrutura de dados

Embora fosse possível resolver a atividade utilizando uma lista de dicionários, optei por utilizar uma lista de objetos da classe `Aluno`.

Essa escolha foi feita porque o sistema passou a trabalhar com mais informações e regras relacionadas a cada estudante, como cálculo de média, recuperação, situação acadêmica, faixa etária, repetência e previsão de conclusão do curso.

Com a classe `Aluno`, os dados e comportamentos de cada estudante ficam mais organizados, facilitando a manutenção, a leitura do código e a expansão futura do sistema.

## Autor

Samuel dos Santos Escoval

Projeto desenvolvido como atividade prática de programação em Python.
