# Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una
# lista.

def sumalista(listanumeros):
    laSuma = 0
    for i in listanumeros:
        laSuma = laSuma + i
    return laSuma


def multiplicalista(listanumeros):
    multiplica = 1
    for i in listanumeros:
        multiplica = multiplica * i
    return multiplica


print(sumalista([1, 2, 3, 4]))
print(multiplicalista([1, 2, 3, 4]))
