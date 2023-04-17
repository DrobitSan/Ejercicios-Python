'''
47.- Mediante el generador de números aleatorios generar un texto (mayúsculas -65 a 90- y
minúsculas -97 a 122-) de 250 caracteres. Convertir todo a mayúsculas. Ver cuántas A, B,
C...Z hay en el texto.
El texto debe aparecer en 5 líneas de 50 caracteres cada una al principio de la pantalla y a
doble espacio. Más abajo aparecerán la tabla siguiente:
A B C D E F G H I J K L MN O P Q R S T U V WX Y Z
23053157803145735790124679
La que aparezca mayor número de veces se mostrará en vídeo inverso.
'''


import random as rd

#diccionario minusculas
d_minusculas={}
str_minusculas= "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
l_minusculas= str_minusculas.split(",")

for n in range(26):
    d_minusculas[n+65]=l_minusculas[n]

#diccionario mayusculas
l_mayusculas=[]
d_mayusculas={}
for n in range(26):
    d_mayusculas[n+97]= l_minusculas[n].upper()


#aleatorios a letras
l_aleatorios=[]
while len(l_aleatorios)<250:
    n= rd.randint(65,122)
    if not (90<n<97):
        l_aleatorios.append(n)


l_letras=[]
i=0
while i <250:
    if 96<l_aleatorios[i]<123:
        l_letras.append(d_mayusculas[l_aleatorios[i]])
    elif 64<l_aleatorios[i]<91:
        l_letras.append(d_minusculas[l_aleatorios[i]])
    i+=1


#letras a mayusculas todas
l_mayusculas=[]
for n in range(len(l_letras)):
    l_mayusculas.append(l_letras[n].upper())

#numero de apariciones
l_apariciones=[0]*26
valores_dic=d_mayusculas.values()
for n in range(len(l_mayusculas)):
    for i in range(len(l_apariciones)):
        if l_mayusculas[n]==d_mayusculas[i+97]:
            l_apariciones[i]+=1


def imprimir():
    y=0
    while y<5:
        for n in range(50):
            print(l_letras[n+(50*y)], end=" ")
        print("\n")
        y+=1
    for i in range(26):
        print("{:<4}".format(d_mayusculas[i+97]), end="")
    print("\n")
    for i in range(26):
        print("{:<4}".format(l_apariciones[i]), end="")


imprimir()
