def cadenaToDiccionario(texto):
    retirar = ".;:.\n\"'"
    for i in retirar:
        texto = texto.replace(i,"")
    texto.lower()
    listPalabras = texto.split(" ")
    diccionario = {}
    for i in listPalabras:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
    for j in diccionario:
        cantidad = diccionario[j]
        print(f"Palabra {j} se repite {cantidad}")
cadenaToDiccionario("Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres.")
