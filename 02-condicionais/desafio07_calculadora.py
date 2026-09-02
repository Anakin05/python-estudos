numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, * ou /): ")
if operacao == "+":
    print("Resultado:", numero1 + numero2)
elif operacao == "-":
    print("Resultado:", numero1 - numero2)
elif operacao == "/":
    print("Resultado:", numero1 / numero2)
elif operacao == "*":
    print("Resultado:", numero1 * numero2)
else:
    print("Operação inválida")