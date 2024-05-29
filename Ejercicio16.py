# Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
# strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que
# permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en am-
# bos episodios.

from pila import Stack


def intersecciones (pilaV, pilaVII):
    pila_aux = Stack()
    pila_intersecciones = Stack()

    while pilaV.size() > 0:
        personajeV = pilaV.pop()
        while pilaVII.size() > 0:
            personajeVII = pilaVII.pop()
            pila_aux.push(personajeVII)
            if ( personajeV == personajeVII):
                pila_intersecciones.push(personajeV)
        while pila_aux.size() > 0:
            personaje = pila_aux.pop()
            pilaVII.push(personaje)
    return pila_intersecciones

def barrido(self):
    pila_aux = Stack()
    while self.size() > 0:
        dato = self.pop()
        print(dato)
        pila_aux.push(dato)
    while pila_aux.size() > 0:
        dato = pila_aux.pop()
        self.push(dato)

pilaV = Stack()
pilaV.push('Luke Skywalker')
pilaV.push('Han Solo')
pilaV.push('Darth Vader')
pilaV.push('Princesa Leia')
pilaV.push('C-3PO')
pilaV.push('Yoda')
pilaV.push('Boba Fett')
pilaV.push('Ben Kenobi')


pilaVII = Stack()
pilaVII.push('Ben Solo')
pilaVII.push('Rey')
pilaVII.push('Finn')
pilaVII.push('Han Solo')
pilaVII.push('Chewbacca')
pilaVII.push('Princesa Leia')
pilaVII.push('C-3PO')
pilaVII.push('Luke Skywalker')

print(pilaV)
print(pilaVII)

pila_resultados = intersecciones(pilaV, pilaVII)

if pila_resultados.size() < 0:
    print("No hay intersecciones.")
else:
    print("Los personajes que se repitieron son: ") 
    barrido(pila_resultados)

