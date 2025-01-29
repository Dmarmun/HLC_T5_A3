def largo(lista):
    diccionario = {palabra: len(palabra) for palabra in lista}
    print("Diccionario con longitud: "+str(diccionario))
lista = ['disco', 'windows', 'sandia']
print("Diccionario sin longitud: "+str(lista))
largo(lista)