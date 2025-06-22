__all__ = ["insere_lance", "consulta_tabuleiro", "partida_acabou"]

from tabuleiro import insere_lance as tabuleiro_insere, retorna_tabuleiro
from condicoes import partida_acabou as verifica_fim
from placar import retorna_placar, atualiza_placar as somar_vitoria

"""
    Nome: insere_lance(i, j, mark)

    Objetivo:
        Inserir um lance no tabuleiro, verificando validade por meio do módulo tabuleiro.

    Acoplamento:
        - parâmetros: i (int), j (int), mark (int)
        - retorno: int — 1 se jogada foi bem-sucedida; 0 caso contrário.

    Condições de Acoplamento:
        AE: posição dentro dos limites e livre.
        AS: valor inserido no tabuleiro, se válido.

    Descrição:
        1) Encaminha a jogada para a função insere_lance do módulo tabuleiro.
        2) Retorna o resultado.

    Hipóteses:
        - `mark` deve ser 0 (X) ou 1 (O).
"""
def insere_lance(i, j, mark):
    return tabuleiro_insere(i, j, mark)

"""
    Nome: consulta_placar(modo)

    Objetivo:
        Consultar o placar atual entre os jogadores do tabuleiro da partida em andamento.

    Acoplamento:
        - parâmetros: modo (int)
        - retorno: {'Jogador1':N, 'Jogador2':M} se modo for contra jogador; {'Jogador1':N, 'IA':M} se modo for IA

    Condições de Acoplamento:
        AE: recebe o modo de jogo ( 1 == Jogador2 ; 2 == IA).
        AS: retorna cópia segura do placar no formato {'Jogador1':N, 'Jogador2':M} ou {'Jogador1':N, 'IA':M} 
        onde N e M são inteiros e a segunda chave do dicionário varia de acordo com o modo escolhido.

    Descrição:
        1) Requisita o placar.
        2) Retorna o placar só com as chaves ativas.

    Hipóteses:
        - Parâmetro de entrada é validado previamente como 1 ou 2.
"""
def consulta_placar(modo):
    placar = retorna_placar()
    if modo == 1:
        key = "IA"
    elif modo == 2:
        key = "Jogador2"
    placar.pop(key)
    return placar

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
        1) Chama função de acesso do módulo placar, passando o jogador que venceu

    Hipóteses:
        - Parâmetro de entrada é validado previamente como 0, 1 ou 2.
        - Jogador passado realmente venceu a partida.
"""
def atualiza_placar(player):
    somar_vitoria(player)

"""
    Nome: consulta_tabuleiro()

    Objetivo:
        Consultar o estado atual do tabuleiro da partida em andamento.

    Acoplamento:
        - retorno: matriz 3x3 com os valores do tabuleiro.

    Condições de Acoplamento:
        AE: chamada sem parâmetros.
        AS: retorna cópia segura da matriz.

    Descrição:
        1) .
        2) Retorna a cópia obtida.

    Hipóteses:
        - Usado para exibir o atual recorde dos jogadores.
"""
def consulta_tabuleiro():
    return retorna_tabuleiro()

"""
    Nome: partida_acabou()

    Objetivo:
        Verificar se a partida terminou com vitória, empate ou ainda está em andamento.

    Acoplamento:
        - retorno: int — -1 (não acabou), 0 (X venceu), 1 (O venceu), 2 (empate)

    Condições de Acoplamento:
        AE: chamada sem parâmetros.
        AS: retorno do status da partida.

    Descrição:
        1) Consulta o tabuleiro atual.
        2) Encaminha a matriz para o módulo de condições.
        3) Retorna o resultado da verificação.

    Hipóteses:
        - Verificado após cada jogada.

    Restrições:
        - Deve retornar valor coerente com as regras do jogo.
"""
def partida_acabou():
    matriz = retorna_tabuleiro()
    return verifica_fim(matriz)
