#1.- Programa que lea 3 números y los escriba ordenados de forma ascendente

texto = input("Introduce 3 numeros diferentes separados por comas")

lista = texto.split(",")

lista_enteros=[]

for n in lista:
    lista_enteros.append(int(n))

lista_ordenada= sorted(lista_enteros) 

print(lista_ordenada)