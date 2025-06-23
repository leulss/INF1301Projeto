# test_placar.py

import unittest
import json
import importlib
from unittest.mock import patch, mock_open

import placar  # importa o módulo que vamos testar

class TestPlacar(unittest.TestCase):
    def setUp(self):
        self.initial_scores = {"Jogador1": 0, "Jogador2": 0, "IA": 0}
        self.mock_file = mock_open(read_data=json.dumps(self.initial_scores))
        self.patcher_open = patch('placar.open', self.mock_file)
        self.patcher_load = patch('placar.json.load', return_value=self.initial_scores.copy())
        self.patcher_open.start()
        self.patcher_load.start()
        importlib.reload(placar)

    def tearDown(self):
        patch.stopall()

    @patch('placar.json.dump')
    def test_atualiza_jogador1(self, mock_dump):
        print("Teste 01 - atualiza_placar: Jogador1 (player=0)")
        placar.atualiza_placar(0)
        expected = {"Jogador1": 1, "Jogador2": 0, "IA": 0}
        handle = self.mock_file()
        mock_dump.assert_called_once_with(expected, handle)

    @patch('placar.json.dump')
    def test_atualiza_jogador2(self, mock_dump):
        print("Teste 02 - atualiza_placar: Jogador2 (player=1)")
        placar.atualiza_placar(1)
        expected = {"Jogador1": 0, "Jogador2": 1, "IA": 0}
        handle = self.mock_file()
        mock_dump.assert_called_once_with(expected, handle)

    @patch('placar.json.dump')
    def test_atualiza_ia(self, mock_dump):
        print("Teste 03 - atualiza_placar: IA (player=2)")
        placar.atualiza_placar(2)
        expected = {"Jogador1": 0, "Jogador2": 0, "IA": 1}
        handle = self.mock_file()
        mock_dump.assert_called_once_with(expected, handle)

    def test_retorna_placar_safe_copy(self):
        print("Teste 04 - retorna_placar: cópia segura")
        importlib.reload(placar)
        copia = placar.retorna_placar()
        self.assertEqual(copia, self.initial_scores)
        copia['Jogador1'] = 999
        self.assertNotEqual(placar.placar['Jogador1'], 999)
        self.assertIsNot(copia, placar.placar)

if __name__ == '__main__':
    unittest.main()