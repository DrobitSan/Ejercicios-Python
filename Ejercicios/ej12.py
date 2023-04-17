'''
12.- Escribe un programa C que lea como dato de entrada una fecha expresada en días
(1-31), mes (1-12) y año (en nº) y nos dice la fecha que será al día siguiente. Se supone
que febrero siempre tiene 28 días.
'''


fecha= input("Introducir fecha en formato DD/MM/YY:")

lista_fecha= fecha.split("/")


dia=int(lista_fecha[0])
mes=int(lista_fecha[1])
año=int(lista_fecha[2])
bisiestro=bool

meses_31= [1,3,5,7,8,10,12]
meses_30= [4,6,9,11]
meses_28= [2]



if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    bisiestro = True
    print("Es bisiesto")
else:
    bisiestro = False
    print("No es bisiesto")



if mes == 2 and ((bisiestro and dia<29) or (bisiestro == False and dia<28)):
    dia += 1

elif mes == 2 and ((bisiestro and dia==29) or (bisiestro == False and dia==28)):
    dia = 1
    mes += 1


elif (mes in meses_30) and dia < 30:
    dia += 1

elif (mes in meses_30) and dia == 30 and mes < 12:
    dia = 1
    mes += 1

elif (mes in meses_30) and dia == 30 and mes == 12:
    año += 1
    mes = 1
    dia = 1




elif (mes in meses_31) and dia < 31:
    dia += 1

elif (mes in meses_31) and dia == 31 and mes < 12:
    dia = 1
    mes += 1

elif (mes in meses_31) and dia == 31 and mes == 12:
    año += 1
    mes = 1
    dia = 1

print(str(dia)+"/"+str(mes)+"/"+str(año))





















