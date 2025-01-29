def contar_frecuencia_palabras(frase):
    palabras = frase.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    print(frecuencia)
frase = input("Introduce una frase: ")
contar_frecuencia_palabras(frase)