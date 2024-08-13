# 15. Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, can-
# tidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y ade-
# más la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver
# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
from lista import search, show_list_list, by_name, by_torneos, by_nivel
from random import choice

entrenadores = [
    {'nombre': 'Leon', 'torneos ganados': 5 , 'batallas perdidas': 2 , 'batallas ganadas': 10 },
    {'nombre': 'Ash Ketchum', 'torneos ganados': 3 , 'batallas perdidas': 5 , 'batallas ganadas': 2 },
    {'nombre': 'Goh', 'torneos ganados': 4 , 'batallas perdidas': 1 , 'batallas ganadas': 3 },
    {'nombre': 'Chloe', 'torneos ganados': 2 , 'batallas perdidas': 3 , 'batallas ganadas': 5 },
]

nombres = ['Leon', 'Ash Ketchum', 'Goh', 'Chloe']

pokemons = [
    {"nombre": "Pikachu", "nivel": 35, "tipo": "Eléctrico", "subtipo": None},
    {"nombre": "Charizard", "nivel": 40, "tipo": "Fuego", "subtipo": "Volador"},
    {"nombre": "Bulbasaur", "nivel": 30, "tipo": "Planta", "subtipo": "Veneno"},
    {"nombre": "Starmie", "nivel": 30, "tipo": "Agua", "subtipo": "Psíquico"},
    {"nombre": "Nidoking", "nivel": 40, "tipo": "Veneno", "subtipo": "Tierra"},
    {"nombre": "Tyrantrum", "nivel": 35, "tipo": "Agua", "subtipo": "Volador"},
    {"nombre": "Geodude", "nivel": 28, "tipo": "Roca", "subtipo": "Tierra"},
    {"nombre": "Vulpix", "nivel": 20, "tipo": "Fuego", "subtipo": None},
    {"nombre": "Blastoise", "nivel": 50, "tipo": "Agua", "subtipo": None},
    {"nombre": "Umbreon", "nivel": 45, "tipo": "Siniestro", "subtipo": None},
]

lista_entrenadores = []

for entrenador in entrenadores:
    entrenador.update({'sublist': []})
    lista_entrenadores.append(entrenador)

for pokemon in pokemons:
    pos = search(lista_entrenadores, 'nombre', choice(nombres))
    if pos is not None:
        lista_entrenadores[pos]['sublist'].append(pokemon)
    else:
        print('No existe el entrenador.')

lista_entrenadores.sort(key=by_name)

show_list_list('Entrenadores', 'Pokemons', lista_entrenadores)

# a. obtener la cantidad de Pokémons de un determinado entrenador;
def obtener_cantidad(nombre_entrenador):
        pos = search(lista_entrenadores, 'nombre', nombre_entrenador)
        if pos is not None:
             return len(lista_entrenadores[pos]['sublist'])
        else:
             return print('No se encontró al entrenador.')
        
print(obtener_cantidad('Goh'))


# b. listar los entrenadores que hayan ganado más de tres torneos;
def mas_tres_torneos(entrenadores):
    tres_torneos = []
    for entrenador in entrenadores:
        if entrenador['torneos ganados'] > 3:
            tres_torneos.append({
                 'nombre': entrenador['nombre'],
                 'torneos ganados' : entrenador['torneos ganados']
            })
    return tres_torneos
     
print('Entrenadores que han ganado mas de 3 batallas:')
print(mas_tres_torneos(lista_entrenadores))
          

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
def mayor_nivel(entrenadores):
    max_torneos = 0
    entrenador_mas_torneos = None
    pokemon_mayor_nivel = None

    for entrenador in entrenadores:
        if entrenador['torneos ganados'] > max_torneos:
            max_torneos = entrenador['torneos ganados']
            entrenador_mas_torneos = entrenador
            pokemon_mayor_nivel = max(entrenador['sublist'], key=lambda x: x['nivel'])

    return pokemon_mayor_nivel

print('Pokemon de mayor nivel del entrenador con mayor cantidad de torneos ganados:')
print(mayor_nivel(lista_entrenadores))


# d. mostrar todos los datos de un entrenador y sus Pokémos;
def mostrar_datos(entrenadores, nombre_entrenador):

    for entrenador in entrenadores:
        if entrenador['nombre'] == nombre_entrenador:
            print('Entrenador:', entrenador['nombre'])
            print('Torneos ganados:', entrenador['torneos ganados'])
            print('Batallas perdidas:', entrenador['batallas ganadas'])
            print('Batallas perdidas:', entrenador['batallas perdidas'])
            print('Pokemons:')
            for pokemon in entrenador['sublist']:
                print('Nombre:', pokemon['nombre'], 'Nivel:', pokemon['nivel'], 'tipo:', pokemon['tipo'])
            break
        
mostrar_datos(lista_entrenadores, 'Leon')



# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
def entrenadores_porcentaje(entrenadores):
    for entrenador in entrenadores:
        porcentaje = (entrenador['batallas ganadas'] * 100.0 / (entrenador['batallas ganadas'] + entrenador['batallas perdidas']))
        if porcentaje > 79 :
            print('Entrenador:', entrenador['nombre'])
            print('Batallas ganadas:', entrenador['batallas ganadas'])
            break

print('Entrenadores cuyo porcentaje de batallas ganados es mayor al 79%:')
entrenadores_porcentaje(lista_entrenadores)

# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
def entrenadores_pokemons(entrenadores):
    for entrenador in entrenadores:
        nombre_entrenador = entrenador['nombre']
        pokemons = entrenador['sublist']
        for pokemon in pokemons:
            tipo_pokemon = pokemon['tipo']
            subtipo_pokemon = pokemon['subtipo']
            if tipo_pokemon == 'Fuego' or tipo_pokemon == 'Planta':
                print('Entrenador:', nombre_entrenador)
                print('Pokemon:', pokemon['nombre'], 'tipo:', pokemon['tipo'], 'subtipo:', pokemon['subtipo'])
            elif tipo_pokemon == 'Agua' and subtipo_pokemon == 'Volador':
                print('Entrenador:', nombre_entrenador)
                print('Pokemon:', pokemon['nombre'], 'tipo:', pokemon['tipo'], 'subtipo:', pokemon['subtipo'])
            break

print('Entrenadores con pokemons de tipo fuego y planta o agua/volador:')
entrenadores_pokemons(lista_entrenadores)

# g. el promedio de nivel de los Pokémons de un determinado entrenador;
def promedio_nivel(entrenadores, nombre_entrenador):
    for entrenador in entrenadores:
        if entrenador['nombre'] == nombre_entrenador:
            pokemons = entrenador['sublist']
            total_niveles = 0
            total_pokemons = len(pokemons)
            for pokemon in pokemons:
                total_niveles += pokemon['nivel']
            promedio = total_niveles / total_pokemons
            return promedio
            
nombre_entrenador = 'Leon'
print('El promedio de nivel de los pokemons de', nombre_entrenador, 'es:', promedio_nivel(lista_entrenadores, nombre_entrenador) )

# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
def entrenadores_pokemon(entrenadores, nombre_pokemon):
    for entrenador in entrenadores:
        cantidad_entrenadores = 0
        pokemons = entrenador['sublist']
        for pokemon in pokemons:
            if pokemon['nombre'] == nombre_pokemon:
                cantidad_entrenadores += 1
        return cantidad_entrenadores

nombre_pokemon = 'Pikachu'
print('Cantidad de entrenadores que tienen a ', nombre_pokemon, ':', entrenadores_pokemon(lista_entrenadores, nombre_pokemon))

# i. mostrar los entrenadores que tienen Pokémons repetidos;
def pokemons_repetidos(entrenadores):
    entrenadores_repetidos = []
    nombres_pokemons = []
    for entrenador in entrenadores:
        pokemons = entrenador['sublist']
        for pokemon in pokemons:
            nombres_pokemons.append(pokemon['nombre'])
    if len(nombres_pokemons) != len(set(nombres_pokemons)):
        entrenadores_repetidos.append(entrenador['nombre'])
        print('Los entrenadores que tienen pokemons repetidos son:', entrenadores_repetidos)
    else:
        print('No hay entrenadores con pokemons repetidos.')
            
pokemons_repetidos(lista_entrenadores)


# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-
# rrakion o Wingull;
def entrenadores_TTW(entrenadores):
    for entrenador in entrenadores:
        pokemons = entrenador['sublist']
        for pokemon in pokemons:
            if pokemon['nombre'] == 'Tyrantrum' or pokemon['nombre'] == 'Terrakion' or pokemon['nombre'] == 'Wingull':
                print('Nombre:', entrenador['nombre'])
                break

print('Los entrenadores que tienen los pokemons Tyrantrum, Terrakion o Wingull son:')
entrenadores_TTW(lista_entrenadores)


# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;
def entrenadorx_pokemony(entrenadores, entrenadorx, pokemony):
    for entrenador in entrenadores:
        if entrenador['nombre'] == entrenadorx:
            pokemons = entrenador['sublist']
            pokemon_encontrado = False
            for pokemon in pokemons:
                if pokemon['nombre'] == pokemony:
                    pokemon_encontrado = True
                    print('Datos de entrenador:')
                    print('Nombre:', entrenador['nombre'])
                    print('Torneos ganados:', entrenador['torneos ganados'])
                    print('Batallas ganadas:', entrenador['batallas ganadas'])
                    print('Batallas perdidas:', entrenador['batallas perdidas'])
                    print('Datos de pokemon:')
                    print('Nombre:', pokemon['nombre'])
                    print('Nivel:', pokemon['nivel'])
                    print('Tipo', pokemon['tipo'])
                    print('Subtipo', pokemon['subtipo'])
            if not pokemon_encontrado:
                print('El entrenador no tiene al pokemon ingresado.')
            break
            

entrenadorx = 'Leon'
pokemony = 'Umbreon'
entrenadorx_pokemony(lista_entrenadores, entrenadorx, pokemony)