def longSubCadena(palabra):
    subcadenas = palabra.split()
    listaCadena = []
    for i in subcadenas:
        listaCadena.append(len(i))
    for j in subcadenas:
        if len(j) == max(listaCadena):
            return str(i) + "\n" + "De valor : " + str(len(j))

print("Valor de la cadena mas larga : " + longSubCadena("Cómo quieres que te quiera,si el que quiero no me quiere,no me quiere como quiero que me quiera."))
