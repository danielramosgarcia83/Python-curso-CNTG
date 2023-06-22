#Operador in
#'El regreso de la momia'
#'momia' in titulo
palabras_prohibidas = "momia vampiro ajo clavo estaca"
palabra = input("Introduce una palabra:")
#Indicar si la palabra introducida está o no prohibida (sin importar si es mayúsculas o minúsculas)
'''
if (edad>=18):
    print("Enhorabuena")
    print("Eres mayor de edad")
else:
    print("Lo siento")
    print("Eres menor de edad")
'''
if palabra in palabras_prohibidas.lower():
    print("La palabra esta prohibida")
if palabra in palabras_prohibidas.upper():
    print("La palabra esta prohibida")
else:
    print("La palabra no esta prohibida")
