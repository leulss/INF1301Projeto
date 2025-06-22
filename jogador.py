_all_ = ["escolher_lance"]

"""
    Nome: escolher_lance()

    Objetivo:
        Coletar uma jogada do jogador humano, garantindo que esteja dentro do intervalo válido do tabuleiro.

    Acoplamento:
        - retorno: tuple — par (i, j) com coordenadas válidas da jogada.

    Condições de Acoplamento:
        AE: chamada sem parâmetros.
        AS: devolve um par de inteiros entre 0 e 2.

    Descrição:
        1) Solicita linha e coluna via input().
        2) Valida se ambos estão entre 0 e 2.
        3) Retorna a tupla (i, j) se válidos; repete se inválido.

    Hipóteses:
        - Executada apenas durante o turno de um jogador humano.
    
    Restrições:
        - Função bloqueante: espera a entrada do usuário.
"""
def escolher_lance():
    while True:
        try:
            i = int(input("Informe a linha (0 a 2): "))
            j = int(input("Informe a coluna (0 a 2): "))
            if 0 <= i <= 2 and 0 <= j <= 2:
                return (i, j)
            else:
                print("Coordenadas inválidas. Devem estar entre 0 e 2.")
        except ValueError:
            print("Entrada inválida. Digite números inteiros.")