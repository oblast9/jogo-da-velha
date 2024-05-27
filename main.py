from classes import *

player = JogoDaVelha()


print( " ESSE É O TABULEIRO  ")
print(" ")
player.tabuleiro()
print(" ")
print(" VOCÊ TERÁ QUE DIGITAR O NUMERO DA POSIÇÃO PARA JOGAR ")
print(" ")
cont = 10
while cont > 5:
    for i in range(4):
        val = input(" DIGITE UM NUMERO JOGADOR | X | : ")
        player.jogador2(val)
        val = input(" DIGITE UM NUMERO JOGADOR | O | : ")
        player.jogador1(val)
        player.tabuleiro()
    r = input(" houve um ganhador? S ou N: ")
    resp = r.lower()
    if resp == "s":
        print(" PARABENS AO GANHADOR! ")
        cont = cont - 5
    elif resp == "n":
        print(" DEU VELHA...")
        cont = cont - 5
        
 







