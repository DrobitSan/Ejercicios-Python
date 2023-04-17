#Raiz digital de una numero

num = input("Introducir número para calcular su raís digital:")


def raiz(x):

    suma_i= 0
    digitos= 0

    for i in x: 
        suma_i += int(i)
    
    for n in str(suma_i):
        digitos +=1 

    if digitos > 1:
        return raiz(str(suma_i))
    else: 
        return suma_i
        


print("La raiz digital de "+ str(num)+ " es "+ str(raiz(num)))

