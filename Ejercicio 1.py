from arbol_avl import BinaryTree

# 1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
# de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir
# tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:

pokemons = [
    {
        "nombre": "Pikachu",
        "numero": 25,
        "tipo": ["Eléctrico"]
    },
    {
        "nombre": "Charmander",
        "numero": 4,
        "tipo": ["Fuego"]
    },
    {
        "nombre": "Bulbasaur",
        "numero": 1,
        "tipo": ["Planta", "Veneno"]
    },
    {
        "nombre": "Squirtle",
        "numero": 7,
        "tipo": ["Agua"]
    },
    {
        "nombre": "Lucario",
        "numero": 448,
        "tipo": ["Lucha", "Acero"]
    },
    {
        "nombre": "Greninja",
        "numero": 658,
        "tipo": ["Agua", "Siniestro"]
    },
    {
        "nombre": "Rowlet",
        "numero": 722,
        "tipo": ["Planta", "Volador"]
    },
    {
        "nombre": "Jolteon",
        "numero": 810,
        "tipo": ["Planta"]
    },
    {
        "nombre": "Sobble",
        "numero": 816,
        "tipo": ["Agua"]
    },
    {
        "nombre": "Talonflame",
        "numero": 663,
        "tipo": ["Fuego", "Volador"]
    },
    {
        "nombre": "Togekiss",
        "numero": 468,
        "tipo": ["Hada", "Volador"]
    },
    {
        "nombre": "Dragapult",
        "numero": 887,
        "tipo": ["Dragón", "Fantasma"]
    },
    {
        "nombre": "Incineroar",
        "numero": 727,
        "tipo": ["Fuego", "Siniestro"]
    },
    {
        "nombre": "Garchomp",
        "numero": 445,
        "tipo": ["Dragón", "Tierra"]
    },
    {
        "nombre": "Corviknight",
        "numero": 823,
        "tipo": ["Volador", "Acero"]
    },
    {
        "nombre": "Rillaboom",
        "numero": 812,
        "tipo": ["Planta"]
    },
    {
        "nombre": "Cinderace",
        "numero": 815,
        "tipo": ["Fuego"]
    },
    {
        "nombre": "Toxtricity",
        "numero": 849,
        "tipo": ["Eléctrico", "Veneno"]
    },
    {
        "nombre": "Zacian",
        "numero": 888,
        "tipo": ["Hada", "Acero"]
    },
    {
        "nombre": "Zamazenta",
        "numero": 889,
        "tipo": ["Lucha", "Acero"]
    },
    {
        "nombre": "Eternatus",
        "numero": 890,
        "tipo": ["Veneno", "Dragón"]
    },
    {
        "nombre": "Regieleki",
        "numero": 894,
        "tipo": ["Eléctrico"]
    },
    {
        "nombre": "Spectrier",
        "numero": 897,
        "tipo": ["Fantasma"]
    },
    {
        "nombre": "Urshifu",
        "numero": 892,
        "tipo": ["Lucha", "Siniestro"]
    }
]


# a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

for pokemon in pokemons:
    arbol_nombre.insert_node(pokemon['nombre'], pokemon)
    arbol_numero.insert_node(pokemon['numero'], pokemon)
    for tipo in pokemon['tipo']:
        nodo_tipo = arbol_tipo.search(tipo)
        if nodo_tipo:
            nodo_tipo.other_value.append(pokemon)
        else:
            arbol_tipo.insert_node(tipo, [pokemon])



# b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
# último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
# mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
# caracteres–;

numero = 897
resultado_num = arbol_numero.search(numero)
if resultado_num:
    print("El pokemon encontrado es el siguiente: ", resultado_num.other_value)
else: 
    print("El pokemon no ha sido encontrado.")

busqueda = 'Za'
print(f"El/los pokemon/s que contiene/n {busqueda} en su nombre son:")
arbol_nombre.proximity_search(busqueda)


# c) mostrar todos los nombres de todos los Pokémons de un determinado
# tipo agua, fuego, planta y eléctrico;

def mostrar_nombres_por_tipo(arbol, tipo):
    resultado = arbol.search(tipo)  
    if resultado and resultado.other_value:
        print(f"Pokemon/s de tipo '{tipo}':")
        for pokemon in resultado.other_value:
            print(pokemon["nombre"])
    else:
        print(f"No se encontraron Pokemon de tipo {tipo}")

tipos_a_buscar = ["Agua", "Fuego", "Planta", "Eléctrico"]

for tipo in tipos_a_buscar:
    mostrar_nombres_por_tipo(arbol_tipo, tipo)


# d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
# además un listado por nivel por nombre;
print("Listado en orden ascendente por numero de pokemon:")
arbol_numero.inorden() 

print("Listado en orden ascendente por nombre de pokemon:")
arbol_nombre.inorden()

print("Listado por nivel por nombre de pokemon:")
arbol_nombre.by_level()

# e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
def mostrar_datos_pokemon(arbol_nombre, nombres):
    for nombre in nombres:
        resultado = arbol_nombre.search(nombre)
        if resultado:
            print(f"Datos de {nombre}: {resultado.other_value}")
        else:
            print(f"No se encontro el pokemon {nombre}.")

pokemons_datos = ["Jolteon", "Lycanroc", "Tyrantrum"]

mostrar_datos_pokemon(arbol_nombre, pokemons_datos)           


# f) Determina cuantos Pokémons hay de tipo eléctrico y acero.

def contar_tipo(arbol, tipo):
    resultado = arbol.search(tipo)
    if resultado:
        return len(resultado.other_value)
    return 0

tipos_a_contar = ["Eléctrico", "Acero"]

for tipo in tipos_a_contar:
    cantidad = contar_tipo(arbol_tipo, tipo)
    print(f"Cantidad de Pokémon de tipo '{tipo}': {cantidad}")