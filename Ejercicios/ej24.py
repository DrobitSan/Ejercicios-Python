'''
24.- Programa que lee 50 números enteros sobre un vector y obtiene e imprime cuáles
son el mayor y el menor número almacenados y cuántas veces se repiten ambos.
'''



entrada= input("Introducir numeros enteros:")


def programa():
    menor= 0
    mayor= 0

    lista= sorted(entrada.split(","))
    
    for n in lista:
        if n == lista[0]:
            menor += 1
    
    
    print("El numero menor es: " + lista[0]+ " y se repite "+ str(menor) + " veces.")


    lista= sorted(lista,reverse=True)

    for n in lista:
        if n == lista[0]:
            mayor += 1

    print("El numero mayor es: " + lista[0] + " y se repite "+ str(mayor) + " veces.")


programa()



