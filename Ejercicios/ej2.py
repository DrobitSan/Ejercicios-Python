'''
2.- Programa que recibe como dato de entrada una hora expresada horas, minutos y
segundos y escribe la nueva hora transcurrido 1 segundo. Controlar el valor de las
entradas.
'''

hora= input("Introducir hora")

hora_split= hora.split(":")

hora_int= []

for n in hora_split:
    hora_int.append(int(n))


def sumar_segundo(hh,mm,ss):
    if ss < 59:
        return [hh, mm, ss + 1]
    elif ss==59:
        if mm<59:
            return [hh, mm+ 1, 00]
        elif mm==59:
            if hh<23:
                return [hh+1, 00, 00]
            elif hh==23:
                return [00, 00, 00]
                            
     

new_hora= sumar_segundo(hora_int[0],hora_int[1], hora_int[2])

print(str(new_hora[0]) +":"+ str(new_hora[1]) + ":" + str(new_hora[2]))


