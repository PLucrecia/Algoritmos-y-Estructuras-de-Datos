# 11. Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
# de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:



from Cola import Queue

class Personaje:
    def __init__(self, nombre, planeta):
        self.nombre = nombre
        self.planeta = planeta

personajes = Queue()

personajes.arrive(Personaje("Luke Skywalker", "Tatooine")),
personajes.arrive(Personaje("Han Solo", "Corellia")),
personajes.arrive(Personaje("Leia Organa", "Alderaan")),
personajes.arrive(Personaje("Yoda", "Dagobah")),
personajes.arrive(Personaje("Jar Jar Binks", "Naboo")),
personajes.arrive(Personaje("Chewbacca", "Kashyyyk"))


# a. mostrar los personajes del planeta Alderaan, Endor y Tatooine

def mostrar_personajes(cola, planeta):
    size = cola.size()
    for i in range(size):
        personaje = cola.on_front()
        if personaje.planeta in planeta:
            print (f'{personaje.nombre} es del planeta {personaje.planeta}')
        cola.move_to_end()

mostrar_personajes(personajes, "Alderaan")
mostrar_personajes(personajes, "Endor")
mostrar_personajes(personajes, "Tatooine")

print(' ')


# b. indicar el plantea natal de Luke Skywalker y Han Solo
def mostrar_planeta(cola, nombre):
    size = cola.size()
    for i in range(size):
        personaje = cola.on_front()
        if personaje.nombre in nombre:
            print(f'{personaje.nombre} es del planeta {personaje.planeta}')
        cola.move_to_end()

print("Planetas natales de Luke Skywalker y Han Solo:")
mostrar_planeta(personajes, ["Luke Skywalker", "Han Solo"])

print(' ')


# c. insertar un nuevo personaje antes del maestro Yoda
def insertar_antes_de_yoda(cola, nuevo_personaje):
    size = cola.size()
    yoda_encontrado = False

    for i in range(size):
        personaje = cola.on_front()

        if personaje.nombre == "Yoda" and not yoda_encontrado:
            cola.arrive(nuevo_personaje)
            yoda_encontrado = True

        cola.move_to_end()

nuevo_personaje = Personaje("Obi-Wan Kenobi", "Stewjon")

insertar_antes_de_yoda(personajes, nuevo_personaje)

print('Insertamos un nuevo personaje antes del maestro Yoda:')
for i in range(personajes.size()):
    personaje = personajes.on_front()
    print(f'{personaje.nombre} es del planeta {personaje.planeta}')
    personajes.move_to_end()

print(' ')


# d. eliminar el personaje ubicado después de Jar Jar Binks
def eliminar_despues_de_jarjar(cola):
    size = cola.size()
    eliminar_siguiente = False

    for i in range(size):
        personaje = cola.on_front()

        if eliminar_siguiente:
            eliminar_siguiente = False
            cola.attention()
        else:
            if personaje.nombre == "Jar Jar Binks":
                eliminar_siguiente = True
            cola.move_to_end()

eliminar_despues_de_jarjar(personajes)

print('Eliminamos el personaje ubicado despues de Jar Jar Binks:')
for i in range(personajes.size()):
    personaje = personajes.on_front()
    print(f'{personaje.nombre} es del planeta {personaje.planeta}')
    personajes.move_to_end()

print(' ')
