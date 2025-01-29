def suma_promedio(numeros):
    suma = 0
    for i in numeros:
        suma += i
    promedio = suma / len(numeros)
    print(f"Suma: {suma}, Promedio: {promedio}")
numeros = [90, 50, 70]
print("Lista: "+str(numeros))
suma_promedio(numeros)
