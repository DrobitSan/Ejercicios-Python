'''
29.- Con la misma matriz del ejercicio anterior. Programa que obtiene e imprime su
matriz traspuesta.
'''



filas= int(input("Introducir numero de filas de la matriz:"))
columnas= int(input("introducir numero de comlumnas de la matriz:"))

def crear_matriz(filas, columnas):
    matriz=[]
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(int(input("Introducir valor ("+ str(i) + ", " + str(j) + "):")))
    return matriz

matriz= crear_matriz(filas,columnas)
print(matriz)

def matraspuesta(matriz):
    traspuesta=[]
    for i in range(columnas):
        traspuesta.append([])
        for j in range(filas):
            traspuesta[i].append(matriz[j][i])
    return traspuesta

traspuesta= matraspuesta(matriz)

print(traspuesta)
