import unittest
from main import Aluno


class TestAluno(unittest.TestCase):

    def test_calcular_media(self):
        aluno = Aluno("Teste", 20, 8, 6, 2024)
        self.assertEqual(aluno.calcular_media(), 7.0)

    def test_calcular_media_final_sem_recuperacao(self):
        aluno = Aluno("Teste", 20, 8, 6, 2024)
        self.assertEqual(aluno.calcular_media_final(), 7.0)

    def test_calcular_media_final_com_recuperacao(self):
        aluno = Aluno("Teste", 20, 6, 6, 2024, 8)
        self.assertEqual(aluno.calcular_media_final(), 7.0)

    def test_aluno_aprovado(self):
        aluno = Aluno("Teste", 20, 8, 7, 2024)
        self.assertEqual(aluno.verificar_situacao(), "Aprovado")

    def test_aluno_em_recuperacao(self):
        aluno = Aluno("Teste", 20, 5, 6, 2024)
        self.assertEqual(aluno.verificar_situacao(), "Em recuperação")

    def test_aluno_aprovado_apos_recuperacao(self):
        aluno = Aluno("Teste", 20, 6, 6, 2024, 8)
        self.assertEqual(aluno.verificar_situacao(), "Aprovado após recuperação")

    def test_aluno_reprovado(self):
        aluno = Aluno("Teste", 20, 2, 3, 2024, 4)
        self.assertEqual(aluno.verificar_situacao(), "Reprovado")

    def test_faixa_etaria_jovem(self):
        aluno = Aluno("Teste", 17, 8, 8, 2024)
        self.assertEqual(aluno.faixa_etaria(), "Jovem")

    def test_faixa_etaria_adulto(self):
        aluno = Aluno("Teste", 30, 8, 8, 2024)
        self.assertEqual(aluno.faixa_etaria(), "Adulto")

    def test_faixa_etaria_idoso(self):
        aluno = Aluno("Teste", 65, 8, 8, 2024)
        self.assertEqual(aluno.faixa_etaria(), "Idoso")

    def test_verificar_repetencia_true(self):
        aluno = Aluno("Teste", 20, 2, 3, 2024, 4)
        self.assertTrue(aluno.verificar_repetencia())

    def test_verificar_repetencia_false(self):
        aluno = Aluno("Teste", 20, 8, 7, 2024)
        self.assertFalse(aluno.verificar_repetencia())

    def test_conclusao_curso_sem_repetencia(self):
        aluno = Aluno("Teste", 20, 8, 7, 2024)
        self.assertEqual(aluno.conclusao_curso(), (2, 2026))

    def test_conclusao_curso_com_repetencia(self):
        aluno = Aluno("Teste", 20, 2, 3, 2024, 4)
        self.assertEqual(aluno.conclusao_curso(), (3, 2027))


if __name__ == "__main__":
    unittest.main()