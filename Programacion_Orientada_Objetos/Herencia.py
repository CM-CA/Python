# Herencia: una clase hereda de otra. Cuando una clase no hereda de ninguna otra, debe hacerse heredar
# de la clase Object (clase principal de python, que define un objeto)


class Antena(object):
    color = ""
    longitud = ""


class Pelo(object):
    color = ""
    textura = ""


class Ojo(object):
    forma = ""
    color = ""
    tamanio = ""


class Objeto(object):
    color = ""
    tamanio = ""
    aspecto = ""
    antenas = Antena()
    ojos = Ojo()
    pelos = Pelo()

    def flotar(self):
        pass


class Dedo(object):
    longitud = ""
    forma = ""
    color = ""


class Pie(object):
    forma = ""
    color = ""
    dedos = Dedo()


# NuevoObjeto sí hereda de otra clase: Objeto
class NuevoObjeto(Objeto):
    pie = Pie()

    def saltar(self):
        pass


# Acceso a metodos: nombre del objeto.propiedad o metodo

pie = Pie()
print(pie.dedos)
pie.dedos = "5"
variable = pie.metodo()
print(variable)
print(pie.otro_metodo())
