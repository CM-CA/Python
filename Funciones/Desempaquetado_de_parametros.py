# la función espere una lista fija de parámetros, pero que éstos, en vez de estar disponibles de forma separada,
# se encuentren contenidos en una lista o tupla. En este caso, el signo asterisco (*) deberá preceder al nombre de la
# lista o tupla que es pasada como parámetro durante la llamada a la función.


def calcular(importe, descuento):
    return importe - (importe * descuento / 100)


datos = [1500, 10]
print(calcular(*datos))


# El mismo caso puede darse cuando los valores a ser pasados como parámetros a una función, se encuentren disponibles en
# un diccionario. Aquí, deberán pasarse a la función, precedidos de dos asteriscos (**):
#

def calcular(importe, descuento):
    return importe - (importe * descuento / 100)


datos = {"descuento": 10, "importe": 1500}
print(calcular(**datos))
