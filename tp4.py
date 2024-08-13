# Escribir un algoritmo que permita utilizar tres tablas hash para guardar los datos de Pokémons,
# que contemple las siguientes actividades: 

# a. en la primera tabla hash la función hash debe ser sobre el tipo de Pokémon, en la segunda
# tabla la función hash deberá utilizar el ultimo dígito del número del Pokémon como clave y la tercera
# sera en base  a su nivel repartiéndolos en 10 posiciones dentro de la tabla; 

# b. debe utilizar tablas hash abiertas con listas como estructura secundaria;
# c. si el Pokémon es de más de un tipo deberá cargarlo en cada uno de las tabla que indiquen estos tipos;

# d. deberá permitir cargar Pokémons de los cuales se dispone de su número, nombre, tipo/s, nivel.

# e. mostrar todos los Pokémons cuyos numeros terminan en 3, 7 y 9;

# f. mostrar todos los Pokémons cuyos niveles son multiplos de 2, 5 y 10;

# g. mostrar todos los Pokémons de los siguientes tipo: Acero, Fuego, Electrifico, Hielo

pokemons = [
    {'nombre': 'Weedle', 'tipo': 'bicho/veneno', 'nivel': 12, 'numero': 13 },
    {'nombre': 'Tadbulb', 'tipo': 'electrico', 'nivel': 5, 'numero': 938 },
    {'nombre': 'Bulbasaur', 'tipo': 'planta/veneno', 'nivel': 2, 'numero': 1 },
    {'nombre': 'Krokorok', 'tipo': 'tierra/siniestro', 'nivel': 15, 'numero': 552 },
    {'nombre': 'Swirlix', 'tipo': 'hada', 'nivel': 3, 'numero': 684 },
    {'nombre': 'Alakazam', 'tipo': 'psiquico', 'nivel': 7, 'numero': 65 },
    {'nombre': 'Lombre', 'tipo': 'agua/planta', 'nivel': 8, 'numero': 271 },
    {'nombre': 'Gliscor', 'tipo': 'tierra/volador', 'nivel': 10, 'numero': 472 }
]


def hash_tipo(pokemons):
    return pokemon['tipo']

def hash_digito(pokemons):
    return pokemon['numero'] % 10

def hash_nivel(pokemons):
    return pokemon['nivel'] % 10


tabla_tipo = {}
tabla_digito = {}
tabla_nivel = {}

for pokemon in pokemons:
    valor = hash_tipo(pokemon)
    if valor not in tabla_tipo:
        tabla_tipo[valor] = []
    tabla_tipo[valor].append(pokemon)


for pokemon in pokemons:
    valor = hash_digito(pokemon)
    if valor not in tabla_digito:
        tabla_digito[valor] = []
    tabla_digito[valor].append(pokemon)

for pokemon in pokemons:
    valor = hash_nivel(pokemon)
    if valor not in tabla_nivel:
        tabla_nivel[valor] = []
    tabla_nivel[valor].append(pokemon)


print("Pokémons cuyos números terminan en 3, 7 y 9:")
for i in [3, 7, 9]:
    if i in tabla_digito:
        for pokemon in tabla_digito[i]:
            print(pokemon)


print("Pokémons cuyos niveles son multiplos de 2, 5 y 10:")
for i in range(10):
    if i % 2 == 0 or i % 5 == 0 or i % 10 == 0:
        if i in tabla_nivel:
            for pokemon in tabla_nivel[i]:
                print(pokemon)


print("Pokémons de tipo Acero, Fuego, Electrifico, Hielo:")
for tipo in ["Acero", "Fuego", "Electrifico", "Hielo"]:
    if tipo in tabla_tipo:
        for pokemon in tabla_tipo[tipo]:
            print(pokemon)