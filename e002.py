def ordenada(lista):
    sin_repes = list(set(lista))
    print("La lista ordenada: "+str(sin_repes))
lista = ['hola', 'hola', 'caracola', 'caracola']
print("La lista sin ordenar: "+str(lista))
ordenada(lista)
