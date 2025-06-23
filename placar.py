import json
from copy import deepcopy

__all__ = ["atualiza_placar", "retorna_placar"]

with open('placar.json', 'r') as file:
    placar = json.load(file)

"""
    Nome: retorna_placar()

    Objetivo:
        Retorna o placar atual entre os jogadores.

    Acoplamento:
        - retorno: {'Jogador1':N, 'Jogador2':M, 'IA':K} onde N, M, K são inteiros

    Condições de Acoplamento:
        AE: chamada sem parâmetros.
        AS: retorna cópia segura do placar no formato {'Jogador1':N, 'Jogador2':M, 'IA':K} onde N, M, K são inteiros.

    Descrição:
        1) Faz cópia do placar atual.
        2) Retorna a cópia.

    Hipóteses:
        - Parâmetro de entrada é validado previamente como 1 ou 2.
"""
def retorna_placar():
    return deepcopy(placar)

"""
    Nome: atualiza_placar(player)

    Objetivo:
        Atualizar o placar atual.

    Acoplamento:
        - parâmetros: player (int)

    Condições de Acoplamento:
        AE: recebe um inteiro indicando qual jogador venceu a partida ( 1 == Jogador1 ; 2 == Jogador2 ; 3 == IA).
        AS: retorna void

    Descrição:
        1) Atualize a variável local com a chave vencedora da partida.
        2) Altera o arquivo placar.json.

    Hipóteses:
        - Parâmetro de entrada é validado previamente como 0, 1 ou 2.
        - Jogador passado realmente venceu a partida.
"""
def atualiza_placar(player):
    if player == 0:
        key = "Jogador1"
    elif player == 1:
        key = "Jogador2"
    elif player == 2:
        key = "IA"
    placar[key] += 1
    with open('placar.json', 'w') as file:
        json.dump(placar, file)
