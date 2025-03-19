import os

os.system('cls')

valor = int(input())

intervalo = [
    (0,25), (25,50), (50,75), (75,100)
]
rotulos = [
    "Está entre 0 e 25","Está entre 25 e 50", "Está entre 50 e 75", "Está entre 75 e 100"
]



for i in range(4):
    if intervalo[i][0] <= valor <= intervalo[i][1]:
        print(f"O valor {valor} {rotulos[i]}.")
        break
else:
    print(f"O valor {valor} está fora dos intervalos definidos")
