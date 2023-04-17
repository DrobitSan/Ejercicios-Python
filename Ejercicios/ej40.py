'''
40.- Hacer un programa que haga “eco” de la entrada poniendo cada palabra en una
línea.
'''



frase= input("Introducir frase")

def basura(frase):
    frase=frase.split(" ")
    for i in range(len(frase)):
        print(frase[i])

basura(frase)