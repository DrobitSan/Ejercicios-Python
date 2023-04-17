'''
3.- Programa que lee un nº de notas con valores de 0 a 10, que termina con el valor –1,
y nos dice si hubo o no alguna con el valor 10.
'''


notas = input("Introducir notas")
array_notas= notas.split(",")
resultado= False

for n in array_notas:
    if n=="10":
        resultado=True
       

if resultado==True:
    print("Sobresaliente")
else:
    print("GG anyways")