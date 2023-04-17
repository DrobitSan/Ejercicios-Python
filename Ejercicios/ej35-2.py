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


l_suma=[]
l_llevas=[]
n=4
while n > -1:
    if n==4:
        x= int(_lista1[n])+int(_lista2[n])
    else:
        x= int(_lista1[n])+int(_lista2[n])+int(l_llevas[0])
    
    if len(str(x))==2:
        l_llevas.insert(0,str(x)[0])
        l_suma.insert(0,str(x)[1])
    else:
        l_llevas.insert(0,0)
        l_suma.insert(0,str(x)[0])
    n -= 1
l_suma.insert(0,l_llevas[0])
print(l_llevas)
print(_lista1)
print(_lista2)
print(l_suma)


def constante():
    print(" ",end="")
    for i, j in enumerate(_lista1):
        print("{:3}".format(j), end="")
    print("\n")
    print("+", end="")
    for i, j in enumerate(_lista2):
        print("{:3}".format(j), end="")
    print("\n")
    print("----------------")

def imp_suma(i):
    print("   "*(i),end="")
    for n in range((6-i)):
        print(l_suma[-(6-i):][n],end= "  ")
    print("\n")

i=5
while i > -1:
    if i==5:
        constante()
        print("\n")
        input("Pulsa ENTER para comenzar la suma paso a paso")
    print("\n")
    if len(l_suma)==5:
        if l_llevas[i-1]=="1":
            print("   "*(i-1)+"1")
        constante()
        imp_suma(i)
    elif len(l_suma)==6:
        if l_llevas[i-1]=="1":
            if i>0:
                print("   "*(i-1)+"1")
            else:
                print("1")
        constante()
        imp_suma(i)
    print("\n")
    if i>0:
        input("Pulsa ENTER para el siguiente paso")

    i -= 1
    
#hacer que no salga al final 1 arriba o 0 abajo