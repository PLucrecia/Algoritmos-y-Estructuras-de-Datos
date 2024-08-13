# Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
# casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa-
# rias para poder realizar las siguientes actividades:

superheroes = [
    {'Nombre': 'Linterna Verde', 'Año': 1940, 'Casa': 'DC', 'biografia': 'Linterna Verde es un superhéroe con un anillo de poder'},
    {'Nombre': 'Wolverine', 'Año': 1974, 'Casa': 'Marvel', 'biografia': 'Wolverine es un mutante con garras retráctiles'},
    {'Nombre': 'Dr. Strange', 'Año': 1963, 'Casa': 'DC', 'biografia': 'Dr. Strange es un mago con poderes mágicos'},
    {'Nombre': 'Iron Man', 'Año': 1963, 'Casa': 'Marvel', 'biografia': 'Iron Man es un superhéroe con un traje de armadura'},
    {'Nombre': 'Capitana Marvel', 'Año': 1968, 'Casa': 'Marvel', 'biografia': 'Capitana Marvel es una superheroína con poderes cósmicos'},
    {'Nombre': 'Mujer Maravilla', 'Año': 1941, 'Casa': 'DC', 'biografia': 'Mujer Maravilla es una superheroína con una armadura mágica'},
    {'Nombre': 'Flash', 'Año': 1940, 'Casa': 'DC', 'biografia': 'Flash es un superhéroe con la velocidad de la luz'},
    {'Nombre': 'Star-Lord', 'Año': 1976, 'Casa': 'Marvel', 'biografia': 'Star-Lord es un superhéroe con un traje espacial'},
    {'Nombre': 'Batman', 'Año': 1939, 'Casa': 'DC', 'biografia': 'Batman es un superhéroe con un traje de murciélago'},
    {'Nombre': 'Spider-Man', 'Año': 1963, 'Casa': 'Marvel', 'biografia': 'Spider-Man es un superhéroe con poderes arácnidos'},
    {'Nombre': 'Black Widow', 'Año': 1964, 'Casa': 'Marvel', 'biografia': 'Black Widow es una superheroína con habilidades de espionaje'},
    {'Nombre': 'Martian Manhunter', 'Año': 1955, 'Casa': 'DC', 'biografia': 'Martian Manhunter es un superhéroe con poderes telepáticos'},
]

# a. Eliminar el nodo que contiene la información de Linterna Verde
superheroes = [hero for hero in superheroes if hero['Nombre'] != 'Linterna Verde']

# b. Mostrar el año de aparición de Wolverine
for hero in superheroes:
    if hero['Nombre'] == 'Wolverine':
        print(f"El año de aparición de Wolverine es {hero['Año']}")

# c. Cambiar la casa de Dr. Strange a Marvel
for hero in superheroes:
    if hero['Nombre'] == 'Dr. Strange':
        hero['Casa'] = 'Marvel'

# d. Mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”
traje_armadura_heroes = [hero['Nombre'] for hero in superheroes if 'traje' in hero['biografia'] or 'armadura' in hero['biografia']]
print("Superhéroes que mencionan la palabra 'traje' o 'armadura' en su biografia:")
print(traje_armadura_heroes)

# e. Mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963
superhereoes_1963 = [(hero['Nombre'], hero['Casa']) for hero in superheroes if hero['Año'] < 1963]
print("Superhéroes que aparecieron antes de 1963:")
print(superhereoes_1963)

# f. Mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla
for hero in superheroes:
    if hero['Nombre'] == 'Capitana Marvel':
        capitana_marvel_Casa = hero['Casa']
    if hero['Nombre'] == 'Mujer Maravilla':
        mujer_maravilla_Casa = hero['Casa']
print(f"Capitana Marvel pertenece a {capitana_marvel_Casa} y Mujer Maravilla pertenece a {mujer_maravilla_Casa}")

# g. Mostrar toda la información de Flash y Star-Lord
for hero in superheroes:
    if hero['Nombre'] == 'Flash':
        flash_info = hero
    if hero['Nombre'] == 'Star-Lord':
        star_lord_info = hero
print("Información de Flash:")
print(flash_info)
print("Información de Star-Lord:")
print(star_lord_info)

# h. Listar los superhéroes que comienzan con la letra B, M y S
b_heroes = [hero['Nombre'] for hero in superheroes if hero['Nombre'][0].lower() == 'b']
m_heroes = [hero['Nombre'] for hero in superheroes if hero['Nombre'][0].lower() == 'm']
s_heroes = [hero['Nombre'] for hero in superheroes if hero['Nombre'][0].lower() == 's']
print("Superhéroes que comienzan con la letra B:")
print(b_heroes)
print("Superhéroes que comienzan con la letra M:")
print(m_heroes)
print("Superhéroes que comienzan con la letra S:")
print(s_heroes)

# i. Determinar cuántos superhéroes hay de cada casa de comic
marvel_heroes = len([hero for hero in superheroes if hero['Casa'] == 'Marvel'])
dc_heroes = len([hero for hero in superheroes if hero['Casa'] == 'DC'])
print(f"Hay {marvel_heroes} superhéroes de Marvel y {dc_heroes} superhéroes de DC")