def divisores(numero):
    lista = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            lista.append(i)
    print("Lista de divisores: "+str(lista))
numero = int(input("Introduce un número: "))
divisores(numero)