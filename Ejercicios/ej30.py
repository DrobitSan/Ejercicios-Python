'''
30.- Programa que genera e imprime una matriz unitaria de orden N. Una matriz unitaria
de orden N es la que tiene N filas y N columnas con todas sus componentes a 0, excepto
las de su diagonal principal que están a 1.
'''



def unitaria():
    filas= int(input("Introducir numero de filas de la matriz:"))
    matriz=[]
    for i in range(filas):
        matriz.append([])
        for j in range(filas):
            if j == i:
                matriz[i].append(1)
            elif j != i:
                matriz[i].append(0)
    return matriz

matriz= unitaria()

def imprimatriz(matriz):
    for i in range(len(matriz)):
        for j in matriz[i]:
            print(str(j), end=" ")
        nl="\n"
        print(f"{nl}")

imprimatriz(matriz)

