# Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga

def mas_larga(lista):
    mas_larga = ""
    for i in lista:
        if len(i) > len(mas_larga):
            mas_larga = i
    return print(mas_larga)


mas_larga(["dados", "tres","dedos","pie","joputa"])
