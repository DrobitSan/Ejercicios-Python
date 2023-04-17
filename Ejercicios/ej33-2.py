'''
33.- Generar un número de cuatro cifras (no debe repetirse ninguna de ellas).
Realizar un programa para adivinar el número anterior. Se introducirá otro número de
cuatro cifras (sin repetir ninguna) y se comparará con el generado anteriormente. Si
coincide la cifra y la posición se indicará con el signo “+”, si coincide sólo la cifra (y no
la posición) se indicará con el signo “-”.

Ej:
7 2 1 4 (número generado, que no aparecerá en pantalla)
2 0 6 4 (número que introduce el usuario)

A la derecha del número introducido aparecerá un signo “+” (el 4 está acertado y
además está en su sitio) y un signo “-” el 2 está acertado, pero no está en su sitio.

Se darán diez oportunidades para adivinar el número, si no se consigue en este plazo se
mostrará dicho por pantalla.

Tanto si se adivina el número como si no se dará la posibilidad de jugar de nuevo.
'''



import random 

print("Juego: Trata de adivinar un numero de 4 digitos enteros, si fallas se te dará una pista y tienes que lograrlo en 10 intentos o menos.")

def compr_aleatorio(n, aleatorio):
    for i in aleatorio:
        if i == str(n):
            return False
    return True


def generar_aleatorio():
    aleatorio= ""
    while len(aleatorio)<4:
        n= random.randint(0,9)
        if compr_aleatorio(n, aleatorio):
            aleatorio += str(n)       
    return aleatorio

def generar_pista(aleatorio,intento):
    num="0000"
    for n in range(len(intento)):
        for i in range(len(aleatorio)):
            
                








_n_intentos=0
while _n_intentos<10:
    _n_intentos += 1
    _intento= input("Introducir intento:")

    if _n_intentos==1:
        if generar_aleatorio()==_intento:
            print("Enhorabuena, has acertado el numero")
        else:
            print("Vaya, parece que no has acertado, te vamos a dar una pista\n")
            print("Los numeros que acertados que esten en suu lugar saldran con un + a la derechaªn") 
            print("Los acertados pero en lugarincorrecto saldran con un - a la izquierda\n")
            print("Y los numeros que no hayas acertado saldran sin modificaciones")
            input("Presiona ENTER para generar la pista")

