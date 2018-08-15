# Clases: las clases son los modelos sobre los cuales se construiran los objetos

class Objeto:
    pass


class Antena:
    pass


class Pelo:
    pass


class Ojo:
    pass


# Propiedades: Las propiedades son las caracteristicas del objeto

class Antena():
    color = ""
    longitud = ""


class Ojo():
    forma = ""
    color = ""
    tamanho = ""


class Pelo():
    color = ""
    textura = ""


class Objeto():
    color = ""
    tamanho = ""
    aspecto = ""


antenas = Antena()
ojos = Ojo()
pelos = Pelo()


# Las propiedades se definen de la misma forma que las variables

# Los metodos son funciones que representan accones propias que puede
# realizar el objeto.

class Objeto():
    color = "verde"
    tamanho = "grande"
    aspecto = "feo"
    antenas = Antena()
    ojos = Ojo()
    pelos = Pelo()


def flotar(self):
    # El primer parametro de un metro SIEMPRE debe ser (self).
    pass


# Objeto: materializacion de una clase. La clase es el razonamiento del objeto. al instanciar una clase (asignar como
# valor a una variable) se crea un objeto.

class Objeto:
    color = "verde"
    tamanho = "grande"
    aspecto = "feo"
    antenas = Antena()
    ojos = Ojo()
    pelos = Pelo()


def flotar(self):
    print(12)


et = Objeto()
print(et.color)
print(et.tamanho)
print(et.aspecto)
et.color = "rosa"
print(et.color)
