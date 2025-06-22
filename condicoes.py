__all__ = ["partida_acabou"]

"""
    Nome: partida_acabou(matriz)

    Objetivo:
        Verificar o estado da partida (vitória de X, vitória de O, empate ou jogo em andamento).

    Acoplamento:
        - parâmetro: matriz — lista de listas 3x3 representando o tabuleiro.
        - retorno: int — código do status da partida (-1, 0, 1 ou 2)

    Condições de Acoplamento:
        AE: matriz 3x3 contendo valores -1 (vazio), 0 (X) ou 1 (O).
        AS: retorno coerente com o estado da partida.

    Descrição:
        1) Verifica todas as linhas, colunas e diagonais por vitória.
        2) Caso nenhuma vitória seja detectada, verifica se ainda há posições vazias.
        3) Se não houver vazios, retorna 2 (empate); senão, retorna -1 (em andamento).

    Hipóteses:
        - A matriz representa um estado válido de tabuleiro.

    Restrições:
        - A matriz deve ser 3x3; a função não valida isso.
"""
def partida_acabou(m):
    # Verifica linhas
    for i in range(3):
        if m[i][0] == m[i][1] == m[i][2] and m[i][0] != -1:
            return m[i][0]

    # Verifica colunas
    for j in range(3):
        if m[0][j] == m[1][j] == m[2][j] and m[0][j] != -1:
            return m[0][j]

    # Verifica diagonais
    if m[0][0] == m[1][1] == m[2][2] and m[0][0] != -1:
        return m[0][0]
    if m[0][2] == m[1][1] == m[2][0] and m[0][2] != -1:
        return m[0][2]

    # Verifica empate (se não há espaços livres)
    for linha in m:
        if -1 in linha:
            return -1

    return 2
