# Operadores relacionales
# == 	Igual que 	5 == 7 	False
# != 	Distinto que 	rojo != verde 	True
# < 	Menor que 	8 < 12 	True
# > 	Mayor que 	12 > 7 	True
# <= 	Menor o igual que 	12 <= 12 	True
# >= 	Mayor o igual que 	4 >= 5 	False

# Operadores Logicos
# Operador 	Ejemplo 	          Explicación 	    Resultado
# and 	    5 == 7 and 7 < 12 	  False and False   False
# and 	    9 < 12 and 12 > 7 	  True and True 	True
# and 	    9 < 12 and 12 > 15 	  True and False 	False
# or 	    12 == 12 or 15 < 7 	  True or False 	True
# or 	    7 > 5 or 9 < 12 	  True or True 	    True
# xor 	    4 == 4 xor 9 > 3 	  True o True 	    False
# xor 	    4 == 4 xor 9 < 3 	  True o False 	    True

# Las estructuras de control de flujo condicionales,
# se definen mediante el uso de tres palabras claves
# reservadas, del lenguaje:
# if (si), elif (sino, si) y else (sino).

# Ejemplo 1: Semaforo en rojo

Color = ['Rojo', 'Verde']
Semaforo = Color[0]  # Cambiando la variable por 0 o 1, nos permite cambiar la luz del semaforo
Alto = "Stop"
Adelante = "Go"
if Semaforo == Color[0]:
    print(Alto)
else:
    print(Adelante)

# Ejemplo 2: Pago con tarjeta de credito

Gasto_compra = 299.35

if Gasto_compra <= 299.25:
    print("Pago en Efectivo")
elif Gasto_compra > 200.00 and Gasto_compra < 300.00:
    print("Pago con tarjeta de debito")
else:
    print("Pago con tarjeta de credito")
