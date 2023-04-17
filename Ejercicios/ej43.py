'''
43.- Leer una secuencia de nombres, uno por línea, terminado por el valor centinela’$’.
A continuación visualizar los nombres almacenados en el array nombres.
'''



def leer_nombres():
    nombres= []
    nombre1= input("Introducir nombres 1 por 1, ultimo terminar en punto: ")
    nombres.append(nombre1)
    if nombre1[-1]==".":
        return nombres
    else:
        nombre2=input("Introducir siguiente nombre: ")
        nombres.append(nombre2)
        while nombre2[-1] != ".":
            nombre2=input("Introducir siguiente nombre: ")
            nombres.append(nombre2)
        nombres[-1]= list(nombres[-1])
        nombres[-1].pop()
        nombres[-1]="".join(nombres[-1])
        return nombres

print(leer_nombres())