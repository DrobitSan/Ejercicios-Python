'''
22.- Escribir un programa que lea un número natural de 4 cifras, no todos iguales.
Implementa la función Mayor(N), que calcula el mayor número que se puede formar
con las cifras de N, y la función Menor(N) que calcula el menor número que se puede
formar con las cifras de N.
'''



num= input("Introducir numero de 4 cifras:")

while len(num) != 4:
    print("Solo se puede un numero de 4 cifras")
    num= input("Introducir numero de 4 cifras:")


def ordenar(n):
    lista=[]
    for n in num:
        lista.append(n)

    mayor= sorted(lista, reverse=True) 
    menor= sorted(lista)

    print("".join(mayor))
    print("".join(menor))
    
ordenar(num)

