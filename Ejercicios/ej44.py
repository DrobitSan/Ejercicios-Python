'''
44.- Escribir un programa que devuelve la forma plural de la palabra española que se le
pase.
'''



singular=input("Introducir singular: ")
if singular[-1]== ("a"or"e"or"i"or"o"or"u"):
    plural=singular+"s"
else:
    plural=singular+"es"

print(plural)