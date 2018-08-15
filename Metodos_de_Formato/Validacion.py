cadena = "To some, a yogi is a thought for capturing.".capitalize()

# Saber si una cadena comienza con una subcadena determinada.

print(cadena.startswith("To"))  # True
print(cadena.startswith("yogui"))  # False
print(cadena.startswith("some", 3))  # True
print('')
# Saber si una cadena finaliza con una subcadena determinada.

cadena_2 = "Arg,ransack me whale,ye salty wench!".capitalize()

print(cadena_2.endswith("wench!"))  # True
print(cadena_2.endswith("Arg"))  # False
print(cadena_2.endswith("ransack", 4, 11))  # True
print('')

# Saber si es una cadena alfanumerica

cadena_3 = "Esto es un 1"
print(cadena_3.isalnum())
cadena_3 = 'Esto no tiene numero'
print(cadena_3.isalnum())
cadena_3 = 'Estaesalfanumericaporquetiene1numero'
print(cadena_3.isalnum())
