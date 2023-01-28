from collections import Counter
def contador(palabra):
    contador = Counter(palabra)
    rep = [t[1] for t in list(contador.items()) if t[1] > 1]
    return len(rep)

def long(cadena):
    lista = cadena.split()
    print(lista)
    for i in lista:
        if contador(i) == 0:
            rpt = "La cadena más larga es: " + str(i) + "\n" + "Con un valor de: " + str(len(i))
            return rpt

print(long("Ligar es ser agil"))

