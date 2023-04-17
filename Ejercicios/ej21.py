'''
21.-Escribe un programa C que, dado un número entero positivo y lo devuelva al revés.
Por ejemplo, si el número de entrada es 1234, la rutina debería devolver 4321.
'''


num= input("Introducir numero entero:")

x=[]

for n in reversed(num):
    x.append(n)

invertido= "".join(x)

print(invertido)