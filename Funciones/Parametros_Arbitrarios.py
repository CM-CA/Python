# Al igual que en otros lenguajes de alto nivel, es posible que una función, espere recibir un número arbitrario
# -desconocido- de argumentos. Estos argumentos, llegarán a la función en forma de tupla.
# Para definir argumentos arbitrarios en una función, se antecede al parámetro un asterisco (*):


def recorrer_parametros_arbitrarios(parametro_fijo, *arbitrarios):
    print(parametro_fijo)

    # Los parámetros arbitrarios se corren como tuplas
    for argumento in arbitrarios:
        print(argumento)


recorrer_parametros_arbitrarios('Fixed', 'arbitrario 1', 'arbitrario 2', 'arbitrario 3')


# Si una función espera recibir parámetros fijos y arbitrarios, los arbitrarios siempre deben suceder a los fijos.
#
# Es posible también, obtener parámetros arbitrarios como pares de clave=valor. En estos casos, al nombre del
# parámetro deben precederlo dos astericos (**):


def recorrer_parametros_arbitrarios(parametro_fijo, *arbitrarios, **kwords):
    print(parametro_fijo)

    for argumento in arbitrarios:
        print(argumento)

    # Los argumentos arbitrarios tipo clave, se recorren como los diccionarios
    for clave in kwords:
        print("El valor de", clave, "es", kwords[clave])


recorrer_parametros_arbitrarios("Fixed", "arbitrario 1", "arbitrario 2", "arbitrario 3", clave1="valor uno",
                                clave2="valor dos")
