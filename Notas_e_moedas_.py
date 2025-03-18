valor = float(input())

if  0<= valor <= 1000000.00:
       

#notas
#100
    valor100 = int(valor//100)
    valor = valor%100

#50
    valor50 = int(valor//50)
    valor = valor%50

#20
    valor20 = int(valor//20)
    valor = valor%20

#10
    valor10 = int(valor//10)
    valor = valor%10

#5
    valor5 = int(valor//5)
    valor = valor%5

#2
    valor2 = int(valor//2)
    valor = valor%2

#Moedas
#1
    valor1 = int(valor//1)
    valor = valor%1

#050
    valor050 = int(valor//0.5)
    valor = valor%0.5

#025
    valor025 = int(valor//0.25)
    valor = valor%0.25

#010
    valor010 = int(valor//0.1)
    valor = valor%0.1

#005
    valor005 = int(valor//0.05)
    valor = valor%0.05

#001
    valor001 = round(valor/0.01)
else:
    print("Digite um número valido!")

print("NOTAS:")
print(f"{valor100} nota(s) de R$ 100.00")
print(f"{valor50} nota(s) de R$ 50.00")
print(f"{valor20} nota(s) de R$ 20.00")
print(f"{valor10} nota(s) de R$ 10.00")
print(f"{valor5} nota(s) de R$ 5.00")
print(f"{valor2} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{valor1} moeda(s) de R$ 1.00")
print(f"{valor050} moeda(s) de R$ 0.50")
print(f"{valor025} moeda(s) de R$ 0.25")
print(f"{valor010} moeda(s) de R$ 0.10")
print(f"{valor005} moeda(s) de R$ 0.05")
print(f"{valor001} moeda(s) de R$ 0.01")
