def computador_escolhe_jogada(n, m):
    jogada = 0
    if m == 1:
        return 1
    else:
        for i in range(1, m):
            if (n-i) % (m+1) == 0:
                jogada = i
                break
        if jogada != i:
            return m
        else:
            return jogada


def usuario_escolhe_jogada(n,m):
    x=True
    while x == True:
        jogada=int(input("Quantas peças você quer tirar? "))
        if jogada > m or jogada <= 0:
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            x=False
    return jogada

def partida():
    z = True
    while z == True:
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        if n < m:
            print("Por favor, digite um número de peças maior que número máximo de jogadas!")
        else:
            z = False
    if n % (m+1) == 0:
        print("Voce começa!")
        print("")
        primeiro = 'Usuário'
    else:
        print("Computador começa!")
        print("")
        primeiro = 'Computador'
    x = True
    while x == True:
        if n > 0:
            i = 2
            for i in (2,3):
                    if primeiro == 'Computador':
                        if i == 2 and n != 0:
                            jogada = computador_escolhe_jogada(n, m)
                            n = n - jogada
                            if jogada == 1:
                                print("O Computador tirou uma peça.")
                                print("")
                            else:
                                print(f"O Computador tirou {jogada} peças.")
                                print("")
                            jogador = 'Computador'
                        if i == 3 and n != 0:
                            jogada = usuario_escolhe_jogada(n, m)
                            n = n - jogada
                            if jogada == 1:
                                print("Você tirou uma peça.")
                                print("")
                            else:
                                print(f"Você tirou {jogada} peças.")
                                print("")
                            jogador = 'Usuário'
                    if primeiro == 'Usuário':
                        if i == 2 and n != 0:
                            jogada = usuario_escolhe_jogada(n, m)
                            n = n - jogada
                            if jogada == 1:
                                print("Você tirou uma peça.")
                                print("")
                            else:
                                print(f"Você tirou {jogada} peças.")
                                print("")

                            jogador = 'Usuário'
                        if i == 3 and n != 0:
                            jogada = computador_escolhe_jogada(n, m)
                            n = n - jogada
                            if jogada == 1:
                                print("O Computador tirou uma peça.")
                                print("")
                            else:
                                print(f"O Computador tirou {jogada} peças.")
                                print("")
                            jogador = 'Computador'
            if n == 1:
                print("Agora resta apaneas uma peça.")
                print("")
            elif n ==0:
                print("")
            else:
                print(f"Agora restam {n} peças.")
                print("")
        else:
            x=False
    print(f"Fim de jogo o {jogador} ganhou!")
    return jogador


def campeonato():
    comp = 0
    usu = 0
    for i in range(3):
        ganhador = 0
        print(f"**** Rodada {i} ****")
        ganhador = partida()
        if ganhador == 'Computador':
            comp = comp +1
        else:
            usu = usu +1
    print("")
    print("**** Final do campeonato! ****")
    print("")
    print(f"Placar: Você {usu} X {comp} Computador")


def main():
    z = True
    while z == True:
        escolha=int(input("""
        Olá, seja bem-vindo ao jogo do NIM!
        Dentre as opções a baixo, escolha uma:    
        1 - para jogar uma partida isolada
        2 - para jogar um campeonato  
        """))
        if escolha == 1:
            print("Você escolheu jogar uma partida isolada!")
            partida()
            z=False
        elif escolha == 2:
            print("Você escolheu jogar um campeonato!")
            campeonato()
            z=False
        else:
            print("Opção inválida, tente novamente!")



main()
