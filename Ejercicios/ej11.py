'''
11.- Un número natural se denomina perfecto cuando es igual a la suma de todos sus
divisores, primos o no excepto él mismo. Por ejemplo 128 = 1 + 2 + 4 + 7 + 14. Escribe
un programa C que averigüe si un número natural positivo es perfecto o no
'''



num= int(input("Introducir numero:"))

lista_divisores=[]

def añadir_divisores(n):
    i = 1
    while n > i:

        if n % i == 0:
            lista_divisores.append(i)
        i += 1

def comprobar_suma():
    suma=0
    for n in lista_divisores:
        suma += n
    return suma

añadir_divisores(num)

if comprobar_suma() == num:
    print("Es un numero perfecto")
else:
    print("No es un numero perfecto")



