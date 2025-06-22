import unittest
from condicoes import partida_acabou

class TestCondicoes(unittest.TestCase):

    def test_vitoria_x_horizontal(self):
        print("Caso de Teste 01 - X vence na horizontal")
        matriz = [
            [0, 0, 0],
            [1, 1, -1],
            [-1, 1, 1]
        ]
        self.assertEqual(partida_acabou(matriz), 0)

    def test_vitoria_o_horizontal(self):
        print("Caso de Teste 02 - O vence na horizontal")
        matriz = [
            [1, 1, 1],
            [-1, 0, -1],
            [-1, 0, -1]
        ]
        self.assertEqual(partida_acabou(matriz), 1)

    def test_vitoria_x_vertical(self):
        print("Caso de Teste 03 - X vence na vertical")
        matriz = [
            [0, 1, -1],
            [0, 1, -1],
            [0, -1, 1]
        ]
        self.assertEqual(partida_acabou(matriz), 0)

    def test_vitoria_o_vertical(self):
        print("Caso de Teste 04 - O vence na vertical")
        matriz = [
            [1, 0, 0],
            [1, 0, 0],
            [1, -1, 1]
        ]
        self.assertEqual(partida_acabou(matriz), 1)

    def test_vitoria_x_diagonal(self):
        print("Caso de Teste 05 - X vence na diagonal")
        matriz = [
            [1, 1, 0],
            [-1, 0, -1],
            [0, -1, 1]
        ]
        self.assertEqual(partida_acabou(matriz), 0)

    def test_vitoria_o_diagonal(self):
        print("Caso de Teste 06 - O vence na diagonal")
        matriz = [
            [0, 0, 1],
            [-1, 1, 0],
            [1, -1, 0]
        ]
        self.assertEqual(partida_acabou(matriz), 1)

def test_empate(self):
    print("Caso de Teste 07 - Empate")
    matriz = [
        [0, 1, 1],
        [1, 0, 0],
        [1, 0, 1]
    ]
    self.assertEqual(partida_acabou(matriz), 2)

def test_partida_em_andamento(self):
    print("Caso de Teste 08 - Partida em andamento")
    matriz = [
        [0, -1, 1],
        [-1, 0, 0],
        [1, -1, 1]
    ]
    self.assertEqual(partida_acabou(matriz), -1)


if __name__ == '__main__':
    unittest.main()
