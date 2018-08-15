# 6.2.1. Contar cantidad de apariciones de una subcadena
#
# Método: count("subcadena" [, posicion_inicio, posicion_fin])
#
# Retorna: un entero representando la cantidad de apariciones de subcadena dentro de cadena.
#

cadena = "bienvenido a mi aplicación".capitalize()
print(cadena.count("a"))
# 3

#
# 6.2.2. Buscar una subcadena dentro de una cadena
#
# Método: find("subcadena" [, posicion_inicio, posicion_fin])
#
# Retorna: un entero representando la posición donde inicia la subcadena dentro de cadena. Si no la encuentra, retorna -1.
#

cadena = "bienvenido a mi aplicación".capitalize()
print(cadena.find("mi"))
# 13
print(cadena.find("mi", 0, 10))
# -1
