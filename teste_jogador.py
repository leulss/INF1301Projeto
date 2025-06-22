import unittest
from unittest.mock import patch
from jogador import escolher_lance

class TestJogador(unittest.TestCase):
    def test_escolher_lance_valido(self):
        print("Caso de Teste - Jogador insere (1,2)")
        with patch('builtins.input', side_effect=['1', '2']):
            resultado = escolher_lance()
            self.assertEqual(resultado, (1, 2))

    def test_escolher_lance_invalido_e_corrige(self):
        print("Caso de Teste - Jogador insere inválido (3,3), depois (0,0)")
        with patch('builtins.input', side_effect=['3', '3', '0', '0']):
            resultado = escolher_lance()
            self.assertEqual(resultado, (0, 0))

    def test_escolher_lance_valor_nao_inteiro(self):
        print("Caso de Teste - Jogador insere texto, depois valor válido")
        with patch('builtins.input', side_effect=['a', 'b', '1', '1']):
            resultado = escolher_lance()
            self.assertEqual(resultado, (1, 1))

if __name__ == '__main__':

    unittest.main()