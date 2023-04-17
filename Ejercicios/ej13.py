'''
13.- Programa que genera la lista de los N primeros números primos, N es el dato de
entrada
'''



num = int(input("Introducir cuántos de los primero numeros primos quiere ver:"))


def primos(n):
    lista_primos=[]
    i = 1
    x = 2

    while len(lista_primos) <= n:
        lista= []
        while  x >= i :
            if x % i == 0:
                lista.append(i) 
            i += 1

        if lista == [1,x]:
            lista_primos.append(x)

        x += 1
        i = 1

    return lista_primos

print(primos(num))

            


