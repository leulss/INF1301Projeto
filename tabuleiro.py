__all__ = ["insere_lance", "reinicia_tabuleiro", "retorna_tabuleiro"]

from copy import deepcopy

# Encapsulamento da estrutura de dados
_tabuleiro = [[-1 for _ in range(3)] for _ in range(3)]

"""
    Nome: insere_lance(i, j, mark)

    Objetivo:
        Inserir uma marca (0 = X, 1 = O) no tabuleiro na posição especificada.

    Acoplamento:
        - parâmetros: i (int), j (int), mark (int)
        - retorno: int — 1 se inserção for bem-sucedida; 0 caso contrário.

    Condições de Acoplamento:
        AE: i e j devem estar entre 0 e 2; mark deve ser 0 ou 1.
        AS: posição modificada se válida; senão, retorna 0.

    Descrição:
        1) Verifica se i e j estão dentro do range.
        2) Verifica se a posição está livre (-1).
        3) Insere o valor mark na posição (i,j) e retorna 1; senão retorna 0.

    Hipóteses:
        - A função é chamada por turno e o controle de alternância já foi validado.

    Restrições:
        - Não pode sobrescrever uma posição já preenchida.
"""
def insere_lance(i, j, mark):
    if i not in range(3) or j not in range(3):
        return 0
    if _tabuleiro[i][j] != -1:
        return 0
    _tabuleiro[i][j] = mark
    return 1

"""
    Nome: reinicia_tabuleiro()

    Objetivo:
        Redefinir o tabuleiro para seu estado inicial, com todas as casas livres.

    Acoplamento:
        - retorno: None

    Condições de Acoplamento:
        AE: chamada sem parâmetros.
        AS: todas as posições definidas como -1.

    Descrição:
        1) Itera pelas posições da matriz e define todas como -1.

    Hipóteses:
        - Utilizada entre partidas.

    Restrições:
        - Afeta diretamente a estrutura encapsulada.
"""
def reinicia_tabuleiro():
    for i in range(3):
        for j in range(3):
            _tabuleiro[i][j] = -1

"""
    Nome: retorna_tabuleiro()

    Objetivo:
        Devolver uma cópia segura do estado atual do tabuleiro.

    Acoplamento:
        - retorno: matriz 3x3 com inteiros (-1, 0 ou 1)

    Condições de Acoplamento:
        AE: chamada sem parâmetros.
        AS: retorno de deepcopy da matriz interna.

    Descrição:
        1) Cria e retorna uma cópia profunda do tabuleiro.

    Hipóteses:
        - Chamada por funções de exibição, IA ou checagem de fim de jogo.

    Restrições:
        - O retorno não deve permitir alterar diretamente a estrutura interna.
"""
def retorna_tabuleiro():
    return deepcopy(_tabuleiro)
