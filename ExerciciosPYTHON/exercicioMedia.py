#Podemos programar a entrada de dois modos
#MODO 1:
nota1, nota2, nota3, nota4 = map(float, input().split())

#MODO 2 (tenho, particulamente, mais afinidade com essa forma. Entretanto, a outra economiza em linhas de programação)
valores = input().split()
nota1 = float(valores[0])
nota2 = float(valores[1])
nota3 = float(valores[2])
nota4 = float(valores[3])

media = (nota1*2 + nota2*3 + nota3*4 + nota4*1)/10

if 10 < valores < 0:
    print("Digite valores válidos!")
else:
    if media >= 7.0: #Preciso descobrir métodos para diminuição e uso de menos IF e ELIF
        print("Media: %.1f"%media)
        print("Aluno aprovado.")
    elif media < 5.0:
        print("Media: %.1f"%media)
        print("Aluno reprovado.")
    else:
        print("Media: %.1f"%media)
        print("Aluno em exame.")

        exame = float(input())
        print("Nota do exame: %.1f"%exame)
        mediafinal = (exame + media)/2
        if mediafinal >= 5.0:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
        print("Média final: %.1f"%mediafinal)

    
