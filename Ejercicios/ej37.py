'''
37.- Llenar dos tablas de 10 posiciones cada una con números enteros comprendidos entre
el 1 y el 99. Ordenar dichas tablas y fusionarlas en una tercera de 20 posiciones, de forma
que vaya quedando ordenada de menor a mayor. Ir visualizando el proceso.
'''



import random

lista_1= []
lista_2= []
for i in range(10):
    lista_1.append(random.randint(1,99))
    lista_2.append(random.randint(1,99))


def seleccion(listo):
    lista= listo.copy()
    izquierda=0
    derecha= len(lista)-1
    while izquierda < derecha:
        listaca= range(10)[-(10-izquierda):]
        for i in listaca:
            if lista[izquierda]>lista[i]:
                lista[izquierda], lista[i]= lista[i], lista[izquierda]
        izquierda += 1
    return lista 

primeras_listas= seleccion(lista_1)+ seleccion(lista_2)    
print("Primeras listas: "+ str(primeras_listas))

def mergesort(lista):
    if len(lista)==1:
        return lista
    izq, dcha= dividir(lista)
    return mezclar(mergesort(izq), mergesort(dcha))

def dividir(lista):
    mitad= len(lista)//2
    return lista[0:mitad], lista[mitad:]

def mezclar(izq, dcha):
    mezclada= []
    i, j= 0, 0
    while i<len(izq) and j<len(dcha):
        if izq[i]<dcha[j]:
            mezclada.append(izq[i])
            i +=1
        else:
            mezclada.append(dcha[j])
            j+= 1
    mezclada.extend(izq[i:])
    mezclada.extend(dcha[j:])
    return mezclada
    

l_resultado= mergesort(primeras_listas)

print("{:<10} {:<10} {:<10}".format("Tabla 1","Tabla 2", "T. Resultado"))
for i in range(20):
    if i<10:
        print("{:<10} {:<10} {:<10}".format(lista_1[i], lista_2[i], l_resultado[i]))
    else:
        print("{:24}".format(l_resultado[i]))
