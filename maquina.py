__all__ = ["escolher_lance"]

from tabuleiro import retorna_tabuleiro
from condicoes import partida_acabou
from tabuleiro import insere_lance as testa_insere_lance
from copy import deepcopy
import random

"""
    Nome: escolher_lance()

    Objetivo:
        Escolher a melhor jogada possível para a IA, priorizando vitória, bloqueio e posicionamento estratégico.

    Acoplamento:
        - retorno: tuple — coordenadas (i, j) de uma posição ideal no tabuleiro.

    Condições de Acoplamento:
        AE: chamada sem parâmetros.
        AS: retorna uma jogada válida segundo prioridades.

    Descrição:
        1) Tenta vencer com um lance direto.
        2) Bloqueia o adversário se ele puder vencer.
        3) Escolhe o centro se livre.
        4) Escolhe aleatoriamente entre cantos livres.
        5) Escolhe a primeira posição livre como fallback.

    Hipóteses:
        - A IA sempre joga com mark = 1 (O).
"""
def escolher_lance():
    tabuleiro = retorna_tabuleiro()
    
    # 1. Tentar vencer
    pos = busca_jogada_decisiva(tabuleiro, mark=1)
    if pos:
        return pos
    
    # 2. Bloquear jogador
    pos = busca_jogada_decisiva(tabuleiro, mark=0)
    if pos:
        return pos

    # 3. Centro
    if tabuleiro[1][1] == -1:
        return (1, 1)

    # 4. Canto aleatório
    cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
    cantos_livres = [pos for pos in cantos if tabuleiro[pos[0]][pos[1]] == -1]
    if cantos_livres:
        return random.choice(cantos_livres)

    # 5. Primeira posição livre
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == -1:
                return (i, j)
    
    return (-1, -1)  # fallback

"""
    Nome: busca_jogada_decisiva(tabuleiro, mark)

    Objetivo:
        Verificar se há alguma jogada que garanta vitória imediata (ou bloqueie o oponente).

    Acoplamento:
        - parâmetros: tabuleiro (matriz), mark (0 ou 1)
        - retorno: tuple (i,j) se jogada decisiva existir, senão None

    Descrição:
        1) Percorre todas as posições livres.
        2) Simula a jogada.
        3) Verifica se venceria a partida.
"""
def busca_jogada_decisiva(tabuleiro, mark):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == -1:
                copia = deepcopy(tabuleiro)
                copia[i][j] = mark
                if partida_acabou(copia) == mark:
                    return (i, j)
    return None
