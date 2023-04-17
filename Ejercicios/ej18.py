'''
18.- En el supermercado de la esquina colocan las latas de conservas apiladas
triangularmente. Esto trae bastantes problemas a la hora de hacer los pedidos, ya que
quieren un número de latas de manera que no sobre ni falte ninguna. Así, 6 latas se
pueden apilar triangularmente de la siguiente manera.
*
* *
* * *
Si tuvieran 7 latas, no podrían apilarse de forma triangular, ya que sobraría una.
Escribir un programa C, que dado un número natural, compruebe si es adecuado para
montar pilas triangulares.
'''



n = int(input("Introducir numero de latas:"))

def piramide(n):
    i = 1
    pisos = 1

    while n - i > 0:
        n -= i
        i += 1
        pisos += 1

    if n == i:
        print("Se pueden apilar en una piramide de "+str(pisos)+" pisos")
    else:
        print("No se pueden apilar en piramide")

piramide(n)