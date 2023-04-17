'''
17.- Escribe un programa que lea un número e imprime un triángulo de números de la
forma siguiente. Si el número leído es 4, imprimirá:
1
22
333
4444
'''


num= int(input("Introducir altura de la piramide:"))

for n in range(num):
    for i in range(n+1):
        print(n+1, end= "")
    print("\n")

