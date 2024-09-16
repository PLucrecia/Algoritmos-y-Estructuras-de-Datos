# 3. El general Hux es la persona encargada de administrar todas las operaciones de la base Starki-
# ller, para lo cual nos solicita desarrollar un algoritmo que permita controlar las actividades que
# se realizan, contemplando lo siguiente:

# a. debe contemplar distintas prioridades para el control de operaciones de acuerdo al siguien-
# te criterio: pedidos de líder supremo Snoke y de Kylo Ren nivel tres, de capitán Phasma
# nivel dos y el resto de las operaciones nivel a cargo de los generales de la base de nivel uno;
# b. de cada actividad se conoce quien es el encargado, una descripción, la hora y opcional-
# mente la cantidad de Stormtroopers requeridos;
# c. utilizar una cola de prioridad para administrar las distintas operaciones, debe cargar al
# menos ocho: dos de nivel tres, cuatro de nivel dos y cuatro de nivel uno;
# d. opcionalmente se podrán agregar operaciones luego de atender una;
# e. realizar la atención de las operaciones de la cola;
# f. luego de atender la quinta operación, agregar una operación solicitada por capitán Phasma
# para revisión de intrusos en el hangar B7 que requiere 25 Stormstroopers;
# g. luego de atender la sexta operación, agregar una operación solicitada por el líder supremo
# Snoke para destruir el planeta Takodana.

from Heap import HeapMax

class Operacion:
    def __init__(self, encargado, descripcion, hora, prioridad, stormtroopers = 0):
        self.encargado = encargado
        self.descripcion = descripcion
        self.hora = hora
        self.prioridad = prioridad
        self.stormtroopers = stormtroopers

    def __str__(self):
        return f'{self.descripcion} (Prioridad {self.prioridad}) - {self.encargado}'

cola_operaciones = HeapMax()

operaciones_iniciales = [
    Operacion("Líder Supremo Snoke", "Reunion con Kylo Ren", "08:00", 3),
    Operacion("Kylo Ren", "Entrenamiento de Stormtroopers", "09:00", 3),
    Operacion("Capitan Phasma", "Revision de armamento", "10:00", 2),
    Operacion("Capitan Phasma", "Entrenamiento de tropas", "11:00", 2),
    Operacion("General Hux", "Revision de defensas", "12:00", 1),
    Operacion("General Hux", "Reunion con oficiales", "13:00", 1),
    Operacion("General Hux", "Inspeccion de hangares", "14:00", 1),
    Operacion("General Hux", "Revisión de suministros", "15:00", 1)
]

for operacion in operaciones_iniciales:
    cola_operaciones.arrive(operacion, operacion.prioridad)

atencion = 0
while cola_operaciones.elements:
    i, operacion = cola_operaciones.atention()
    print(f'Atendiendo operación: {operacion.descripcion} (Prioridad {operacion.prioridad}) - {operacion.encargado}')

    atencion += 1
    if atencion == 5:
        cola_operaciones.arrive(Operacion("Capitan Phasma", "Revision de intrusos en hangar B7", "16:00", 2, 25), 2)
    elif atencion == 6:
        cola_operaciones.arrive(Operacion("Lider Supremo Snoke", "Destruir planeta Takodana", "17:00", 3), 3)