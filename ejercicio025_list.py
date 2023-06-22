import requests
#import json #Es de las librerías estándar de Python
KEY = 'b55b0696'
URL = 'http://www.omdbapi.com'
titulo = input("Título de la película:")
#http://www.omdbapi.com/?apikey=95c08eba&t=Batman
parametros = {'apikey': KEY, 't': titulo}
r = requests.get(URL, params=parametros)
if r.status_code==200:#200 es el código OK de HTTP
    # Title , Director, Plot, Year y Actors
    pelicula_dict = r.json()
    pelicula_dict["Actors"].split
    print(pelicula_dict.get("Title","No dispongo de director"))
    print(pelicula_dict.get("Director","No dispongo de director"))
    print(pelicula_dict.get("Plot","No dispongo de director"))
    print(pelicula_dict.get("Year","No dispongo de director"))

    for actor in pelicula_dict.get("Actors","No dispongo de director"):
        print(actor)
        

