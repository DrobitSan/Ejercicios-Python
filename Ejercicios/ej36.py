'''
36.- Llenar una tabla de 10 posiciones con números enteros comprendidos entre el 1 y el
99. Ordenar dicha tabla de menor a mayor y visualizarla por pantalla de la forma
siguiente:
'''



import random

lista=[]
for n in range(10):
    lista.append(random.randint(1,99))

lista2=sorted(lista)

def ordenar(listo):
    lista= listo.copy()
    for i in range(len(lista)):
        for indice in range(len(lista)-1):
            if lista[indice]>lista[indice+1]:
                lista[indice], lista[indice+1]= lista[indice+1], lista[indice]
    return lista
    
    
def imp_tabla(lista):
    print("{:<20} {:<25}".format("Tabla inicial","Tabla ordenada"))
    for i in range(10):
        print("{:<20} {:<25}".format(lista[i],ordenar(lista)[i]))
    
imp_tabla(lista)
