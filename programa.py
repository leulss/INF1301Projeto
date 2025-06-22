from tabuleiro import reinicia_tabuleiro, insere_lance, retorna_tabuleiro
from partida import partida_acabou, consulta_placar, atualiza_placar
from jogador import escolher_lance
from maquina import escolher_lance as escolher_lance_maquina

"""
    Nome: exibe_tabuleiro(matriz)

    Objetivo:
        Apresentar o tabuleiro atual no terminal de forma legível.

    Acoplamento:
        - parâmetro: matriz — lista de listas representando o tabuleiro.

    Condições de Acoplamento:
        AE: matriz 3x3 contendo -1, 0 ou 1.
        AS: impressão formatada no terminal.

    Descrição:
        1) Itera pelas linhas da matriz.
        2) Converte os valores em símbolos visuais.
        3) Exibe a matriz formatada com separadores.

    Hipóteses:
        - Apenas valores -1, 0 ou 1 estão presentes.

    Restrições:
        - Exclusivamente para visualização em modo texto.
"""
def exibe_tabuleiro(matriz):
    print("\nTabuleiro:")
    for linha in matriz:
        print(" | ".join([' ' if x == -1 else 'X' if x == 0 else 'O' for x in linha]))
        print("-" * 9)

"""
    Nome: main()

    Objetivo:
        Controlar o fluxo geral do jogo da velha (turnos, jogadas, fim de jogo, reinício).

    Acoplamento:
        - Entrada via input()
        - Uso de funções dos módulos: tabuleiro, jogador, máquina, partida.

    Condições de Acoplamento:
        AE: chamada sem parâmetros.
        AS: jogo executado até fim da interação do usuário.

    Descrição:
        1) Pergunta o modo de jogo.
        2) Alterna entre jogador e máquina.
        3) Coleta jogadas e atualiza o tabuleiro.
        4) Verifica vitória ou empate.
        5) Permite novo jogo.

    Hipóteses:
        - Jogadores entendem as regras do jogo da velha.

    Restrições:
        - Executado apenas via terminal.
        - Não persiste histórico entre execuções.
"""
def main():
    print("Bem-vindo ao Jogo da Velha!")
    while True:
        try:
            modo = int(input("Digite 1 para jogar contra outro jogador ou 2 para jogar contra a máquina: ").strip())
            if modo == 2:
                vs_maquina = True
                break
            elif modo == 1:
                vs_maquina = False
                break
        except:
            pass
        print("Digite uma opção válida")

    while True:
        placar = consulta_placar(modo)
        oponente = "IA" if vs_maquina else "Jogador2"
        print(f"Vitórias Jogador1: {str(placar['Jogador1'])} \nVitórias {oponente}: {str(placar[oponente])}")
        reinicia_tabuleiro()
        jogador_atual = 0  # 0 = X, 1 = O

        while True:
            exibe_tabuleiro(retorna_tabuleiro())
            print(f"Vez do {'Jogador' if not vs_maquina or jogador_atual == 0 else 'Máquina'} {['X','O'][jogador_atual]}")

            if vs_maquina and jogador_atual == 1:
                i, j = escolher_lance_maquina()
            else:
                i, j = escolher_lance()

            if insere_lance(i, j, jogador_atual):
                resultado = partida_acabou()
                if resultado != -1:
                    exibe_tabuleiro(retorna_tabuleiro())
                    if resultado == 0:
                        print("Vitória do Jogador X!")
                        player = 0
                        atualiza_placar(player)
                    elif resultado == 1:
                        print("Vitória do Jogador O!")
                        if vs_maquina:
                            player = 2
                        else:
                            player = 1
                        atualiza_placar(player)
                    else:
                        print("Empate!")
                    break
                jogador_atual = 1 - jogador_atual
            else:
                print("Jogada inválida! Tente novamente.")

        novo_jogo = input("Deseja jogar novamente? (sim): ")
        if novo_jogo.strip().lower() != 'sim':
            break

if __name__ == "__main__":
    main()
