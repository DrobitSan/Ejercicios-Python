'''
48.- Introducid un texto por teclado (de 250 caracteres). Se debe realizar un programa que
cuente el número de preposiciones existentes en dicho texto, listando la frecuencia de cada
una de ellas.
El texto debe aparecer en cinco líneas de 50 caracteres cada una al principio de la pantalla
y a doble espacio. A continuación se indicará el número total de preposiciones y después
una lista de todas las preposiciones y cuántas veces aparece cada una.
'''


import re

preposiciones="a, ante, bajo, cabe, con, contra, de, desde, en, entre, hasta, hacia, para, por, según, sin, so, sobre, tras"
preposiciones=re.sub("[,]","",preposiciones)
preposiciones=preposiciones.split(" ")
texto="En la habitación había cuatro sillas de madera. Sobre las sillas unos cojines con grandes dibujos que llegaban hasta sus bordes. Hacia una esquina se podía divisar un jarrón sin flores y tras el jarrón, cabe la pared, una lámpara que se encendía mediante un largo cordón para iluminar el rincón de lectura. A un lado del jarrón, en una mesa antigua, permanecía un libro abierto bajo cuyas tapas asomaba un marcador de lectura. Desde la ventana, durante las horas solares y por entre las cortinas, un rayo de luz se proyectaba contra el fondo, ofreciendo al conjunto situado ante nosotros una visión más o menos nítida según la hora del día."
n_texto=re.sub("[^A-Za-z áéíóú]", "", texto)
l_texto=n_texto.split(" ")
for i in range(len(l_texto)):
    l_texto[i]=l_texto[i].lower()


apariciones=[0]*len(preposiciones)

for i in range(len(l_texto)):
    for n in range(len(preposiciones)):
        if l_texto[i]==preposiciones[n]:
            apariciones[n] +=1

total=0
for i in range(len(apariciones)):
    total+=apariciones[i]

print(f"El numero total de preposiciones es: {total}")


lineas=len(texto)//2 +1
for i in range(len(l_texto)):
    if i%13==0:
        print("\n")
    print(f"{l_texto[i]:<12}", end="")



print("\nPreposiciones:")
for i in range(len(apariciones)):
    print(f"{preposiciones[i]:<8}", end="")

print("\nNumero de apariciones:")

for i in range(len(apariciones)):
    print(f"{apariciones[i]:<8}", end="")