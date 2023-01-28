def dividirCadena(cadena,caracter):
    subCadena = cadena.split(caracter)
    return subCadena

cadena = "A lo hecho, pecho"
caracter = "h"
print(dividirCadena(cadena,caracter))
