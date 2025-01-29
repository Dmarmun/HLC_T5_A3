def suma_promedio(numeros):
    suma = sum(numeros)
    promedio = suma / len(numeros)
    print(f"Suma: {suma}, Promedio: {promedio}")
numeros = [90, 50, 70]
print("Lista: "+str(numeros))
suma_promedio(numeros)
