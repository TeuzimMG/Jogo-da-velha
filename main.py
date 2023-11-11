import os



class Tabuleiro():
    

    def __init__(self) -> None:
        self.tab = [[0,0,0],
                    [0,0,0],
                    [0,0,0]]
        
        return None
    
    def jogar(self) -> None:
        print("""

Jogo da velha

| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 0 | 0 | 1 |        

        """)
        jogo = True
        while jogo:
            partida = True
            vez_de_jogar = 0
            marcacao = str(input("Selecione se o primeiro jogador será O ou X: "))
            if marcacao == "X":
                marcacao2 = "O"
            elif marcacao == "O":
                marcacao2 = "X"
            else:
                print("Opção inválida")
                continue
            print(f"O seu tipo foi seleciondo como {marcacao}")
            print(f"O {marcacao} joga primeiro")
            print(f"O {marcacao2} joga em seguida")
            while partida:
                try:
                    x,y = [int(x) for x in input("Digite as cordenadas separadas com[:]: ").split(':')]
                    if x > 2 or y > 2:
                        print("Coloque uma coordenada válida")
                        continue
                    os.system("cls")
                    if vez_de_jogar % 2 == 0:
                        if self.tab[x][y] == marcacao2:
                            print(self.print_tabuleiro())
                            print("Seu inimigo já marcou aqui !!!")
                            continue
                        elif self.tab[x][y] == marcacao:
                            print("Você já marcou aqui")
                            continue
                        self.tab[x][y] = marcacao
                    else:
                        if self.tab[x][y] == marcacao:
                            print(self.print_tabuleiro())
                            print("Seu inimigo já marcou aqui !!!")
                            continue
                        elif self.tab[x][y] == marcacao2:
                            print(self.print_tabuleiro())
                            print("Você já marcou aqui")
                            continue
                        self.tab[x][y] = marcacao2
                    for x in marcacao,marcacao2:
                        if (self.tab[0][0] == x and self.tab[1][1] == x and self.tab[2][2] == x):
                            print(f"O {x} GANHOU !!!")
                            partida = False
                            jogo = False
                        for c in range(0,3):
                            if (self.tab[c][0] == x and self.tab[c][1] == x and self.tab[c][2] == x):
                                print(f"O {x} GANHOU !!!")
                                partida = False
                                jogo = False
                            if (self.tab[0][c] == x and self.tab[1][c] == x and self.tab[2][c] == x):
                                print(f"O {x} GANHOU !!!")
                                partida = False
                                jogo = False
                    if partida == True:
                        print(self.print_tabuleiro())
                    vez_de_jogar += 1
                except:
                    print("Um erro inesperado ocorreu")
                


    def print_tabuleiro(self) -> str:
        taborganizado = "\n"
        for line in self.tab:
            taborganizado += f"{line[0]} {line[1]} {line[2]}\n"
        return taborganizado

tab = Tabuleiro()

tab.jogar()