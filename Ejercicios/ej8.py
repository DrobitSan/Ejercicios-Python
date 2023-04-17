'''
8.- Programa que dado dos intervalos cerrados [a, b] y [c, d] de la recta real devuelve la
intersección de ambos intervalos.
'''


intervalo1= input("introducir intervalo 1 sin corchetes:")
intervalo2= input("introducir intervalo 2 sin corchetes:")

inter1_list= intervalo1.split(",")
inter2_list= intervalo2.split(",")

def interseccion(a,b,c,d):
    a=int
    b=int
    c=int
    d=int
    
    if a<b<c<d or c<d<a<b:
        return "No existe interseccion"
    elif a<c<d<b:
        return [c,d]
    elif c<a<b<d:
        return [a,b]
    elif c<a<d<b:
        return [a,d]
    elif a<c<b<d:
        return [b,c]


resultado= interseccion(inter1_list[0], inter1_list[1], inter2_list[0], inter2_list[1])


print(resultado)