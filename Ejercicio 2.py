# 2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los
# algoritmos necesarios para resolver las siguientes tareas:

from grafo import Graph
from arbol import BinaryTree


# a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la
# cantidad de episodios en los que aparecieron juntos ambos personajes que se
# relacionan;

personajes = ["Darth Vader", "Luke Skywalker", "Leia Organa", "Yoda", "Boga", "Rex", "C21"]

grafo = Graph(dirigido=False)
for personaje in personajes:
    nodo = {
        'value': personaje,
        'aristas': [],
        }
    grafo.insert_vertice(personaje)

grafo.insert_arista("Darth Vader", "Luke Skywalker", 2)
grafo.insert_arista("Darth Vader", "Leia Organa", 5)
grafo.insert_arista("Yoda", "Leia Organa", 3)
grafo.insert_arista("Rex", "C21", 1)
grafo.insert_arista("Rex", "Boga", 2)
grafo.insert_arista("Boga", "Luke Skywalker", 4)
grafo.insert_arista("Boga", "Yoda", 6)
grafo.insert_arista("C21", "Luke Skywalker", 2)

grafo.show_graph()
print()

# b) hallar el árbol de expansión minino y determinar si contiene a Yoda;
print("ARbol de expansion minimo:")
arbol_expansion = grafo.kruskal("Darth Vader")
for arista in arbol_expansion[0].split(';'):
    origen, destino, peso = arista.split('-')
    print(f"origen: {origen} -> destino: {destino} peso: {peso}")

yoda_en_arbol = any("Yoda" in arista for arista in arbol_expansion)
if yoda_en_arbol == True:
    print("Yoda esta en el arbol de expansion minimo")
else: print("Yoda no esta en el arbol de expansion minimo")
print()

# c) determinar cuál es el número máximo de episodio que comparten dos personajes,
# y quienes son
maximo_episodio = 0
personajes = ("", "")
for nodo in grafo.elements:
    for arista in nodo["aristas"]:
        if arista["peso"] > maximo_episodio:
                  maximo_episodio = arista["peso"]
                  personajes_maximos = (nodo["value"], arista["value"])

print("El numero maximo de episodio que comparten dos personajes es:", maximo_episodio)
print("Los personajes son:", personajes_maximos[0], "y", personajes_maximos[1])
print()

# d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda,
# Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8.

nuevos_personajes = ["Boba Fett", "C3PO", "Rey", "Kylo Ren", "Chewbacca",
                     " Han Solo", "R2D2", "BB8"]

for personaje in nuevos_personajes:
    nodo = {
        'value': personaje,
        'aristas': [],
        }
    grafo.insert_vertice(personaje)

grafo.insert_arista("Boba Fett","C3PO", 2)
grafo.insert_arista("C3PO","Rey", 3)
grafo.insert_arista("Rey","Kylo Ren", 4)
grafo.insert_arista("Kylo Ren","Chewbacca", 5)
grafo.insert_arista("Chewbacca","Han Solo", 6)
grafo.insert_arista("Han Solo","R2D2", 7)
grafo.insert_arista("R2D2","BB8", 8)
grafo.insert_arista("BB8","Boba Fett", 9)

print("Grafo actualizado con nuevos personajes:")
grafo.show_graph()