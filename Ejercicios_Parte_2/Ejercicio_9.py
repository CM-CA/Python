# Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e"
# tiene y así hasta completar todas las vocales

def contar_vocales(cadena):
    cadena = cadena.lower ()
    vocales = "aeiou"

    for x in vocales:
        contador = 0
        for i in cadena:
            if i == x:
                contador += 1
        print ( "Hay %d %s" % (contador, x) )


contar_vocales ( "Hola,hoy vamos a contar las vocales,si? uo!" )
