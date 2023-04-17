'''
46.- Leer una línea de entrada. Descartar todos los símbolos excepto los dígitos.
Convertir la cadena de dígitos en un entero y fijar el valor del entero a la variable n.
'''



def interesante():
    linea=input("Introduce cosas con numeros: ")
    lista=[]
    for i in range(len(linea)):
        if linea[i].isnumeric():
            lista.append(linea[i])
    numero="".join(lista)
    n=int(numero)
    return n

print(interesante())
