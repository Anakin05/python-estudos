numero = int(input("Digite um número: "))

numeroinicial = 2
soma = 0

while numeroinicial <= numero:
    soma = soma + numeroinicial
    numeroinicial = numeroinicial + 2

print(soma)