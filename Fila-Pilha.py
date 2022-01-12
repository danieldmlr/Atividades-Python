import random
def main():
    pilha =[]
    j1 =[]
    j2 =[]
    print()
    print(" 1 - Jogar com fila")
    print(" 2 - Jogar com pilha")
    print(" 3 - Sair")
    print()
    menu = (input("Selecione o comando: "))
    print()
    valorinicial = int(input('Qual o valor inicial? '))
    print()
    valorfinal = int(input('Qual o valor final? '))
    print()
    qnumeros = int(input('Com quantos números quer jogar? '))
    fila = random.sample(range(valorinicial,valorfinal) ,qnumeros)
    print()
    print("O intervalo é de",valorinicial,"a ",valorfinal)
    print()
    while menu != '3':
        nescolhido = int(input('Jogador 1, insira o seu número: \n'))
        print ()
        while nescolhido in fila:
            j1.append(nescolhido)
            fila.pop(nescolhido)
            nescolhido = int(input('Você acertou, escolha outro número: '))
            print()
            print("Seus acertos foram: ",j1)
            print ()
        print ('Você errou, agora é o jogador 2\n')
        nescolhido = int(input('Jogador 2, insira seu palpite: \n'))
        while nescolhido in fila:
            j2.append(nescolhido)
            fila.pop(nescolhido)
            nescolhido = int(input('Você acertou, escolha outro número: \n'))
            print()
            print("Seus acertos foram: ",j2)
            print()
        if fila == []:
            if len(j1) > len(j2):
                print("O jogador 1 ganhou o jogo \n")
            if len(j2) > len(j1):
                print("O jogador 2 ganhou o jogo \n")
            if len(j1) == len(j2):
                print("O jogo deu empate \n")
            break
        else:
            print("Você errou, agora é o jogador 1\n")
            continue
main()
