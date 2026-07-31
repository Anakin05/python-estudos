#programa que imprima apenas os números pares até o número escolhido pelo usuário.

final = int(input("Escolha um número final: "))
contador = 2

while contador <= final:
    print(contador)
    contador = contador + 2

#segunda opção

contador = 1

while contador <= final:
    if contador % 2 == 0:
        print(contador)

    contador = contador + 1