#Calcular mcd de dos numeros 

print("Programa que calcula el mcd de A y B")
a = int(input("introducir A:"))
b = int(input("Introducir B:"))

while a < b:
    print("A debe ser mayor que B")
    a = int(input("introducir A:"))
    b = int(input("Introducir B:"))

def mcd(dd,d):
    q = dd//d
    r = dd%d

    if r != 0:
        dd = d
        d = r
        return mcd(dd,d)

    elif r == 0:
        return d

print(mcd(a,b))







