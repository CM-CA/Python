# es posible, llamar a una función dentro de otra,
# de forma fija y de la misma manera que se la llamaría,
# desde fuera de dicha función.

# Ejemplo 1:

print('Ejemplo 1')


def mensaje_sol(solucion):
    return 'El resultado es: ' + solucion


def sumar(num1, num2):
    sol = int(num1) + int(num2)
    print(mensaje_sol(str(sol)))


sumar(3, 5)
print('')
print('Ejemplo 2')


# Ejemplo 2:


def funcion():
    return 'Hola Mundo'


def saludar(nombre, mensaje='Hola'):
    print(mensaje, nombre)
    print(funcion())


saludar("Manuel")

print('')

# Lambdas: nos permite crear funciones rapidas. Estas funciones no pueden
# distinguirse por el nombre, por eso de les denomina "Funciones anonimas"

print('Ejemplo Lambdas: ')
f = lambda x, y: y + x
suma = f(1, 2)
print(suma)
print('')


# Para conseguir llamar a una función de manera dinámica, Python dispone de dos funciones nativas: locals() y globals().
#
# Ambas funciones, retornan un diccionario. En el caso de locals(), éste diccionario se compone -justamente- de todos
# los elementos de ámbito local, mientras que el de globals(), retorna lo propio pero a nivel global.


def funcion():
    return "Hola Mundo"


def llamada_de_retorno(func=""):
    """Llamada de retorno a nivel global"""
    return globals()[func]()


print(llamada_de_retorno("funcion"))

# Llamada de retorno a nivel local
nombre_de_la_funcion = "funcion"
print(locals()[nombre_de_la_funcion]())
print('')

# Si se tienen que pasar argumentos en una llamada retorno, se lo puede hacer normalmente:

print('Argumentos de retorno: ')


def funcion(nombre):
    return "Hola " + nombre


def llamada_de_retorno(func=""):
    """Llamada de retorno a nivel global"""
    return globals()[func]("Laura")


print(llamada_de_retorno("funcion"))

# Llamada de retorno a nivel local
nombre_de_la_funcion = "funcion"
print(locals()[nombre_de_la_funcion]("Facundo"))

# Durante una llamada de retorno, el nombre de la función, puede no ser el indicado. Entonces, siempre que se deba
# realizar una llamada de retorno, es necesario comprobar que ésta exista y pueda ser llamada

print('')

print('Comprobar nombre de la funcion: ')
if nombre_de_la_funcion in locals():
    if callable(locals()[nombre_de_la_funcion]):
        print(locals()[nombre_de_la_funcion]("Emilse"))

print('')

# El operador in, nos permitirá conocer si un elemento se encuentra dentro de una colección, mientras que la función
# callable() nos dejará saber si esa función puede ser llamada.

print('Comprobar y llamar una funcion: ')


def funcion(nombre):
    return "Hola " + nombre


def llamada_de_retorno(func=""):
    if func in globals():
        if callable(globals()[func]):
            return globals()[func]("Laura")
    else:
        return "Función no encontrada"


print(llamada_de_retorno("funcion"))

nombre_de_la_funcion = "funcion"

if nombre_de_la_funcion in locals():
    if callable(locals()[nombre_de_la_funcion]):
        print(locals()[nombre_de_la_funcion]("Facundo"))
else:
    print("Función no encontrada")
