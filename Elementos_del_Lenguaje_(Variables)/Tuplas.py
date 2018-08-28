# Una tupla es una variable que permite almacenar varios datos inmutables (no pueden ser modificados una vez creados) de
#  tipos diferentes

mi_tupla = ('el precio es', 120, 'euros con iva al', 21, 'carallo')

# Se puede acceder a cada uno de los datos mediante su índice correspondiente, siendo 0 (cero), el índice del primer
# elemento

print(mi_tupla[0])  # Imprime la primera cadena de texto, ya que esta en el puesto 0

# También se puede acceder a una porción de la tupla, indicando (opcionalmente) desde el índice de inicio hasta el
# índice de fin

print(mi_tupla[0:2])
print(mi_tupla[1:4])
print(mi_tupla[2:])
print(mi_tupla[:2])

# Para acceder de forma inversa, se coloca un valor en negativo

print(mi_tupla[-2])
print(mi_tupla[1:-1])
