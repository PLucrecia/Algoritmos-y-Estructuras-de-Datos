# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (), de los cuales se cono-
# ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
# F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
# manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

from Cola import Queue

class Personaje:
    def __init__(self, nombre, superheroe, genero):
        self.nombre = nombre
        self.superheroe = superheroe
        self.genero = genero

personajes = Queue()

personajes.arrive(Personaje("Tony Stark", "Iron Man", "M")),
personajes.arrive(Personaje("Steve Rogers", "Capitan America", "M")),
personajes.arrive(Personaje("Natasha Romanoff", "Black Widow", "F")),
personajes.arrive(Personaje("Carol Danvers", "Capitana Marvel", "F")),
personajes.arrive(Personaje("Scott Lang", "Ant-Man", "M")),
personajes.arrive(Personaje("Sam Wilson", "Falcon", "M")),
personajes.arrive(Personaje("Sharon Carter", "Agent 13", "F"))


# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
def personaje_capitana_marvel(cola):
    size = cola.size()
    for i in range(size):
        personaje = cola.on_front()
        if personaje.superheroe == "Capitana Marvel":
            print(f'El nombre del personaje de la superheroe Capitana Marvel es: {personaje.nombre}')
        cola.move_to_end()

personaje_capitana_marvel(personajes)

print(' ')


# b. mostrar los nombre de los superhéroes femeninos;
def superheroes_femeninos(cola):
    size = cola.size()
    for i in range(size):
        personaje = cola.on_front()
        if personaje.genero == 'F':
            print(personaje.superheroe)
        cola.move_to_end()

print(f'Los superheroes femeninos son:')
superheroes_femeninos(personajes)

print(' ')


# c. mostrar los nombres de los personajes masculinos;
def personajes_masculinos(cola):
    size = cola.size()
    for i in range(size):
        personaje = cola.on_front()
        if personaje.genero == 'M':
            print(personaje.nombre)
        cola.move_to_end()

print(f'Los nombres de los personajes masculinos son:')
personajes_masculinos(personajes)

print(' ')


# d. determinar el nombre del superhéroe del personaje Scott Lang;
def superheroe_scott_lang(cola):
    size = cola.size()
    for i in range(size):
        personaje = cola.on_front()
        if personaje.nombre == "Scott Lang":
            print(f'El nombre del superheroe del personaje Scott Lang es: {personaje.superheroe}')
        cola.move_to_end()

superheroe_scott_lang(personajes)

print(' ')


# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
def nombres_letra_s(cola):
    size = cola.size()
    for i in range(size):
        personaje = cola.on_front()
        if personaje.nombre.startswith("S") or personaje.superheroe.startswith("S"):
            print(f'Nombre: {personaje.nombre}, Superheroe: {personaje.superheroe}, Genero: {personaje.genero}')
        cola.move_to_end()

nombres_letra_s(personajes)

print(' ')


# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.
def personaje_carol_danvers(cola):
    size = cola.size()
    encontrado = False
    for i in range(size):
        personaje = cola.on_front()
        if personaje.nombre == "Carol Danvers":
            print(f'El nombre del superheroe del personaje Carol Danvers es: {personaje.superheroe}')
            encontrado = True
        cola.move_to_end()
    if not encontrado:
        print("El personaje Carol Danvers no se encuentra en la cola.")

personaje_carol_danvers(personajes)

