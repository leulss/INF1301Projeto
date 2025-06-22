import unittest
from maquina import escolher_lance
from tabuleiro import reinicia_tabuleiro, insere_lance
from partida import insere_lance as partida_insere
from tabuleiro import retorna_tabuleiro

class TestMaquina(unittest.TestCase):

    def setUp(self):
        reinicia_tabuleiro()

    def test_maquina_vence_quando_pode(self):
        print("Caso de Teste 01 - IA vence se puder")
        partida_insere(0, 0, 1)
        partida_insere(0, 1, 1)
        # IA deve jogar em (0,2) para vencer
        i, j = escolher_lance()
        self.assertEqual((i, j), (0, 2))

    def test_maquina_bloqueia_jogador(self):
        print("Caso de Teste 02 - IA bloqueia o jogador")
        partida_insere(1, 0, 0)
        partida_insere(1, 1, 0)
        # Jogador poderia vencer em (1,2), IA deve bloquear
        i, j = escolher_lance()
        self.assertEqual((i, j), (1, 2))

    def test_maquina_escolhe_centro(self):
        print("Caso de Teste 03 - IA escolhe o centro")
        # Tabuleiro vazio
        i, j = escolher_lance()
        self.assertEqual((i, j), (1, 1))

    def test_maquina_escolhe_canto_aleatorio(self):
        print("Caso de Teste 04 - IA escolhe canto aleatório")
        # Centro ocupado
        partida_insere(1, 1, 0)
        i, j = escolher_lance()
        self.assertIn((i, j), [(0, 0), (0, 2), (2, 0), (2, 2)])

    def test_maquina_escolhe_primeira_livre(self):
        print("Caso de Teste 05 - IA escolhe posição livre qualquer")
        # Preenche quase todo o tabuleiro
        jogadas = [
            (0, 0), (0, 1), (0, 2),
            (1, 0), (1, 1), (1, 2),
            (2, 0), (2, 1)
        ]
        for i, j in jogadas:
            partida_insere(i, j, 0)
        # Só sobra (2,2)
        i, j = escolher_lance()
        self.assertEqual((i, j), (2, 2))

if __name__ == '__main__':
    unittest.main()
