#Factorial de un numero entero positivo

numero=int(input("Calcular factorial de:"))

def fact_fun(n):
    if n >1:
        return n *fact_fun(n -1)
    else:
        return 1

factorial= fact_fun(numero)   

print(factorial)
