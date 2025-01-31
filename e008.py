def contar_letras(texto):
    vocales = 'aeiouáéíóú'
    consonantes = 'bcdfghjklmnpqrstvwxyz'
    texto = texto.lower()
    conteo = {'vocales': 0, 'consonantes': 0}
    for letra in texto:
        if letra in vocales:
            conteo['vocales'] += 1
        elif letra in consonantes:
            conteo['consonantes'] += 1
    print("Vocales: "+str(conteo['vocales'])+ " Consonantes: "+str(conteo['consonantes']))
texto = input("Introduce un texto: ")
contar_letras(texto)