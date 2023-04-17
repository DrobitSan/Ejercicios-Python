'''
34.- Generar 30 números entre el 1 y el 99 y dar como resultados de salida:
a) Número más alto.
b) Número más bajo.
c) Media aritmética.
d) Moda.
e) Mediana.
f) Cantidad de 1,2...10 y sus porcentajes.
'''


import random as rd

def gen_num():
    lista=[]
    for n in range(30):
        lista.append(rd.randint(1,99))
    return lista

_lista=gen_num()
print(_lista)
print("El numero mas alto es: "+ str(max(_lista)))
print("El numero mas bajo es: "+ str(min(_lista)))

def media():
    suma=0
    for n in _lista:
        suma += n
    media= suma/len(_lista)
    return media

print("La media es: " + str(media()))

def moda():
    moda=[0]*len(_lista)
    for n, m in enumerate(_lista):
        for i in _lista:
            if m==i:
                moda[n]+=1
    x=moda.index(max(moda))
    return _lista[x]
print("Moda: " + str(moda()))

def mediana():
    ordenada= sorted(_lista)
    mediana= (ordenada[14]+ordenada[15])/2
    return mediana

print("Mediana: "+ str(mediana()))

def porcentaje_digitos():
    repeticiones=[]
    total=0
    for n in range(1,11):
        num=0
        for i in _lista:
            if n==i:
                num+=1
                total += 1
        repeticiones.append(num)
    digito=1
    for n in repeticiones:
        porcentaje= n/total*100
        print("El numero "+str(digito)+" aparece "+ str(n)+" veces con un porcentaje de "+str(round(porcentaje,2))+"%")
                                                                                            # o str("{0:.2f}".format(porcentaje))   
        digito+=1               
porcentaje_digitos()
        


