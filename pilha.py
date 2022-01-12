def main():
    global pilha
    pilha =[]
    menu = None
    maxPilha = 20
    contpilha = 0
    while menu != "5":
        print()
        print("1 - Empilhar   2 - Desempilhar")
        print("3 - Limpar     4 - Mostrar Pilha")
        print("5 - Sair")
        print()
        menu = (input(("Selecione o comando: ")))
        print()
        if menu == "1": 
            pilhaInserir =(input(("Digite o número ou nome: ")))
            pilha.append(pilhaInserir)
            print()
            print("Foi adicionado no topo da pilha: ",pilha)
            contpilha = contpilha +         1
        if contpilha == maxPilha:
            print()
            print("#-#-#-#-PILHA CHEIA-#-#-#-#")
            print()
            print("PARA LIMPAR A PILHA SELECIONO A OPÇÃO 3 OU 2 PARA DESEMPILHAR")
            print()            
        if menu == "2": 
            pilha.pop()
            print("Foi removido o topo da pilha",pilha)
            print()
            contpilha = contpilha - 1
        if menu == "3":
            pilha.clear()
        if  menu == "4":
            print("Esses são os elementos da pilha: ",pilha)
            print()       
main()
