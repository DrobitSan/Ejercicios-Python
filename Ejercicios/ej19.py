'''
19.- En el mismo supermercado quieren montar también pilas del mismo número de
latas de alto que de ancho.
* * *
* * *
* * *
Ahora bien no todas las cantidades de latas que pueden apilarse triangularmente pueden
ponerse en estructuras cuadradas. Diseñas un programa C que indique si un número
natural es válido para realizar los dos tipos de estructuras. (Un ejemplo válido es el
número 36).
'''



num = int(input("Introducir numero de latas:"))

def piramide(n):
    i = 1
    pisos = 1
    x = 1
    suma_i = 1

    while n - i > 0:
        n -= i
        i += 1
        pisos += 1
        suma_i += i  

    if n == i:
        resultado = False    
        while  resultado == False:
            if x ** 2 == suma_i:
                resultado = True
                print("Se pueden apilar en una piramide de "+str(pisos)+" pisos y tambien en un cuadrado de "+ str(x) + " lados.")
           
            elif x**2 > suma_i:
                resultado = True
                print("No se pueden apilar en piramide y cuadrado a la vez")
            
            elif x**2 < suma_i:
                x += 1
           
    else:
        print("No se pueden apilar en piramide y cuadrado a la vez")

    

piramide(num)



