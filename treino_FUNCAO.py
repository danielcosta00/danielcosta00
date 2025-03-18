import os

os.system('cls')

def minha_funcao(valor1, valor2):
    return valor1 + valor2

while True:
    valor1 = int(input("Valor1: "))
    valor2 = int(input("Valor2: "))
    if valor1 and valor2 < 0:
        break

    resposta = minha_funcao(valor1, valor2)
    print(valor1, "+", valor2, "=", resposta)