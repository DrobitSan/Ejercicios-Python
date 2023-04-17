'''
32.- Programa que imprime un cuadrado latino de orden N. Un cuadrado latino de orden
N es una matriz cuadrada en la que la primera fila contiene los N primeros números
naturales y cada una de las siguientes N-1 filas contiene la rotación de la fila anterior un
lugar a la derecha.
Ejemplo: Cuadrado latino de orden 4.
1 2 3 4
4 1 2 3
3 4 1 2
2 3 4 1
'''



def cuadlatino():
    filas= int(input("Numero de filas del cuadrado latino:"))
    matriz= []
    
    for i in range(filas):
        matriz.append([])
        if i == 0:
            for j in range(filas):         
                matriz[i].append(j+1)
        if i > 0:         
            matriz[i] = matriz[i-1].copy()  #o new_l = l[:]
            nuevo= matriz[i][filas-1]
            matriz[i].pop()
            matriz[i].insert(0,nuevo)
    return matriz

matriz= cuadlatino()

def imprimatriz(matriz):
    for i in range(len(matriz)):
        for j in matriz[i]:
            print(str(j), end=" ")
        nl="\n"
        print(f"{nl}")

imprimatriz(matriz)

