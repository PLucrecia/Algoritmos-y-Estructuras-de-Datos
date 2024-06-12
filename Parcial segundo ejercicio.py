class Stack:

    def __init__(self):
        self.__elements = []

    def push(self, element):
        self.__elements.append(element)

    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            return None

    def on_top(self):
        if len(self.__elements) > 0:
            return self.__elements[-1]
        else:
            return None

    def size(self):
        return len(self.__elements)
    
    def __str__(self):
        return str(self.__elements)
    
def barrido(self):
    pila_aux = Stack()
    while self.size() > 0:
        dato = self.pop()
        print(dato)
        pila_aux.push(dato)
    while pila_aux.size() > 0:
        dato = pila_aux.pop()
        self.push(dato)

# 2. Dada una pila con los datos de dinosaurios resolver lo siguiente actividades:

dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso": 7000 ,
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": 6000 ,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": 15 ,
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": 56000 ,
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": 5000 ,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": 10000 ,
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": 2000 ,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": 23000 ,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": 15000 ,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": 6000 ,
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": 2500 ,
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": 1500 ,
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": 2700 ,
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": 5000 ,
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": 25 ,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": 200 ,
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": 450 ,
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": 15000 ,
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },

  ]

# a) Contar cuantas especies hay;
def contar_especies(dinosaurios):
    especies = Stack()
    for dinosaurio in dinosaurios:
        especie = dinosaurio['especie']
        auxiliar = Stack()
        while especies.size() > 0:
            elemento = especies.pop()
            auxiliar.push(elemento)
            if elemento == especie:
                while auxiliar.size() > 0:
                    especies.push(auxiliar.pop())
                break
        else:
            especies.push(especie)
            while auxiliar.size() > 0:
                especies.push(auxiliar.pop())
    return especies.size()

print('Cantidad de especies:', contar_especies(dinosaurios))


# b) Determinar cuantos descubridores distintos hay;
def contar_descubridores(dinosaurios):
    descubridores = Stack()
    for dinosaurio in dinosaurios:
        descubridor = dinosaurio['descubridor']
        auxiliar = Stack()
        while descubridores.size() > 0:
            elemento = descubridores.pop()
            auxiliar.push(elemento)
            if elemento == descubridor:
                while auxiliar.size() > 0:
                    descubridores.push(auxiliar.pop())
                break
        else:
            descubridores.push(descubridor)
            while auxiliar.size() > 0:
                descubridores.push(auxiliar.pop())
    return descubridores.size()

print(' ')
print('Cantidad de descubridores:', contar_descubridores(dinosaurios))

# c) Mostrar todos los dinosaurios que empiecen con T;
def empiezan_conT(dinosaurios):
    dinosauriosT = Stack()
    for dinosaurio in dinosaurios:
        dino = dinosaurio['nombre']
        if dino[:1] == 'T':
            dinosauriosT.push(dino)
    return barrido(dinosauriosT)

print(' ')
print('Dinosaurios que empiezan con T:')
empiezan_conT(dinosaurios)

# d) Mostrar todos los dinosaurio que pesen menos de 275 Kg
def menos_275(dinosaurios):
    dinosaurios_275 = Stack()
    for dinosaurio in dinosaurios:
        dino = dinosaurio['peso']
        if dino < 275 :
            dinosaurios_275.push(dinosaurio['nombre'])
    return barrido(dinosaurios_275)

print(' ')
print('Dinosaurios que pesan menos de 275 kg:')
menos_275(dinosaurios)

# e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S;
dinosAQS = Stack()
for dinosaurio in dinosaurios:
    dino = dinosaurio['nombre']
    if dino.startswith('A') or dino.startswith('Q') or dino.startswith('S'):
        dinosAQS.push(dinosaurio)


print(' ')
print('Pila de dinosaurios que empiezan con A, Q o S:')
barrido(dinosAQS)

