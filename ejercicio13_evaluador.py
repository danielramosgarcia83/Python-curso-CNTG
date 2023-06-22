nombre="Roberto"
edad=30
altura=180
japones=True
ruso=False
#Mayor de edad, medir más de 150, hablar japonés y/o ruso
#El nombre no puede contener la letra a
if edad>18 and altura>150 and (japones==True or ruso==True) and nombre.count("a")==False:
    print("Contratado")
else:
    print("No cumple los requisitos")
