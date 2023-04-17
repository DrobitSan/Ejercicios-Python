'''
35.- Obtener diez números (0..9) mediante el generador de números aleatorios. Con
estos diez números se formarán dos de cinco cifras cada uno.

Sumar los dos números de cinco cifras obtenidos. La suma se realizará cifra a cifra
(unidades, decenas, centenas, etc.), apareciendo los sumandos y el resultado en letra,
también se indicará en letra si te llevas una y aparecerá un "1" encima del sumando
correspondiente.
Ej:
1
7 9 1 4 6 SEIS Y
+ 1 6 3 7 5 CINCO
------------------------
 1 ONCE y me llevo una

Pulse <Intro> para continuar

Al pulsar Intro pasarán a sumarse las dos cifras siguientes.
'''




import random

_lista1=[]
_lista2=[]
for i in range(5):
    _lista1.append(random.randint(0,9))
    _lista2.append(random.randint(0,9))

print(_lista1)
print(_lista2)

def imprimir_suma():
    for i in range(5):
        print(str(i), end= " ")
    print("\n")
    for i in range(5):
        print(str(i+5), end= " ")

def sumar():
    l_suma=[" "]*5
    l_llevas=[" "]*5
    n=5
    while n > 0:
        x=_lista2[n-1]+_lista1[n-1]
        if len(str(x))==2:
            abajo= str(x)[1]
            arriba= str(x)[0]
        else:
            abajo= x
            arriba= " "
        n-=1
        l_suma.insert(0, abajo)
        l_llevas.insert(0, arriba)

    return l_llevas, l_suma





def imprimir2():
    for i in sumar()[0]:
        print("{:3}".format(i), end="")
    print(" ",end="")
    for i, j in enumerate(_lista1):
        print("{:3}".format(j), end="")
    print("\n")
    print("+", end="")
    for i, j in enumerate(_lista2):
        print("{:3}".format(j), end="")
    print("\n")
    print("----------------")

imprimir2()


        