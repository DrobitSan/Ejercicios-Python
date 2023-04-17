'''
41.- Hacer un programa que cuente la ocurrencia de la letra ‘e’ en el flujo de entrada.
'''



frase= input("Introduce una puta frase o te rajo:")

def contar_e(frase):
    contador=0
    for i in range(len(frase)):
        if frase[i]== "e":
            contador += 1
    return contador

print(contar_e(frase))
    

