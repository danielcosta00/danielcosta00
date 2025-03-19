valores = input().split()

A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

if A == 0:
    print("Impossivel calcular")
else:
    delta = B**2 - 4*A*C

    if delta < 0:
        print("Impossivel calcular")
    else:
        x1 = (- B + delta**0.5)/ (2*A) 
        x2 = (- B - delta**0.5)/ (2*A)
        print(f"R1= %.5f"%x1)
        print(f"R2= %.5f"%x2)

# DOIS MODOS

valores = input().split()

A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

if A == 0:
    print("Impossivel calcular")
else:
    delta = B**2 - 4*A*C

    if delta < 0:
        print("Impossivel calcular")
    else:
        x1 = (- B + delta**0.5)/ (2*A) 
        x2 = (- B - delta**0.5)/ (2*A)
        print(f"R1 = {x1:.5f}")
        print(f"R2 = {x2:.5f}")