import os

os.system('cls')

# Entrada do valor
valor = float(input("Insira um valor em reais: "))

# Garante que o valor seja tratado corretamente como centavos para evitar imprecisões / 
valor = int(round(valor * 100))

# Listas de cédulas e moedas (em centavos para evitar erros de precisão)
notas_moedas = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
rotulos = [
    "nota(s) de R$ 100.00", "nota(s) de R$ 50.00", "nota(s) de R$ 20.00",
    "nota(s) de R$ 10.00", "nota(s) de R$ 5.00", "nota(s) de R$ 2.00",
    "moeda(s) de R$ 1.00", "moeda(s) de R$ 0.50", "moeda(s) de R$ 0.25",
    "moeda(s) de R$ 0.10", "moeda(s) de R$ 0.05", "moeda(s) de R$ 0.01"
]

# Impressão das notas e moedas
print("NOTAS:")
for i in range(6):  # Primeiras 6 são notas
    qtd, valor = divmod(valor, notas_moedas[i])
    print(f"{qtd} {rotulos[i]}")

print("MOEDAS:")
for i in range(6, len(notas_moedas)):  # As restantes são moedas
    qtd, valor = divmod(valor, notas_moedas[i])
    print(f"{qtd} {rotulos[i]}")

