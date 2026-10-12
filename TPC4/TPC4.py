from random import randint

lista = []

opcao = -1

while opcao != 0:

    print("\n----- MENU -----")
    print("1 - Criar Lista")
    print("2 - Ler Lista")
    print("3 - Soma")
    print("4 - Média")
    print("5 - Maior")
    print("6 - Menor")
    print("7 - Está ordenada por ordem crescente")
    print("8 - Está ordenada por ordem decrescente")
    print("9 - Procurar elemento")
    print("0 - Sair")

    opcao = int(input("Opção: "))

    
    if opcao == 1:

        lista = []

        N = int(input("Quantos números quer na lista? "))

        for i in range(N):
            lista.append(randint(1, 100))

        print(lista)

    
    elif opcao == 2:

        lista = []

        N = int(input("Quantos números quer inserir? "))

        for i in range(N):
            numero = int(input("Número: "))
            lista.append(numero)

        print(lista)

    
    elif opcao == 3:

        soma = 0

        for numero in lista:
            soma = soma + numero

        print("Soma =", soma)

    
    elif opcao == 4:

        soma = 0

        for numero in lista:
            soma = soma + numero

        if len(lista) > 0:
            media = soma / len(lista)
            print("Média =", media)
        else:
            print("Lista vazia")

    
    elif opcao == 5:

        if len(lista) > 0:

            maior = lista[0]

            for numero in lista:
                if numero > maior:
                    maior = numero

            print("Maior =", maior)

        else:
            print("Lista vazia")

    
    elif opcao == 6:

        if len(lista) > 0:

            menor = lista[0]

            for numero in lista:
                if numero < menor:
                    menor = numero

            print("Menor =", menor)

        else:
            print("Lista vazia")

    
    elif opcao == 7:

        crescente = True

        for i in range(len(lista)-1):

            if lista[i] > lista[i+1]:
                crescente = False

        if crescente:
            print("Sim")
        else:
            print("Não")

    
    elif opcao == 8:

        decrescente = True

        for i in range(len(lista)-1):

            if lista[i] < lista[i+1]:
                decrescente = False

        if decrescente:
            print("Sim")
        else:
            print("Não")

    
    elif opcao == 9:

        elemento = int(input("Elemento a procurar: "))

        posicao = -1

        for i in range(len(lista)):

            if lista[i] == elemento:
                posicao = i
                break

        print("Posição =", posicao)

    
    elif opcao == 0:

        print("Lista guardada:", lista)
        print("Programa terminado.")

    else:
        print("Opção inválida")