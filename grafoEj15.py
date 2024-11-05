# Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas moder-
# nas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:

from Cola import Queue
from Heap import HeapMin
from pila import Stack

class Graph:
    def __init__(self, dirigido=True):
        self.elements = []
        self.dirigido = dirigido

    def show_graph(self):
        print()
        print("nodos")
        for index, nodo in enumerate(self.elements):
            print(nodo['value'])
            print(f"    aristas")
            for second_index, second_element in enumerate(nodo['aristas']):
                print(f'    destino {second_element["value"]} peso: {second_element["peso"]}')
        print()

    def search(self, value):
        for index, element in enumerate(self.elements):
            if element['value'] == value:
                return index

    def search_arista(self, vertice_value, value):
        pos_origen = self.search(vertice_value)
        if pos_origen is not None:
            for index, element in enumerate(self.elements[pos_origen]['aristas']):
                if element['value'] == value:
                    return pos_origen, index

    def insert_vertice(self, value, other_value=None):
        nodo = {
        'value': value,
        'aristas': [],
        'visitado': False,
        }
        self.elements.append(nodo)

    def insert_arista(self, origen, destino, peso):
        pos_origen = self.search(origen)
        pos_destino = self.search(destino)
        if pos_origen is not None and pos_destino is not None:
            # print(origen, destino)
            arista = {
                'value': destino,
                'peso': peso
            }
            self.elements[pos_origen]['aristas'].append(arista)
            if not self.dirigido:
                arista = {
                    'value': origen,
                    'peso': peso
                }
                self.elements[pos_destino]['aristas'].append(arista)

    
    def delete_arista(self, origen, destino):
        result = self.search_arista(origen, destino)
        if result:
            pos_vertice, pos_arista = result
            value = self.elements[pos_vertice]['aristas'].pop(pos_arista)
            if not self.dirigido:
                result = self.search_arista(destino, origen)
                if result:
                    pos_vertice, pos_arista = result
                    self.elements[pos_vertice]['aristas'].pop(pos_arista)
            return value
    
    def delete_vertice(self, value):
        pos_vertice = self.search(value)
        if pos_vertice is not None:
            delete_value = self.elements.pop(pos_vertice)
            for nodo in self.elements:
                self.delete_arista(nodo['value'], value)
            return delete_value
    
    def mark_as_not_visited(self):
        for nodo in self.elements:
            nodo['visitado'] = False

    def deep_show(self, origin):
        def __deep_show(graph, origin):
            pos_vertice = graph.search(origin)
            if pos_vertice is not None:
                if not graph.elements[pos_vertice]['visitado']:
                    graph.elements[pos_vertice]['visitado'] = True
                    print(graph.elements[pos_vertice]['value'])
                    adyacentes = graph.elements[pos_vertice]['aristas']
                    for adyacente in adyacentes:
                        __deep_show(graph, adyacente['value'])
        
        self.mark_as_not_visited()
        __deep_show(self, origin)

    def amplitude_show(self, origin):
        self.mark_as_not_visited()
        cola = Queue()
        pos_vertice = self.search(origin)
        if pos_vertice is not None:
            if not self.elements[pos_vertice]['visitado']:
                cola.arrive(self.elements[pos_vertice])
                while cola.size() > 0:
                    nodo = cola.attention()
                    nodo['visitado'] = True
                    print(nodo['value'])
                    adyacentes = nodo['aristas']
                    for adyacente in adyacentes:
                        pos_adyaecnte = self.search(adyacente['value'])
                        if not self.elements[pos_adyaecnte]['visitado']:
                            cola.arrive(self.elements[pos_adyaecnte])
    
    def exist_path(self, origen, destino):
        def __exist_path(graph, origin, destino):
            result = False
            pos_vertice = graph.search(origin)
            if pos_vertice is not None:
                if not graph.elements[pos_vertice]['visitado']:
                    graph.elements[pos_vertice]['visitado'] = True
                    if graph.elements[pos_vertice]['value'] == destino:
                        return True
                    else:
                        adyacentes = graph.elements[pos_vertice]['aristas']
                        for adyacente in adyacentes:
                            result = __exist_path(graph, adyacente['value'], destino)
                            if result:
                                break
            return result
        
        self.mark_as_not_visited()
        result = __exist_path(self, origen, destino)
        return result

    def dijkstra(self, origen):
        from math import inf
        no_visitados = HeapMin()
        camino = Stack()
        for nodo in self.elements:
            distancia = 0 if nodo['value'] == origen else inf
            no_visitados.arrive([nodo['value'], nodo, None], distancia)
        while len(no_visitados.elements) > 0:
            node = no_visitados.atention()
            costo_nodo_actual = node[0]
            camino.push(node)
            adjacentes = node[1][1]['aristas']
            # print(costo_nodo_actual, adjacentes)
            for adjacente in adjacentes:
                pos = no_visitados.search(adjacente['value'])
                if pos is not None:
                    if costo_nodo_actual + adjacente['peso'] < no_visitados.elements[pos][0]:
                        no_visitados.elements[pos][1][2] = node[1][0]
                        no_visitados.change_proirity(pos, costo_nodo_actual + adjacente['peso'])
        return camino

    def kruskal(self, origen):
        def buscar_en_bosque(bosque, buscado):
            for index, arbol in enumerate(bosque):
                # print(buscado, arbol)
                if buscado in arbol:
                    return index

        bosque = []
        aristas = HeapMin()
        for nodo in self.elements:
            bosque.append(nodo['value'])
            adjacentes = nodo['aristas']
            for adjacente in adjacentes:
                aristas.arrive([nodo['value'], adjacente['value']], adjacente['peso'])

        # print(aristas.elements)
        while len(bosque) > 1 and len(aristas.elements) > 0:
            arista = aristas.atention()
            # print(bosque)
            # print(arista[1][0], arista[1][1])
            # print(arista)
            origen = buscar_en_bosque(bosque, arista[1][0])
            destino = buscar_en_bosque(bosque, arista[1][1])
            # print(origen, destino)
            if origen is not None and destino is not None:
                if origen != destino:
                    if origen > destino:
                        vertice_ori = bosque.pop(origen)
                        vertice_des = bosque.pop(destino)
                    else:
                        vertice_des = bosque.pop(destino)
                        vertice_ori = bosque.pop(origen)

                    if '-' not in vertice_ori and '-' not in vertice_des:
                        bosque.append(f'{vertice_ori}-{vertice_des}-{arista[0]}')
                    elif '-' not in vertice_des:
                        bosque.append(vertice_ori+';'+f'{arista[1][0]}-{vertice_des}-{arista[0]}')
                    elif '-' not in vertice_ori:
                        bosque.append(vertice_des+';'+f'{vertice_ori}-{arista[1][1]}-{arista[0]}')
                    else:
                        bosque.append(vertice_ori+';'+vertice_des+';'+f'{arista[1][0]}-{arista[1][1]}-{arista[0]}')
        return bosque
    
    def insertar_maravilla(self, value, pais, tipo):
        nodo = {
            'value': value,
            'pais': pais,
            'tipo': tipo,
            'aristas': [],
            'visitado': False,
        }
        self.elements.append(nodo)


# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
# uno en las naturales) y tipo (natural o arquitectónica);


maravillas= [
    {
        "nombre": "Amazonas",
        "paises": ["Brasil", "Perú", "Colombia", "Venezuela", "Ecuador", "Bolivia", "Guyana", "Surinam", "Guayana Francesa"],
        "tipo": "natural"
    },
    {
        "nombre": "Bahia de Halong",
        "paises": ["Vietnam"],
        "tipo": "natural"
    },
    {
        "nombre": "Cataratas del Iguazu",
        "paises": ["Argentina", "Brasil"],
        "tipo": "natural"
    },
    {
        "nombre": "Isla Jeju",
        "paises": ["Corea del Sur"],
        "tipo": "natural"
    },
    {
        "nombre": "Islas Komodo",
        "paises": ["Indonesia"],
        "tipo": "natural"
    },
    {
        "nombre": "Montaña de la Mesa",
        "paises": ["Sudáfrica"],
        "tipo": "natural"
    },
    {
        "nombre": "Rio Subterraneo de Puerto Princesa",
        "paises": ["Filipinas"],
        "tipo": "natural"
    },
    {
        "nombre": "Chichen Itza",
        "paises": ["México"],
        "tipo": "arquitectonica"
    },
    {
        "nombre": "Cristo Redentor",
        "paises": ["Brasil"],
        "tipo": "arquitectonica"
    },
    {
        "nombre": "Coliseo de Roma",
        "paises": ["Italia"],
        "tipo": "arquitectonica"
    },
    {
        "nombre": "Gran Muralla China",
        "paises": ["China"],
        "tipo": "arquitectonica"
    },
    {
        "nombre": "Machu Pichu",
        "paises": ["Perú"],
        "tipo": "arquitectonica"
    },
    {
        "nombre": "Petra",
        "paises": ["Jordania"],
        "tipo": "arquitectonica"
    },
    {
        "nombre": "Taj Mahal",
        "paises": ["India"],
        "tipo": "arquitectonica"
    }
]


grafo = Graph(dirigido=False)
for maravilla in maravillas:
    grafo.insertar_maravilla(maravilla["nombre"], maravilla["paises"], maravilla["tipo"])


# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
# la distancia que las separa;

grafo.insert_arista('Amazonas', 'Bahia de Halong', 18000)
grafo.insert_arista('Bahia de Halong', 'Isla Jeju', 1900)
grafo.insert_arista('Isla Jeju', 'Rio Subterraneo de Puerto Princesa', 2300)
grafo.insert_arista('Rio Subterraneo de Puerto Princesa', 'Montaña de la Mesa', 12300)
grafo.insert_arista('Montaña de la Mesa', 'Islas Komodo', 8900)
grafo.insert_arista('Islas Komodo', 'Cataratas del Iguazu', 13500)
grafo.insert_arista('Cataratas del Iguazu', 'Amazonas', 3500)

grafo.insert_arista('Chichen Itza', 'Cristo Redentor', 5500)
grafo.insert_arista('Cristo Redentor', 'Coliseo de Roma', 7800)
grafo.insert_arista('Coliseo de Roma', 'Machu Pichu', 10500)
grafo.insert_arista('Machu Pichu', 'Gran Muralla China', 15800)
grafo.insert_arista('Gran Muralla China', 'Petra', 4000)
grafo.insert_arista('Petra', 'Taj Mahal', 3000)
grafo.insert_arista('Taj Mahal', 'Chichen Itza', 7000)

grafo.show_graph()

# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
def crear_subgrafot(grafo, tipo):
    subgrafo = Graph(dirigido=False)
    for nodo in grafo.elements:
        if nodo['tipo'] == tipo:
            subgrafo.insert_vertice(nodo['value'])

    for nodo in grafo.elements:
        if nodo['tipo'] == tipo:
            for arista in nodo["aristas"]:
                if arista["value"] in [n["value"] for n in subgrafo.elements]:
                    subgrafo.insert_arista(nodo["value"], arista["value"], arista["peso"])

    return subgrafo

subgrafo_natural = crear_subgrafot(grafo, "natural")
subgrafo_arquitectonica = crear_subgrafot(grafo, "arquitectonica")

aem_natural = subgrafo_natural.kruskal("Amazonas")
aem_arquitectonica = subgrafo_arquitectonica.kruskal("Chichen Itza")

print("Arbol de expansion minimo de tipo natural:")
for arista in aem_natural[0].split(';'):
    origen, destino, peso = arista.split('-')
    print(f"origen: {origen} -> destino: {destino} peso: {peso}")

print()


print("Arbol de expansion minimo de tipo arquitectonico:")
for arista in aem_arquitectonica[0].split(';'):
    origen, destino, peso = arista.split('-')
    print(f"origen: {origen} -> destino: {destino} peso: {peso}")



# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;

paises_naturales = []
paises_arquitectonicos = []

for maravilla in maravillas:
    if maravilla["tipo"] == "natural":
        for pais in maravilla["paises"]:
            if pais not in paises_naturales:
                paises_naturales.append(pais)
    elif maravilla["tipo"] == "arquitectonica":
        for pais in maravilla["paises"]:
            if pais not in paises_arquitectonicos:
                paises_arquitectonicos.append(pais)

paises_con_maravillas = []
for pais in paises_naturales:
    if pais in paises_arquitectonicos:
        paises_con_maravillas.append(pais)

if paises_con_maravillas:
    print("Los siguientes paises tienen maravillas arquitectonicas y naturales")
    for pais in paises_con_maravillas:
        print(pais)
else:
    print("No hay paises que dispongan de maravillas arquitectonicas y naturales")


# e. determinar si algún país tiene más de una maravilla del mismo tipo;

maravillas_por_pais = {}

for maravilla in maravillas:
    for pais in maravilla["paises"]:
        if pais not in maravillas_por_pais:
            maravillas_por_pais[pais] = {"natural": [], "arquitectonica": []}
        maravillas_por_pais[pais][maravilla["tipo"]].append(maravilla["nombre"])

paises_con_multiples_maravillas = []

for pais, tipos in maravillas_por_pais.items():
    for tipo, maravillas in tipos.items():
        if len(maravillas) > 1:
            paises_con_multiples_maravillas.append((pais, tipo, maravillas))

if paises_con_multiples_maravillas:
    print("Los siguientes países tienen más de una maravilla del mismo tipo:")
    for pais, tipo, maravillas in paises_con_multiples_maravillas:
        print(f"{pais} tiene las siguientes maravillas {tipo}: {maravillas}")
else:
    print("No hay países que tengan más de una maravilla del mismo tipo.")

