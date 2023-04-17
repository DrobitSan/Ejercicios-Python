#Evaluar polinomio de grado n

valor_x = int(input("Introducir valor x:"))

grado = int(input("Grado del polinomio:"))

coeficientes = input("Introducir valor de los coeficientes desde 0 hasta el grado, separados por comas:")



def evaluar(valor_x, grado, coeficientes):
    lista_coeficientes= [int(i) for i in coeficientes.split(",")]
    resultado = 0

    while grado >= 0:
        resultado += lista_coeficientes[grado] * (valor_x ** grado)
        grado -= 1

    return resultado


print(evaluar(valor_x, grado, coeficientes))



