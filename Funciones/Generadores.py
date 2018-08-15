# Los generadores son funciones que nos permitirán obtener sus resultados poco a poco. Es decir, cada vez que llamemos a
# la función nos darán un nuevo resultado. Por ejemplo, una función para generar todos los números pares que cada vez
# que la llamemos nos devuelva el siguiente número par.

# Esta lista tiene como primer elemento n.
# Si n es impar el siguiente elemento es igual a 3*n + 1
# si no, es igual a n // 2 (división redondeando para abajo)
# cuando se llega a 1, la lista está completa.
# La longitud de la lista no se sabe a priori, depende de n.

def wondrous(n):
    milista = []
    while n != 1:
        milista.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    else:
        milista.append(1)
        return milista


for i in wondrous(13):
    print(i)

# Si queremos sólo un conjunto dado de elementos de una de las listas generadas, vemos que perdemos recursos del equipo,
# pues se genera la lista completa:

print("Vemos todos los elementos de la lista: ")
for i in wondrous(13):
    print(i, end=" ")

print("\n\nVemos sólo los primeros cuatro elementos de la lista: ")
n = 0
for i in wondrous(13):
    n = n + 1
    if n < 5:
        print(i, end=" ")
    else:
        break

print('')


# Vemos todos los elementos de la lista:
# 13 40 20 10 5 16 8 4 2 1

# Vemos sólo los primeros cuatro elementos de la lista:
# 13 40 20 10

# Podemos adaptar esta función a un generador:
#
# Desde el punto de vista de la sintaxis, una función generadora se distingue de las funciones vistas por el hecho de
# que el control al llamador es devuelto con la expresión yield en vez de con una instrucción return. Esta función
# devuelve un iterador del tipo generator. La llamada a la función no provoca la ejecución del código, sino que crea
# un generador y lo devuelve

# >>> g = foo('inicio')
# >>> type(g)
# <class 'generator'>

# Para moverse con la lista

# >>> g.__next__()

# Ejemplo:


def wondrous(n):
    while n != 1:
        yield n
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    else:
        yield 1


# Cuando se llama a la función, devuelve un generador, mediante el cual
# podemos producir los elementos de la secuencia uno a uno:


g = wondrous(13)

# Generamos e imprimimos los cuatro primeros números de la lista
for i in range(15):
    num = g.__next__()
    print(num)
    # Si llegamos a "1" la lista NO sigue. Evitamos errores así:
    if num == 1:
        break
