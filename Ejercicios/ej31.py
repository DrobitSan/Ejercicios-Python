'''
31.- Programa que lee un vector de N elementos y rota todas sus componentes un lugar
hacia su derecha. Teniendo en cuenta que la última componente se ha de desplazar al
primer lugar.
'''


entrada=input("Introducir elementos del vector separados por comas:")
vector= entrada.split(",")
print(vector)
nuevo= vector[len(vector)-1]
vector.pop()
vector.insert(0,nuevo)
print(vector)

#pop() eliminar ultimo elemento de la lista