# Programa que aceita apenas números positivos.

numero = int(input("Digite um número: "))

while numero < 0:
    print("Número inválido!")
    numero = int(input("Digite um número: "))

print("Número válido!")