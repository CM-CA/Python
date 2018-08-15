import os

from pip._vendor.distlib.compat import raw_input

os.system("firefox https://librosweb.es/libro/python/capitulo_4/llamadas_recursivas.html")


# Python admite las llamadas recursivas, permitiendo a una función, llamarse a sí misma, de igual forma que lo hace
# cuando llama a otra función.


def jugar(intento=1):
    respuesta = raw_input("¿De qué color es una naranja? ")
    if respuesta != "naranja":
        if intento < 3:
            print("\nFallaste! Inténtalo de nuevo")
            intento += 1
            jugar(intento)  # Llamada recursiva
        else:
            print("\nPerdiste!")
    else:
        print("\nGanaste!")


jugar()
