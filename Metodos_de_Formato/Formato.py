# 6.1.1. Convertir a mayúscula la primera letra
#
# Método: capitalize()
#
# Retorna: una copia de la cadena con la primera letra en mayúsculas.
#

cadena = "bienvenido a mi aplicación"
print(cadena.capitalize())
# Bienvenido a mi aplicación

# 6.1.2. Convertir una cadena a minúsculas
#
# Método: lower()
#
# Retorna: una copia de la cadena en minúsculas.
#

cadena = "Hola Mundo"
print(cadena.lower())
# hola mundo

# 6.1.3. Convertir una cadena a mayúsculas
#
# Método: upper()
#
# Retorna: una copia de la cadena en mayúsculas.
#

cadena = "Hola Mundo"
print(cadena.upper())
# HOLA MUNDO

#
# 6.1.4. Convertir mayúsculas a minúsculas y viceversa
#
# Método: swapcase()
#
# Retorna: una copia de la cadena convertidas las mayúsculas en minúsculas y viceversa.
#

cadena = "Hola Mundo"
print(cadena.swapcase())
# hOLA mUNDO

#
# 6.1.5. Convertir una cadena en Formato Título
#
# Método: title()
#
# Retorna: una copia de la cadena convertida.
#
cadena = "hola mundo"
print(cadena.title())
# Hola Mundo

#
# 6.1.6. Centrar un texto
#
# Método: center(longitud[, "caracter de relleno"])
#
# Retorna: una copia de la cadena centrada.
#
cadena = "bienvenido a mi aplicación".capitalize()
print(cadena.center(50, "="))

# ===========Bienvenido a mi aplicación============

print(cadena.center(50, " "))

#            Bienvenido a mi aplicación

#
# 6.1.7. Alinear texto a la izquierda
#
# Método: ljust(longitud[, "caracter de relleno"])
#
# Retorna: una copia de la cadena alineada a la izquierda.
#
cadena = "bienvenido a mi aplicación".capitalize()
print(cadena.ljust(50, "="))

# Bienvenido a mi aplicación=======================

#
# 6.1.8. Alinear texto a la derecha
#
# Método: rjust(longitud[, "caracter de relleno"])
#
# Retorna: una copia de la cadena alineada a la derecha.
#

cadena = "bienvenido a mi aplicación".capitalize()
print(cadena.rjust(50, "="))

# =======================Bienvenido a mi aplicación

#
print(cadena.rjust(50, " "))
#                        Bienvenido a mi aplicación

#
# 6.1.9. Rellenar un texto anteponiendo ceros
#
# Método: zfill(longitud)
#
# Retorna: una copia de la cadena rellena con ceros a la izquierda hasta alcanzar la longitud final indicada.
#

numero_factura = 1575
print(str(numero_factura).zfill(12))

# 000000001575
