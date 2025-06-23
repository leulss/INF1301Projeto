import unittest
from unittest.mock import patch
from partida import (
    insere_lance,
    consulta_tabuleiro,
    partida_acabou,
    consulta_placar,
    atualiza_placar
)
from tabuleiro import reinicia_tabuleiro

class TestPartida(unittest.TestCase):

    def setUp(self):
        reinicia_tabuleiro()

    def test_insere_lance_validos_e_invalidos(self):
        print("Caso de Teste 01 - Inserções válidas e inválidas")
        self.assertEqual(insere_lance(2, 1, 0), 1)  # Válido
        self.assertEqual(insere_lance(2, 1, 0), 0)  # Já preenchido
        self.assertEqual(insere_lance(1, 3, 1), 0)  # Fora do range
        self.assertEqual(insere_lance(0, 1, 1), 1)  # Válido

    def test_consulta_tabuleiro_vazio_e_modificado(self):
        print("Caso de Teste 02 - Consulta tabuleiro")
        reinicia_tabuleiro()
        esperado_vazio = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.assertEqual(consulta_tabuleiro(), esperado_vazio)

        insere_lance(0, 1, 1)
        esperado_modificado = [[-1, 1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.assertEqual(consulta_tabuleiro(), esperado_modificado)

    def test_partida_acabou_status(self):
        print("Caso de Teste 03 - Fim de partida")
        # Jogo em andamento
        self.assertEqual(partida_acabou(), -1)

        # Vitória de X na horizontal
        reinicia_tabuleiro()
        insere_lance(0, 0, 0)
        insere_lance(0, 1, 0)
        insere_lance(0, 2, 0)
        self.assertEqual(partida_acabou(), 0)

        # Vitória de O na vertical
        reinicia_tabuleiro()
        insere_lance(0, 1, 1)
        insere_lance(1, 1, 1)
        insere_lance(2, 1, 1)
        self.assertEqual(partida_acabou(), 1)

        # Empate (velha)
        reinicia_tabuleiro()
        jogadas = [
            (0, 0, 0), (0, 1, 1), (0, 2, 0),
            (1, 0, 1), (1, 1, 0), (1, 2, 1),
            (2, 0, 1), (2, 1, 0), (2, 2, 1),
        ]
        for i, j, mark in jogadas:
            insere_lance(i, j, mark)
        self.assertEqual(partida_acabou(), 2)

    @patch('partida.retorna_placar', return_value={"Jogador1": 5, "Jogador2": 3, "IA": 2})
    def test_consulta_placar_modo1(self, mock_retorna):
        print("Caso de Teste 04 - consulta_placar modo=1 (versus jogador)")
        # modo=1 deve remover a chave "IA"
        resultado = consulta_placar(1)
        esperado = {"Jogador1": 5, "Jogador2": 3}
        self.assertEqual(resultado, esperado)

    @patch('partida.retorna_placar', return_value={"Jogador1": 8, "Jogador2": 4, "IA": 7})
    def test_consulta_placar_modo2(self, mock_retorna):
        print("Caso de Teste 05 - consulta_placar modo=2 (versus IA)")
        # modo=2 deve remover a chave "Jogador2"
        resultado = consulta_placar(2)
        esperado = {"Jogador1": 8, "IA": 7}
        self.assertEqual(resultado, esperado)

    @patch('partida.somar_vitoria')
    def test_atualiza_placar_encapsulado(self, mock_somar):
        print("Caso de Teste 06 - atualiza_placar chama somar_vitoria")
        atualiza_placar(0)
        mock_somar.assert_called_once_with(0)

if __name__ == '__main__':
    unittest.main()