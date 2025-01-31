def pares(lista):
    for i in lista:
        if i%2==0:
            lista.remove(i)
        print(i)
lista = [1,2,3,4,5,5]
pares(lista)