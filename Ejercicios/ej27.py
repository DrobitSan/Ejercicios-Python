'''
27.- Dado un número entero positivo de 10 cifras. Programa que compruebe si un
número es capicúa utilizando un vector de 10 componentes.
'''



entrada= input("Introducir numero:")

def capicua(entrada):
    lista= list(entrada)
    reves= list(reversed(lista))
    verdadero=[]
    

    for n, i in enumerate(lista):
        if lista[n] == reves[n]:
            verdadero.append(True)
        else:
            verdadero.append(False)


    if all(verdadero):
        print("Es capicua")
    
    else:
        print("No es capicua")
    
capicua(entrada)
            




