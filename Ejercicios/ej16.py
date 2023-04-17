#Calcular minimo comun multiplo

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

def mcm(a,b):
    return int(a*b/mcd(a,b))

print(mcm(a,b))