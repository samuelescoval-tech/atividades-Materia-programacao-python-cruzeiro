from datetime import datetime


class Aluno:
    """
    Representa um aluno com dados pessoais, notas e informações do curso.
    """

    def __init__(self, nome, idade, nota1, nota2, ano_entrada, nota_recuperacao=None):
        self.nome = nome
        self.idade = idade
        self.nota1 = nota1
        self.nota2 = nota2
        self.ano_entrada = ano_entrada
        self.nota_recuperacao = nota_recuperacao

    def calcular_media(self):
        """
        Calcula a média inicial do aluno.

        Returns:
            float: Média aritmética das duas notas.
        """
        return (self.nota1 + self.nota2) / 2

    def calcular_media_final(self):
        """
        Calcula a média final considerando recuperação, se houver.

        Returns:
            float: Média final do aluno.
        """
        media = self.calcular_media()

        if media >= 7:
            return media

        if self.nota_recuperacao is None:
            return media

        return (media + self.nota_recuperacao) / 2

    def verificar_situacao(self):
        """
        Verifica a situação acadêmica do aluno.

        Returns:
            str: Situação acadêmica do aluno.
        """
        media = self.calcular_media()
        media_final = self.calcular_media_final()

        if media >= 7:
            return "Aprovado"

        if self.nota_recuperacao is None:
            return "Em recuperação"

        if media_final >= 7:
            return "Aprovado após recuperação"

        return "Reprovado"

    def faixa_etaria(self):
        """
        Classifica o aluno por faixa etária.

        Returns:
            str: Jovem, Adulto ou Idoso.
        """
        if self.idade < 18:
            return "Jovem"

        if self.idade < 60:
            return "Adulto"

        return "Idoso"

    def verificar_repetencia(self):
        """
        Verifica se o aluno repetiu a matéria.

        Returns:
            bool: True se o aluno foi reprovado, False caso contrário.
        """
        return self.verificar_situacao() == "Reprovado"

    def conclusao_curso(self):
        """
        Calcula o tempo total e o ano previsto de conclusão do curso.

        Returns:
            tuple: Tempo total do curso e ano previsto de conclusão.
        """
        tempo_total = 2

        if self.verificar_repetencia():
            tempo_total += 1

        ano_conclusao = self.ano_entrada + tempo_total
        return tempo_total, ano_conclusao

    def resumo(self):
        """
        Mostra um resumo simples do aluno.
        """
        media = self.calcular_media()
        situacao = self.verificar_situacao()
        faixa = self.faixa_etaria()

        print(f"{self.nome} | Média: {media:.2f} | {situacao} | {faixa}")

    def mostrar_relatorio(self):
        """
        Mostra o relatório completo do aluno.
        """
        media = self.calcular_media()
        media_final = self.calcular_media_final()
        situacao = self.verificar_situacao()
        faixa = self.faixa_etaria()
        repetiu = self.verificar_repetencia()
        tempo_total, ano_conclusao = self.conclusao_curso()

        print("\n===== RELATÓRIO DO ALUNO =====")
        print(f"Aluno: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Faixa etária: {faixa}")
        print(f"Nota 1: {self.nota1}")
        print(f"Nota 2: {self.nota2}")
        print(f"Média inicial: {media:.2f}")
        print(f"Nota recuperação: {self.nota_recuperacao}")
        print(f"Média final: {media_final:.2f}")
        print(f"Situação: {situacao}")
        print(f"Repetiu: {'Sim' if repetiu else 'Não'}")
        print(f"Tempo total do curso: {tempo_total} anos")
        print(f"Ano previsto de conclusão: {ano_conclusao}")


def ler_nota(mensagem):
    """
    Lê e valida uma nota entre 0 e 10.

    Args:
        mensagem (str): Mensagem exibida ao usuário.

    Returns:
        float: Nota válida entre 0 e 10.
    """
    while True:
        try:
            nota = float(input(mensagem))

            if 0 <= nota <= 10:
                return nota

            print("Nota inválida. Digite uma nota entre 0 e 10.")

        except ValueError:
            print("Entrada inválida. Digite apenas números.")


def ler_idade():
    """
    Lê e valida a idade do aluno.

    Returns:
        int: Idade válida entre 1 e 120.
    """
    while True:
        try:
            idade = int(input("Idade: "))

            if 0 < idade <= 120:
                return idade

            print("Idade inválida. Digite uma idade entre 1 e 120.")

        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")


def ler_ano_entrada():
    """
    Lê e valida o ano de entrada do aluno.

    Returns:
        int: Ano de entrada válido.
    """
    ano_atual = datetime.now().year

    while True:
        try:
            ano = int(input("Ano de entrada: "))

            if 1900 <= ano <= ano_atual:
                return ano

            print(f"Ano inválido. Digite um ano entre 1900 e {ano_atual}.")

        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")


def pesquisar_alunos(turma):
    """
    Pesquisa alunos por característica ou nome.

    Args:
        turma (list): Lista de objetos Aluno.
    """
    filtro = input(
        "Digite uma característica ou nome "
        "(aprovados, reprovados, adultos, jovens, idosos): "
    ).lower()

    print("\n===== RESULTADO DA PESQUISA =====")

    encontrou = False

    for aluno in turma:
        situacao = aluno.verificar_situacao().lower()
        faixa = aluno.faixa_etaria().lower()
        nome = aluno.nome.lower()

        if filtro == "aprovados" and "aprovado" in situacao:
            aluno.resumo()
            encontrou = True

        elif filtro == "reprovados" and situacao == "reprovado":
            aluno.resumo()
            encontrou = True

        elif filtro == "adultos" and faixa == "adulto":
            aluno.resumo()
            encontrou = True

        elif filtro == "jovens" and faixa == "jovem":
            aluno.resumo()
            encontrou = True

        elif filtro == "idosos" and faixa == "idoso":
            aluno.resumo()
            encontrou = True

        elif filtro in nome:
            aluno.resumo()
            encontrou = True

    if not encontrou:
        print("Nenhum aluno encontrado.")


def buscar_aluno_por_nome(turma):
    """
    Busca um aluno pelo nome e exibe o relatório completo.

    Args:
        turma (list): Lista de objetos Aluno.
    """
    nome_busca = input("Digite o nome do aluno: ").lower()

    encontrou = False

    for aluno in turma:
        if nome_busca in aluno.nome.lower():
            aluno.mostrar_relatorio()
            encontrou = True

    if not encontrou:
        print("Aluno não encontrado.")


def estatisticas_turma(turma):
    """
    Mostra estatísticas gerais da turma.

    Args:
        turma (list): Lista de objetos Aluno.
    """
    if not turma:
        print("A turma está vazia.")
        return

    total = len(turma)
    aprovados = 0
    reprovados = 0
    soma_medias = 0

    melhor_aluno = turma[0]

    for aluno in turma:
        situacao = aluno.verificar_situacao()
        media = aluno.calcular_media_final()

        soma_medias += media

        if "Aprovado" in situacao:
            aprovados += 1

        if situacao == "Reprovado":
            reprovados += 1

        if media > melhor_aluno.calcular_media_final():
            melhor_aluno = aluno

    media_geral = soma_medias / total

    print("\n===== ESTATÍSTICAS DA TURMA =====")
    print(f"Total de alunos: {total}")
    print(f"Aprovados: {aprovados}")
    print(f"Reprovados: {reprovados}")
    print(f"Média geral da turma: {media_geral:.2f}")
    print(f"Melhor aluno: {melhor_aluno.nome}")


def gerar_relatorio(alunos):
    """
    Gera o relatório completo de todos os alunos.

    Args:
        alunos (list): Lista de objetos Aluno.
    """
    for aluno in alunos:
        aluno.mostrar_relatorio()


turma = [
    Aluno("Alana", 20, 4, 5, 2020, 8),
    Aluno("Samuel", 17, 8, 7, 2024),
    Aluno("Carlos", 65, 3, 4, 2021, 5),
    Aluno("Maria", 30, 5, 1, 2026, 9),
    Aluno("Fernanda", 22, 10, 9, 2025),
    Aluno("Lucas", 16, 2, 3, 2023, 4),
    Aluno("Juliana", 45, 6, 6, 2022, 10),
]


def main():
    """
    Executa o menu principal do sistema escolar.
    """
    while True:
        print("\n===== SISTEMA ESCOLAR =====")
        print("1 - Ver relatório de todos os alunos")
        print("2 - Adicionar aluno")
        print("3 - Pesquisar alunos por nome ou característica")
        print("4 - Buscar relatório individual por nome")
        print("5 - Estatísticas da turma")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            gerar_relatorio(turma)

        elif opcao == "2":
            nome = input("Nome: ")
            idade = ler_idade()
            nota1 = ler_nota("Nota 1: ")
            nota2 = ler_nota("Nota 2: ")
            ano_entrada = ler_ano_entrada()

            recuperacao = input("Fez recuperação? (s/n): ").lower()

            if recuperacao == "s":
                nota_recuperacao = ler_nota("Nota recuperação: ")
            else:
                nota_recuperacao = None

            novo_aluno = Aluno(
                nome,
                idade,
                nota1,
                nota2,
                ano_entrada,
                nota_recuperacao
            )

            turma.append(novo_aluno)
            print("Aluno cadastrado com sucesso!")

        elif opcao == "3":
            pesquisar_alunos(turma)

        elif opcao == "4":
            buscar_aluno_por_nome(turma)

        elif opcao == "5":
            estatisticas_turma(turma)

        elif opcao == "6":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
