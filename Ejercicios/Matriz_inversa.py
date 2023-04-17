"""MATRIZ INVERSA  = A^-1   ;   A^-1 * A= I
Ax=B -> x=A^-1 * B
"""

#DETERMINANTE -> Solo de matrices cuadradas, es un numero

def determinante_1(matriz):
    return matriz[0]

def determinante_2(matriz):
    det= matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0]
    return det

def determinante_3(a):
    suma= a[0][0]*a[1][1]*a[2][2] + a[0][1]*a[1][2]*a[2][0] + a[0][2]*a[1][0]*a[2][1]
    resta= a[0][2]*a[1][1]*a[2][0] + a[0][1]*a[1][0]*a[2][2] + a[0][0]*a[1][2]*a[2][1]
    return suma-resta

matriz1= [3,5],[6,8]
matriz2= [4,7],[3,8]
matriz3= [3,5,7],[4,1,6],[1,3,9]
matrizolalla= [1,0,2],[0,2,-1],[1,1,3]

def adjunto3(A):
    resultado=[]
    for i in range(3):
        resultado.append([])
        for j in range(3):
                a=((-1)**(i+j))*menor_complementario3(A,i,j)
                resultado[i].append(a)
    return resultado

def menor_complementario3(A,i,j):
    nueva=[]
    n=-1
    for x in range(3):
        if x != i:
            nueva.append([])
            n+=1
            for y in range(3):
                if y != j:
                    nueva[n].append(A[x][y])
    return determinante_2(nueva)
            
ej= [1,3], [2,-1]

def adjunto2(A):
    resultado=[]
    for i in range(len(A)):
        resultado.append([])
        for j in range(len(A[i])):
                a=((-1)**(i+j))*menor_complementario2(A,i,j)
                resultado[i].append(a)
    return resultado

def menor_complementario2(A,i,j):
    for x in range(len(A)):
        if x != i:
            for y in range(len(A[i])):
                if y != j:
                    return A[x][y]


def traspuesta(A):
    nueva=[]
    for i in range(len(A)):
        nueva.append([])
        for j in range(len(A[i])):
            nueva[i].append(A[j][i])
    return nueva

def inversa(matriz):
    tras= traspuesta(adjunto3(matriz))
    inversa=[]
    det= determinante_3(matriz)
    for i in range(3):
        inversa.append([])
        for j in range(3):
            div= tras[i][j]/det
            inversa[i].append(div)
    return inversa


print("Matriz=" + str(matrizolalla))
print("Inversa=" + str(inversa(matrizolalla)))

