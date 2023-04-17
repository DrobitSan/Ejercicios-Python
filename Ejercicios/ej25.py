'''
25.- Con el mismo vector del ejercicio anterior. Programa que calcula e imprime las
sumas de las componentes de índice par y las de índice impar.
'''



vector= input("Introducir vector:")

def suma():
    lista= vector.split(",")
    impares=0
    pares=0

    for n in lista:
        if int(n) % 2 !=0:
            impares += int(n)
        elif int(n) % 2 == 0:
            pares += int(n)
    
    print("La suma de los numeros impares es: " + str(impares) + "\n" + "Y la de numeros pares es: " + str(pares))

suma()