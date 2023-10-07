numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 17, 18, 20, 21, 23, 25]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        
print(pares)