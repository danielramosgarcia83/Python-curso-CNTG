#Función que calcule la suma de dos números
def suma(n1,n2):
    return n1+n2

#Función que calcule la suma de un número indeterminado de números
def suma(*arg1,*arg2):
    return arg1+arg2


#Función que escriba en un fichero un texto

def escribir_fichero(texto,fichero):
    open(fichero,'w')
        f.write(texto)
        
#Función que traduzca un texto a un idioma
def traducir(texto,idioma):
    if idioma == 'es':
        return texto.replace('a','á').replace('e','é').replace('i','
                                                               
#Función que calcule el número de primitiva de la próxima semana3
def proxima_semana(dia,mes,año):
    
#Función que proporciona el pronóstico del tiempo de una semana determinada en un lugar concreto