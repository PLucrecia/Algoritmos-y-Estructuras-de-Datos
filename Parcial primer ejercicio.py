# 1. Desarrollar una función recursiva que permita listar los elementos de vector/lista de
# manera inversa al que están cargados. Preferentemente la función solo debe tener un
# parámetro que es la lista de elementos.
lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]

def inversa(lista):
    if len(lista) == 0 :
        return []
    else:
        return [lista[-1]] + inversa(lista[:-1])

print(inversa(lista))
    