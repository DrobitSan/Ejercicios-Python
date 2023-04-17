'''
23.- Construir un algoritmo que permita multiplicar dos números enteros positivos
empleando el método denominado multiplicacion rusa. Este método permite
calcular el producto de M*N de la siguiente manera:
En pasos sucesivos se divide M por 2 (división entera) y se multiplica N por 2. Este
proceso se repite hasta que M es 0. El resultado de la multiplicación deseada se obtiene
acumulando aquellos valores sucesivos de N para los cuales el valor de M es impar:
'''


n = int(input("Introducir primer multiplo:"))
m = int(input("Introducir segundo multiplo:"))

def mult(m, n):
    suma=0

    while m > 0:
        if m%2 != 0:
            suma += n
        
        m = m//2
        n= n*2

        
    return suma

print(str(mult(m, n)))