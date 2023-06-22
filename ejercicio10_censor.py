import lector_palabras

palabras_prohibidas= lector_palabras.get_lines_from_file("palabras_prohibidas.txt")
mensaje=input("Introduce un mensaje:")

for improperio in palabras_prohibidas:
    print(improperio)

    if improperio==mensaje:
        print("La palabra es prohibida")
        break
    else:
        print("La palabra no es prohibida")
    