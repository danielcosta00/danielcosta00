#Vogais
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0
contador_consoantes = 0

#entrada
frase = input("Digite uma frase: ")

#Deixando as letras em minusculo
for letra in frase:
    letra = letra.lower()
   
    if letra.isalpha(): #Essa função verifica se o caractere é uma letra do alfabeto (A-Z, a-z). / Se for uma letra, o código continua e verifica se é uma vogal. / Se não for uma letra (espaço, número, pontuação, etc.), o caractere é ignorado.
        if letra == 'a':
            contador_a += 1
        elif letra == 'e':
            contador_e +=1
        elif letra == 'i':
            contador_i +=1
        elif letra == 'o':
            contador_o +=1
        elif letra == 'u':
            contador_u +=1
        else:
            contador_consoantes += 1


print("\nResultados: ")
print("a: ", contador_a)
print("e: ", contador_e)
print("i: ", contador_i)
print("o: ", contador_o)
print("u: ", contador_u)
print("Além disso, temos :",contador_consoantes,"consoantes")