'''
7.- Programa que obtiene el cociente y el resto de dos números enteros y positivos
mediante restas sucesivas. A y B son las variables para leer datos de entrada (dividendo
y divisor), C es la variable para calcular el cociente. En A se guardará el resto. (Nota: La
división entre 0 no está definida).
'''




dividendo= int(input("Introducir dividendo:"))
divisor= int(input("Introducir divisor:"))

cociente= int(0)
resto= int(0)
n= dividendo

while n > divisor:
    n -= divisor
    cociente += 1
    resto = n

print("Cociente= "+ str(cociente))
print("Resto= "+ str(resto))
