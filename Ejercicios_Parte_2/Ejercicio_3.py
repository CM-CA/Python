# Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que
# tengan mas de n caracteres.


def filtrar_palabras(lista, n):
    for i in lista:
        if len(i) > n:
            print (i)


filtrar_palabras(["uno", "dos", "cinco","joputacabron"],3 )
