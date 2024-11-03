# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:


from Cola import Queue


class BinaryTree:
    class __Node:
        def __init__(self, value, left=None, right=None, other_value=None, capturada=None):
            self.value = value
            self.left = left
            self.right = right
            self.other_value = other_value
            self.capturada = capturada 
            self.height = 0

    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = max(left_height, right_height) + 1

    def simple_rotation(self, root, control):
        if control:
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def balancing(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    def insert_node(self, value, other_value=None):
        def __insert(root, value, other_value=None):
            if root is None:
                return BinaryTree.__Node(value, other_value=other_value)
            elif value < root.value:
                root.left = __insert(root.left, value, other_value)
            else:
                root.right = __insert(root.right, value, other_value)
            root = self.balancing(root)
            self.update_height(root)
            return root

        self.root = __insert(self.root, value, other_value)

    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    return root
                elif key < root.value:
                    return __search(root.left, key)
                else:
                    return __search(root.right, key)
        return __search(self.root, key) if self.root is not None else None

    def preorden(self):
        def __preorden(root):
            if root is not None:
                print(root.value)
                __preorden(root.left)
                __preorden(root.right)
        if self.root is not None:
            __preorden(self.root)

    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(f"{root.value} - {root.other_value.get('derrotado')}")
                __inorden(root.right)
        if self.root is not None:
            __inorden(self.root)

    def inorden_descripcion(self):
        def __inorden_descripcion(root):
            if root is not None:
                __inorden_descripcion(root.left)
                derrotado = root.other_value.get("derrotado por", "Desconocido")
                descripcion = root.other_value.get("descripcion", "No hay descripción disponible.")
                print(f"Nombre: {root.value}, Derrotado por: {derrotado}, Descripción: {descripcion}")
                __inorden_descripcion(root.right)
        if self.root is not None:
            __inorden_descripcion(self.root)

    def postorden(self):
        def __postorden(root):
            if root is not None:
                __postorden(root.left)
                __postorden(root.right)
                print(root.value)
        if self.root is not None:
            __postorden(self.root)

    def lista_derrotado(self, hero_nombre):
        def __lista_derrotado(root):
            if root is not None:
                __lista_derrotado(root.left)
                if root.other_value.get('derrotado') == hero_nombre:
                    print(root.value)
                __lista_derrotado(root.right)
        if self.root is not None:
            __lista_derrotado(self.root)

    def delete_node(self, value):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            if root is not None:
                if root.value > value:
                    root.left, _ = __delete(root.left, value)
                elif root.value < value:
                    root.right, _ = __delete(root.right, value)
                else:
                    if root.left is None:
                        return root.right, root
                    elif root.right is None:
                        return root.left, root
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        root.other_value = replace_node.other_value
                root = self.balancing(root)
                self.update_height(root)
            return root, None

        if self.root is not None:
            self.root, _ = __delete(self.root, value)

    def agregar_descripcion(self, nombre, description):
        node = self.search(nombre)
        if node:
            node.other_value["descripcion"] = description
        else:
            print(f"La criatura '{nombre}' no fue encontrada en el árbol.")

    def mostrar_informacion_criatura(self, nombre):
        node = self.search(nombre)
        if node:
            derrotado = node.other_value.get("derrotado por", "Desconocido")
            descripcion = node.other_value.get("descripcion", "No hay descripción disponible.")
            print(f"Nombre: {node.value}")
            print(f"Derrotado por: {derrotado}")
            print(f"Descripción: {descripcion}")
        else:
            print(f"La criatura '{nombre}' no fue encontrada en el árbol.")


    def contar_derrotas_por_heroe(self):
            heroe_counter = {}

            def __contar(root):
                if root is not None:
                    __contar(root.left)
                    derrotado = root.other_value.get("derrotado")
                    if derrotado:
                        if derrotado in heroe_counter:
                            heroe_counter[derrotado] += 1
                        else:
                            heroe_counter[derrotado] = 1
                    __contar(root.right)

            __contar(self.root)

            sorted_heroes = sorted(heroe_counter.items(), key=lambda x: x[1], reverse=True)

            top_3_heroes = sorted_heroes[:3]

            for hero, count in top_3_heroes:
                print(f"{hero}: {count} criaturas derrotadas")

    def capturar_criatura(self, nombre, heroe):
        node = self.search(nombre)
        if node:
            node.capturada = heroe
        else:
            print(f"La criatura '{nombre}' no fue encontrada en el árbol.")

    def listar_capturadas(self):
        def __listar_capturadas(root):
            if root is not None:
                __listar_capturadas(root.left)
                if root.capturada is not None:
                    print(f"{root.value} - Capturada por: {root.capturada}")
                __listar_capturadas(root.right)

        if self.root is not None:
            __listar_capturadas(self.root)

    def buscar_por_coincidencia(self, coincidencia):
        def __buscar(root, coincidencia):
            if root is not None:
                if coincidencia.lower() in root.value.lower():
                    print(root.value)
                __buscar(root.left, coincidencia)
                __buscar(root.right, coincidencia)
        __buscar(self.root, coincidencia)


    def modificar_derrotado(self, nombre, nuevo_dato):
        def __modificar(root):
            if root is not None:
                if root.value.lower() == nombre.lower(): 
                    root.other_value['derrotado'] = nuevo_dato
                __modificar(root.left)
                __modificar(root.right)

        __modificar(self.root)

    def modificar_nombre(self, nombre, nuevo_dato):
        def __modificar(root):
            if root is not None:
                if root.value.lower() == nombre.lower(): 
                    root.value = nuevo_dato
                __modificar(root.left)
                __modificar(root.right)

        __modificar(self.root)

    def by_level(self):
        pendientes = Queue()
        if self.root is not None:
            pendientes.arrive(self.root)

        while pendientes.size() > 0:
            node = pendientes.attention()
            print(f"nivel {node.height}", node.value)
            if node.left is not None:
                pendientes.arrive(node.left)
            if node.right is not None:
                pendientes.arrive(node.right)

criaturas = [
    {"nombre": "ceto", "derrotado": None},
    {"nombre": "tifon", "derrotado": "zeus"},
    {"nombre": "equidna", "derrotado": "argos panoptes"},
    {"nombre": "dino", "derrotado": None},
    {"nombre": "pefredo", "derrotado": None},
    {"nombre": "enio", "derrotado": None},
    {"nombre": "escila", "derrotado": None},
    {"nombre": "caribdis", "derrotado": None},
    {"nombre": "euríale", "derrotado": None},
    {"nombre": "esteno", "derrotado": None},
    {"nombre": "medusa", "derrotado": "perseo"},
    {"nombre": "ladón", "derrotado": "heracles"},
    {"nombre": "aguila de cácucaso", "derrotado": None},
    {"nombre": "quimera", "derrotado": "belerofonte"},
    {"nombre": "hidra de lerna", "derrotado": "heracles"},
    {"nombre": "león de nemea", "derrotado": "heracles"},
    {"nombre": "esfinge", "derrotado": "edipo"},
    {"nombre": "dragón de la cólquida", "derrotado": None},
    {"nombre": "cerbero", "derrotado": None},
    {"nombre": "cerda de cromión", "derrotado": "teseo"},
    {"nombre": "ortro", "derrotado": "heracles"},
    {"nombre": "toro de creta", "derrotado": "teseo"},
    {"nombre": "jabalí de calidón", "derrotado": "atlanta"},
    {"nombre": "carcinos", "derrotado": None},
    {"nombre": "gerion", "derrotado": "heracles"},
    {"nombre": "cloto", "derrotado": None},
    {"nombre": "láquesis", "derrotado": None},
    {"nombre": "átropos", "derrotado": None},
    {"nombre": "minotauro de creta", "derrotado": "teseo"},
    {"nombre": "harpías", "derrotado": None},
    {"nombre": "argos panoptes", "derrotado": "hermes"},
    {"nombre": "aves del estínfalo", "derrotado": None},
    {"nombre": "talos", "derrotado": "medea"},
    {"nombre": "sirenas", "derrotado": None},
    {"nombre": "pitón", "derrotado": "apolo"},
    {"nombre": "cierva de cerinea", "derrotado": None},
    {"nombre": "basilisco", "derrotado": None},
    {"nombre": "jabalí de erimanto", "derrotado": None}
]


arbol = BinaryTree()

for criatura in criaturas:
    arbol.insert_node(criatura["nombre"], {"derrotado": criatura["derrotado"]})


# a. listado inorden de las criaturas y quienes la derrotaron;
print("Listado inorden de las criaturas y quienes la derrotaron:")
arbol.inorden()
print()


# b. se debe permitir cargar una breve descripción sobre cada criatura;
print("Listado inorden de las criaturas con una breve descripcion de cada una:")
arbol.agregar_descripcion("medusa", "animal marino invertebrado")
arbol.agregar_descripcion("talos", "autómata gigante hecho de bronce")
arbol.inorden_descripcion()
print()


# c. mostrar toda la información de la criatura Talos;
print("Informacion sobre la criatura Talos:")
arbol.mostrar_informacion_criatura("talos")
print()


# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
print("Los 3 heroes que derrotaron mayor cantidad de criaturas son:")
arbol.contar_derrotas_por_heroe()
print()


# e. listar las criaturas derrotadas por Heracles;
print("lista de criaturas derrotadaas por heracles:")
arbol.lista_derrotado("heracles")
print()


# f. listar las criaturas que no han sido derrotadas;
print("lista de criaturas que no han sido derrotadas:")
arbol.lista_derrotado(None)
print()


# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo.
# y
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
arbol.capturar_criatura("cerbero","heracles")
arbol.capturar_criatura("toro de creta","heracles")
arbol.capturar_criatura("cierva de cerinea","heracles")
arbol.capturar_criatura("jabalí de erimanto","heracles")
print("Criaturas que heracles atrapó:")
arbol.listar_capturadas()
print()


# i. se debe permitir búsquedas por coincidencia;
print("Búsqueda por coincidencia, criaturas que contengan 'cer'':")
arbol.buscar_por_coincidencia("cer")
print()


# j. eliminar al Basilisco y a las Sirenas;
arbol.delete_node("basilisco")
arbol.delete_node("sirenas")
print("Arbol sin el basilisco y las sirenas:")
arbol.inorden()
print()


# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
arbol.modificar_derrotado("aves del estínfalo", "heracles")
print("arbol con las aves de estinfalo modificadas:")
arbol.inorden()
print()

# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
print("Arbol con el nombre de la criatura Ladón modificado por Dragón Ladón")
arbol.modificar_nombre("ladón", "dragón ladón")
arbol.inorden()
print()


# m. realizar un listado por nivel del árbol;
print("Listado por nivel del arbol:")
arbol.by_level()
print()


# n. muestre las criaturas capturadas por Heracles.
print("Criaturas capturadas por heracles:")
arbol.lista_derrotado("heracles")