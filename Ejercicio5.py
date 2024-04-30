#Desarrollar una función que permita convertir un número romano en un número decimal
def convertir_romano(num_romano):
    romano_entero= {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    
    if len(num_romano) == 0:
        return 0
    elif len(num_romano) == 1:
        return romano_entero[num_romano]
    
    if romano_entero[num_romano[0]] < romano_entero[num_romano[1]]:
        return romano_entero[num_romano[1]] - romano_entero[num_romano[0]] + convertir_romano(num_romano[2:])
    else:
        return romano_entero[num_romano[0]] + convertir_romano(num_romano[1:])


num_romano = "MMXXIV"

print(f"El número", num_romano, "en decimales es:", convertir_romano(num_romano))
    
    

