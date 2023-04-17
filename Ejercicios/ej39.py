'''
39.- Hacer un programa que hace “eco” del flujo de entrada y convierte las palabras en
palabras iguales que comienzan con letra mayúscula.
Ejemplo: “cáceres patrimonio de la humanidad”
“Cáceres Patrimonio De La Humanidad”

'''


frase= "hola me llamo serhiy"

#frase= frase.title()

def mayus(frase):
    lista= frase.split(" ")
    print(frase)
    for i in range(len(lista)):
        lista[i][0]=lista[i][0].upper()
    return lista

print(mayus(frase))