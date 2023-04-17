'''
28.- Programa que carga una matriz de 5 filas y 10 columnas con números enteros
imprimiendo los valores máximo y mínimo y sus posiciones dentro de la tabla.
'''
        


filas= int(input("Introducir numero de filas de la matriz:"))
columnas= int(input("introducir numero de comlumnas de la matriz:"))

def crear_matriz(filas, columnas):
    matriz= []

    for n in range(filas):
        matriz.append([])
        for i in range(columnas):
            matriz[n].append(int(input("Introducir valor ("+ str(n) + "," + str(i) +"):")))
    return matriz



def mayor_menor(matriz):
    pos_mayor, pos_menor= [0,0], [0,0]
    mayor, menor= matriz[0][0], matriz[0][0]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > mayor:
                pos_mayor= [i,j]
                mayor= matriz[i][j]
            if matriz[i][j] < menor:
                pos_menor= [i,j]
                menor= matriz[i][j]
    
    return {"mayor": mayor, "menor": menor, "pos_mayor": pos_mayor, "pos_menor": pos_menor}
        
crear_matriz= crear_matriz(filas, columnas)
mayor_menor= mayor_menor(crear_matriz)


print("El mayor numero es "+ str(mayor_menor["mayor"]) +" y esta en la posicion "+ str(mayor_menor["pos_mayor"]))
print("El menor numero es " + str(mayor_menor["menor"]) + " y esta en la posicion" + str(mayor_menor["pos_menor"]))





        
        




