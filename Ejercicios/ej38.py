'''
38.- Mediante el generador de números aleatorios llenar una tabla de dos dimensiones
(10,10) con números enteros comprendidos entre el 1 y el 99. La tabla deberá visualizarse
en pantalla así como los números que se van generando, colocándolos en cada casilla de la
tabla.
Ordenar la matriz anterior por filas y columnas, de menor a mayor, y visualizar la tabla
ordenada a la derecha de la anterior.

'''



import random

def crear_tabla(filas, columnas):
    tabla=[]
    for i in range(filas):
        tabla.append([])
        for n in range(columnas):
            tabla[i].append(random.randint(1,99))
    return tabla


def mergesort(lista):
    if len(lista)==1:
        return lista
    izq, dcha= partir(lista)
    return mezclar(mergesort(izq), mergesort(dcha))
    
    
def partir(lista):
    mitad= len(lista)//2    
    return lista[0:mitad], lista[mitad:]


def mezclar(izq, dcha):
    mezclada=[]
    i, j = 0, 0 
    while i<len(izq) and j<len(dcha):
        if izq[i]<dcha[j]:
            mezclada.append(izq[i])
            i += 1
        else:
            mezclada.append(dcha[j])
            j += 1
    mezclada.extend(izq[i:])
    mezclada.extend(dcha[j:])
    return mezclada
    

def ordenar_tabla(tabla):
    resultado1=[]
    for i in range(len(tabla)):
        resultado1.append(mergesort(tabla[i]))
    return resultado1
    
def traspuesta(tabla_ordenada):   
    resultado2=[]
    for i in range(len(tabla_ordenada[0])):
        resultado2.append([])
        for n in range(len(tabla_ordenada)):
            resultado2[i].append(tabla_ordenada[n][i])
    return resultado2


def imprimir_tabla(tabla, resultado):
    print("{:>1} {:>19}".format("Tabla inicial", "Tabla ordenada"))
    print(f'\n{"Tabla inicial", "Tabla ordenada":{20}, {20}}')
    for i in range(len(tabla)):
        for n in range(len(tabla[0])):
            print("{:<4}".format(tabla[i][n]), end="")        #str(tabla[i][n])+" "
        print("    ", end="")
        for n in range(len(tabla[0])):   
            print("{:<4}".format(resultado[i][n]), end="") 

        print("\n")


filas=4  #int(input("Numero de filas: "))
columnas=4   #int(input("Numero de columnas"))
tabla= crear_tabla(filas, columnas)
resultado= traspuesta(ordenar_tabla(traspuesta(ordenar_tabla(tabla))))
print(tabla)
print(resultado)
imprimir_tabla(tabla, resultado)