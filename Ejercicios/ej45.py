'''
45.- Escribir un programa que lea una secuencia de nombres, uno por línea, los ordene
y, a continuación , los presente por pantalla.
'''



def ordenar_nombres():
    lista=[]
    nombre=input("Introducir nombres 1 por 1 , cuando no haya mas escribir \"fin\": ")
    lista.append(nombre)
    while nombre != "fin":
        nombre=input("Introducir siguiente nombre: ")
        if nombre != "fin":
            lista.append(nombre)
    print("Los nombres son: ", end="")
    for i in range(len(lista)):
        if i< (len(lista) -1):
            print(lista[i]+",",end=" ")
        else:
            print(lista[i]+".")

ordenar_nombres()
