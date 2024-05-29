# Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:


from pila import Stack

pila_personajes = Stack()

personajes = [
    {"nombre": 'Iron Man', "peliculas": 11 },
    {"nombre": 'Capitan America', "peliculas": 9 },
    {"nombre": 'Thor', "peliculas": 8 },
    {"nombre": 'Groot', "peliculas": 5 },
    {"nombre": 'Hulk', "peliculas": 6 },
    {"nombre": 'Black Widow', "peliculas": 8 },
    {"nombre": 'Spider-Man', "peliculas": 5 },
    {"nombre": 'Doctor Strange', "peliculas": 3 },
    {"nombre": 'Scarlet Witch', "peliculas": 5 },
    {"nombre": 'Black Panther', "peliculas": 4 },
    {"nombre": 'Capitan Marvel', "peliculas": 2 },
    {"nombre": 'Rocket Raccoon', "peliculas": 5 },
    
]

for personaje in personajes:
    pila_personajes.push(personaje)


print(pila_personajes)

# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
# ción uno la cima de la pila;


def encontrar_posicion(pila, nombre):
    posicion_Rocket = None
    posicion_Groot = None
    for i, personaje in enumerate(personajes):
        if personaje["nombre"] == "Rocket Raccoon":
            posicion_Rocket = i + 1
        if personaje["nombre"] == "Groot":
            posicion_Groot = i + 1
    return posicion_Rocket, posicion_Groot
    
posicion_Rocket = encontrar_posicion(pila_personajes, "Rocket Raccoon")

posicion_Groot = encontrar_posicion(pila_personajes, "Groot")


print("La posición en que se encuentra Rocket Raccoon es:", posicion_Rocket)

print("La posición en que se encuentra Groot es:", posicion_Groot)



# b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
# car la cantidad de películas en la que aparece;

def mas_5_pelis(personajes):
    resultado = {}
    for personaje in personajes:
        if personaje["peliculas"] > 5:
            resultado[personaje["nombre"]] = personaje["peliculas"]
    return resultado

resultado = mas_5_pelis(personajes)

print("Los personajes que participaron en más de 5 peliculas de la saga son:", resultado)



# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
def viuda_negra(personajes):
    for personaje in personajes:
        if personaje["nombre"] == "Black Widow":
            pelicula_blackwidow = personaje["peliculas"]
    return pelicula_blackwidow

pelicula_blackwidow = viuda_negra(personajes)

print("La Viuda Negra participó en ", pelicula_blackwidow, " peliculas")



# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

def personajes_iniciales(pila, iniciales):
    pila_aux = Stack()
    resultado = []
    while pila.size() > 0:
        personaje = pila.pop()
        if personaje["nombre"][0] in iniciales:
            resultado.append(personaje["nombre"])
        pila_aux.push(personaje)

    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

    return resultado

iniciales = ['C', 'D', 'G']
personajes_encontrados = personajes_iniciales(pila_personajes, iniciales)
print("Personajes cuyos nombres empiezan con C, D y G:", personajes_encontrados)