valor = float(input("Digite o valor: "))
distancia = float(input("Digite a distancia em km: "))

if valor >= 100 and distancia <= 10:
    print("Frete gratis")
else:
    print("frete não é gratis")