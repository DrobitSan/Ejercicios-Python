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



import random as rd
           
def puto_aleatorio():
    lista= []
    while len(lista) < 4:
        n= rd.randint(0,9)
        l_comprobaciones=[]
        if len(lista) == 0:
            lista.append(n)
        else:
            for i, j in enumerate(lista):               
                if n != j:
                    l_comprobaciones.append(True)
                else: l_comprobaciones.append(False)
        if all(l_comprobaciones) and len(l_comprobaciones) > 0:
            lista.append(n)
    return lista


def n_a_lista(n_acierto):
    l_acierto= list(n_acierto) 
    for n in range(len(l_acierto)):
        l_acierto[n]= int(l_acierto[n])
    return l_acierto
   
def pista(n_generado, l_acierto):     
    nueva_l= l_acierto.copy()    
    for x, y in enumerate(l_acierto):
        for i, j in enumerate(n_generado):
            if l_acierto[x] == n_generado[i]:
                nueva_l[x] = str(j) +"-"
        if l_acierto[x] == n_generado[x]:
            nueva_l[x]= str(y) +"+"          
    return nueva_l

_intentos=0
_resultado=False
print("Juego: Trata de adivinar un numero de 4 digitos enteros, si fallas se te dará una pista y tienes que lograrlo en 10 intentos o menos.")
_n_generado=puto_aleatorio()
while _intentos < 10 and not _resultado:
    _intentos += 1
    print("Intento nº:"+str(_intentos))
    _acierto= input("Introducir numero:")
    if _n_generado== n_a_lista(_acierto):
        _resultado=True
        print("Enhorabuena, has acertado")
    else:
        if _intentos==1:
            print("Vaya, parece que no has acertado, te vamos a dar una pista")
            print("Los numeros acertados que esten en su lugar saldrán con un + a la derecha") 
            print("Los acertados pero en lugar incorrecto saldran con un - a la izquierda")
            print("Y los numeros que no hayas acertado saldran sin modificaciones")
            input("Presiona ENTER para generar la pista")    
            print(pista(_n_generado,n_a_lista(_acierto))) 
        else:
            print("Vaya, parece que no has acertado, pista:")   
            print(pista(_n_generado,n_a_lista(_acierto)))






    




                

