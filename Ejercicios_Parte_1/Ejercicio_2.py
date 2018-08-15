# Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos

numero_1 = int
numero_2 = int
numero_3 = int


def max_de_tres(numero_1, numero_2, numero_3):
    if numero_1 > numero_2 and numero_1 > numero_3:
        print(numero_1)
    elif numero_1 < numero_2 and numero_2 > numero_3:
        print(numero_2)
    else:
        print(numero_3)


max_de_tres(4, 3, 5)
