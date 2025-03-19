notas =[]
contador = 1

while contador <= 5:
    codigo_aluno = input("Aluno: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

    contador = contador + 1

print("Quantidade de notas", len(notas))

print("\nNotas dos alunos:")
for aluno in notas:
    print(f"Aluno: {aluno[0]}, Nota: {aluno[1]}")