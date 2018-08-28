# Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
from pip._vendor.distlib.compat import raw_input


def main():
    x=input("Cuantos nombres quieres ingresar? ")
    lista=[]

    for i in range(int(x)):
        a=input("Ingresa nombre: ")
        lista.append(a)
    print("")
    comienzo= input("Con que letra empieza?: ")
    cont=0

    for i in lista:
        if i[0]==comienzo.lower() or i[0]==comienzo.upper():
            cont+=1
    return print(cont)


main()