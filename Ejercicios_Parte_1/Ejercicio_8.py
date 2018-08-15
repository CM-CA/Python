# Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o
# devuelva False de lo contrario. Escribir la función usando el bucle for anidado

def superposicion(lista_1, lista_2):
    for i in range(len(lista_1)):
        for j in range(len(lista_2)):
            if lista_1[i] == lista_2[j]:
                return True
            else:
                return False


print(superposicion([4, 3, 2], [4, 5, 6]))
