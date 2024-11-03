# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
# guientes tareas:

from Cola import Queue
from Heap import HeapMin
from pila import Stack
from grafo import Graph

# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

ambientes = ["cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2", "habitacion 1", "habitacion 2", "sala de estar", "terraza", "patio"]

grafo = Graph(dirigido=False)
for ambiente in ambientes:
    nodo = {
        'value': ambiente,
        'aristas': [],
        }
    grafo.insert_vertice(ambiente)


# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
# ta es la distancia entre los ambientes, se debe cargar en metros;

grafo.insert_arista("cocina", "comedor", 2)
grafo.insert_arista("cocina", "cochera", 4)
grafo.insert_arista("cocina", "quincho", 6)
grafo.insert_arista("comedor", "baño 2", 3)
grafo.insert_arista("comedor", "habitacion 1", 4)
grafo.insert_arista("quincho", "patio", 1)
grafo.insert_arista("quincho", "sala de estar", 7)
grafo.insert_arista("cochera", "baño 1", 3)
grafo.insert_arista("cochera", "habitacion 2", 5)
grafo.insert_arista("habitacion 2", "habitacion 1", 3)
grafo.insert_arista("baño 1", "terraza", 4)
grafo.insert_arista("patio", "baño 1", 5)
grafo.insert_arista("baño 2", "patio", 3)
grafo.insert_arista("baño 2", "habitacion 1", 5)
grafo.insert_arista("habitacion 2", "sala de estar", 2)
grafo.insert_arista("sala de estar", "terraza", 4)
grafo.insert_arista("terraza", "comedor", 2)
grafo.insert_arista("cocina", "habitacion 2", 5)
grafo.insert_arista("cocina", "patio", 2)
grafo.insert_arista("patio", "habitacion 1", 6)

grafo.show_graph()


# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;

arbol_expansion = grafo.kruskal('cocina')
for arista in arbol_expansion[0].split(';'):
    origen, destino, peso = arista.split('-')
    print(f"origen: {origen} -> destino: {destino} peso: {peso}")

total_metros = 0
for arista in arbol_expansion[0].split(';'):
    origen, destino, peso = arista.split('-')
    total_metros += int(peso)

print(f"Cantidad de metros de cable necesarios para conectar todos los ambientes: {total_metros}")


# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.
camino = grafo.dijkstra('habitacion 1')
destino = 'sala de estar'
peso_total = None
camino_completo = []
while camino.size() > 0:
    value = camino.pop()
    if value[1][0] == destino:
        if peso_total is None:
            peso_total = value[0]
        camino_completo.append(value[1][0])
        destino = value[1][2]
camino_completo.reverse()
print(f'El camino mas corto es: {' - '.join(camino_completo)}, con {peso_total} metros de cable de red.')

