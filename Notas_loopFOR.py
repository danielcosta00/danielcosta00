notas=[]

for x in range(5):
    codigo_aluno = input("ALUNO: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

print("quantidade de notas", len(notas))

for n in notas:
        codigo_aluno = n[0]
        nota = n[1]
        print("O ALUNO", codigo_aluno, "tirou a nota: ", nota)
        
