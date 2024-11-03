# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
# se (MCU), desarrollar un algoritmo que contemple lo siguiente:

# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
# leano que indica si es un héroe o un villano, True y False respectivamente;


from arbol_avl import BinaryTree

super_heroes = [
  {
    "nombre": "Iron Man",
    "villano": False
  },
  {
    "nombre": "Thanos",
    "villano": True
  },
  {
    "nombre": "Loctor Doom",
    "villano": True
  },
  {
    "nombre": "Green Golbing",
    "villano": True
  },
  {
      "nombre": "Capitan America",
      "villano": False
  },
  {
      "nombre": "Thor",
      "villano": False
  },
  {
      "nombre": "Roctor Strange",
      "villano": False
  }
]

tree = BinaryTree()

for personaje in super_heroes:
    is_hero = False if personaje['villano'] == True else True
    personaje['is_hero'] = is_hero
    tree.insert_node(personaje['nombre'], personaje)



# b. listar los villanos ordenados alfabéticamente;
print("Villanos ordenados alfabeticamente:")
tree.inorden_villanos()


# c. mostrar todos los superhéroes que empiezan con C;
print("Superheroes que comienzan con C:")
tree.inorden_superheros_start_with('C')


# d. determinar cuántos superhéroes hay el árbol;
print("Cantidad de superheroes en el arbol:")
print(tree.contar_super_heroes())


# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
pos = tree.search('Roctor Strange')
pos.value = 'Doctor Strange'
print("Modificar el nombre del Doctor Strange:")
tree.inorden()


# f. listar los superhéroes ordenados de manera descendente;
print("Superheroes ordenados de manera descendiente:")
tree.postorden_super_heroes()


# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.

tree_heroes = BinaryTree()
tree_villanos = BinaryTree()

for personaje in super_heroes:
    if is_hero == True:
      tree_heroes.insert_node(personaje['nombre'], personaje)

print("Arbol de heroes:")
tree_heroes.inorden()

for personaje in super_heroes:
    if is_hero == False:
      tree_villanos.insert_node(personaje['nombre'], personaje)

print("Arbol de villanos:")
tree_villanos.inorden()
