'''
42.- Leer 5 cadenas, almacenarlas en un array separadas por blanco y a continuación
visualizarla.
'''



def frase():
    n=int(input("Elegir numero de cadenas a introducir: "))
    i=1
    array=[]
    while i <= n:
        cadena= input("Introducir cadena nº "+str(i)+": ")
        array.append(cadena)
        i +=1
    for j in range(n):
        print(array[j], end=" ")

frase()


