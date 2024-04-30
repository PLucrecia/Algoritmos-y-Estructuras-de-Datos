mochila = ['comida','holocrón', 'sable de luz', 'comunicador', 'kit primeros auxilios']

def usar_la_fuerza(mochila, objetos_sacados=0):

    if mochila[0] == "sable de luz":
        return True, objetos_sacados+1
    else:
        usar_la_fuerza(mochila[1:], objetos_sacados+1)

    return usar_la_fuerza(mochila[1:], objetos_sacados + 1)

sable_encontrado, objetos_sacados = usar_la_fuerza(mochila)

if sable_encontrado:
    print(f'Se encontró un sable de luz en la mochila, fue necesario sacar {objetos_sacados} objetos para encontrarlo.')
else:
    print('No se encontró un sable de luz en la mochila.')

