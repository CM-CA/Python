# Para definir una funcion se realiza de la siguiente forma:

def Nombre_Funcion():
    print("Hola Mundo")


# Ejecuto la funcion. Para invocar una función,
# simplemente se la llama por su nombre

Nombre_Funcion()  # Imprime el contenido de la funcion


# Cuando una función, haga un retorno de datos,
# éstos, pueden ser asignados a una variable

def Mi_Funcion():
    z = 2
    y = 3
    x = z + y
    return x


ecuacion = Mi_Funcion()

print(ecuacion)  # ecuacion=5 en este caso


# Variables de ambito local

def nombre_alumno(nombre, apellido):
    nombre_completo = nombre, apellido

    print(nombre_completo)


# Al llamar a una función, siempre se le deben pasar sus argumentos en el mismo orden en el que los espera. Pero esto
# puede evitarse, haciendo uso del paso de argumentos como keywords

# Parametros por omision: La funcion puede ser llamada con menos argumentos
# de los que se espera

def saludar(nombre, mensaje='Hola'):
    print(mensaje, nombre)


saludar('Roger')


# Keywords como parametros: también es posible llamar a una función, pasándole los argumentos esperados, como pares
# de claves=valor

def suma(a, b=50):
    print(a + b)


suma(5)


# Otro ejemplo

def saludar(nombre, mensaje='Hola'):
    print(mensaje, nombre)


saludar(mensaje="Buen día", nombre="Juancho")
