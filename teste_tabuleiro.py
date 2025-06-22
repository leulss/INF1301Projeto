import unittest
from tabuleiro import insere_lance, reinicia_tabuleiro, retorna_tabuleiro

class TestTabuleiro(unittest.TestCase):

    def setUp(self):
        reinicia_tabuleiro()

    def test_insere_lance_valido(self):
        print("Caso de Teste 01 - Inserção válida")
        resultado = insere_lance(1, 1, 0)
        self.assertEqual(resultado, 1)

    def test_insere_lance_em_posicao_ocupada(self):
        print("Caso de Teste 02 - Inserção em posição ocupada")
        insere_lance(1, 1, 0)
        resultado = insere_lance(1, 1, 1)
        self.assertEqual(resultado, 0)

    def test_insere_lance_em_posicao_invalida(self):
        print("Caso de Teste 03 - Inserção em posição inválida")
        resultado = insere_lance(-1, 2, 0)
        self.assertEqual(resultado, 0)

    def test_reinicia_tabuleiro(self):
        print("Caso de Teste 04 - Reiniciar tabuleiro")
        insere_lance(0, 0, 0)
        reinicia_tabuleiro()
        esperado = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.assertEqual(retorna_tabuleiro(), esperado)

    def test_retorna_tabuleiro_eh_copia(self):
        print("Caso de Teste 05 - Garantir que retorna cópia")
        insere_lance(0, 0, 0)
        copia1 = retorna_tabuleiro()
        copia1[0][0] = 99
        copia2 = retorna_tabuleiro()
        self.assertNotEqual(copia2[0][0], 99)
        self.assertEqual(copia2[0][0], 0)

if __name__ == '__main__':
    unittest.main()
