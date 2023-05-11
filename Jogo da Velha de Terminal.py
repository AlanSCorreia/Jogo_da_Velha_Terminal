class Tabuleiro:
    def __init__(self):
        self.linhas_colunas = [[' ' for _ in range(3)] for _ in range(3)]

    def desenhar(self):
        pos = self.linhas_colunas
        print("-" * 15)
        print(f" {pos[0][0]}  |  {pos[0][1]}  |  {pos[0][2]}")
        print("--- | --- | ---")
        print(f" {pos[1][0]}  |  {pos[1][1]}  |  {pos[1][2]}")
        print("--- | --- | ---")
        print(f" {pos[2][0]}  |  {pos[2][1]}  |  {pos[2][2]}")
        print("-" * 15)
    
    def entrada_jogador(self, simbolo):

        while True:
            linha, coluna, x = ' ', ' ', "Jogue em uma posição vazia!!"

            try:
                while linha not in range(1, 4):
                    linha = int(input("Em qual linha deseja jogar [1, 2 ou 3]: "))
                    if linha not in range(1, 4):
                        print("Essa não foi uma escolha válida. Tente denovo!")

                while coluna not in range(1, 4):
                    coluna = int(input("Em qual coluna deseja jogar [1, 2 ou 3]: "))
                    if coluna not in range(1, 4):
                        print("Essa não foi uma escolha válida. Tente denovo!")

                if self.linhas_colunas[linha - 1][coluna - 1] == ' ':
                    self.linhas_colunas[linha - 1][coluna - 1] = simbolo
                    break
                else:
                    print("-" * len(x))
                    print(x)
                    print("-" * len(x))
            except ValueError:
                print("Escolha um numero de 1 a 3. Comece novamente!\n")

    def checar_vencedor(self, simbolo):
        tab = self.linhas_colunas
        venceu = f"\nJogador do simbolo '{simbolo}' venceu!!"

        # Checando o tabuleiro
        for x in range(3):

            # Na vertical
            if tab[x][0] == tab[x][1] == tab[x][2] == simbolo:
                print(venceu)
                return True

            # Na horizontal
            elif tab[0][x] == tab[1][x] == tab[2][x] == simbolo:
                print(venceu)
                return True

        # Nas Diagonais
        if tab[0][0] == tab[1][1] == tab[2][2] == simbolo:
            print(venceu)
            return True

        elif tab[2][0] == tab[1][1] == tab[0][2] == simbolo:
            print(venceu)
            return True


def main():
    tabuleiro = Tabuleiro()
    empate = "EMPATE ! ! !"

    for x in range(9):

        if vez(x):
            jogador = "X"
        else:
            jogador = "O"

        tabuleiro.desenhar()
        tabuleiro.entrada_jogador(jogador)
        if tabuleiro.checar_vencedor(jogador):
            tabuleiro.desenhar()
            return
        else:
            continue

    # Empate
    tabuleiro.desenhar()
    print("-" * len(empate))
    print(empate)
    print("-" * len(empate))


def vez(cont):
    if cont % 2 == 0: return True
    else: return False


game_loop = True


while game_loop:
    main()
    pergunta = input("Deseja jogar novamente? [ s / n ] ")[0].lower()
    match pergunta:
        case "s":
            continue
        case "n":
            print("Fim de jogo.")
            game_loop = False
