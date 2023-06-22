#Ejecutar previamente: pip install gTTS
from gtts import gTTS
import os
usu=input("Cual es tu nombre?: ")
gen=input("Eres H/M?:").upper()

if gen=='H':
    mytext = f'Hola {usu}, eres mi amo y señor y te obedeceré en todo lo que quieras'
else:
    mytext = f'Hola {usu}, eres mi ama y señora y te obedeceré en todo lo que quieras'
language = 'es'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("locucion.mp3")
os.system("start locucion.mp3")#No funciona en Linux
#Preguntar al usuario su nombre.
#Preguntar al usuario si es H/M/?
#Hola Fernando, eres mi amo y señor y te obedeceré en todo lo que quieras
#Hola Vanessa, eres mi ama y señora y te obedeceré en todo lo que quieras