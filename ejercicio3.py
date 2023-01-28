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
cadenaToDiccionario("Yo no compro coco porque como poco coco, como poco coco como, poco coco compro.")
