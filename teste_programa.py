import unittest
from io import StringIO
import sys
from programa import exibe_tabuleiro

class TestPrograma(unittest.TestCase):
    def test_exibe_tabuleiro_vazio(self):
        print("Caso de Teste - Exibe tabuleiro vazio")
        matriz = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        esperado = (
            "\nTabuleiro:\n"
            "  |   |  \n"
            "---------\n"
            "  |   |  \n"
            "---------\n"
            "  |   |  \n"
            "---------\n"
        )

        captured_output = StringIO()
        sys.stdout = captured_output
        exibe_tabuleiro(matriz)
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip().replace('\n', ''), esperado.strip().replace('\n', ''))

if __name__ == '__main__':
    unittest.main()