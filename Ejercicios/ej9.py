'''
9.- Algoritmo que diga si un número entero positivo es primo o no (se va dividiendo por
2, 3, 5, 7....... hasta N-1). Si ninguna de las divisiones es exacta y llegamos a una en la
que el cociente es menor o igual que el divisor, el nº es primo.
'''




n= int(input("Comprobar si el número es primo:"))

def primo(n):
    divisor = 2
    while divisor < n:
        if n % divisor == 0:
            return True
        divisor += 1
    return False



if primo(n):
    print("No es primo")
else:
    print("Es primo")


        


