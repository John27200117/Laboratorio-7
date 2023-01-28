import re
def replaceCadena(cadena, subcadena, subcadenaCambio):
    return re.sub(subcadena, subcadenaCambio, cadena)

pala = "Con una corona plateada y bordada llegó mi vecina la buena gallina."
subcadena = "a"
subcambio = " o"
print(replaceCadena(pala, subcadena, subcambio))
