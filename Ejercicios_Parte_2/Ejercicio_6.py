# Escribir un pequeño programa donde:
# - Se ingresa el año en curso.
# - Se ingresa el nombre y el año de nacimiento de tres personas.
# - Se calcula cuántos años cumplirán durante el año en curso.
# - Se imprime en pantalla.



def main():
    a_curso= input("Ingresa año actual: ")
    for i in range(3):
        nombre=input ("Ingresa nombre: ")
        edad= input("Año de nacimiento: ")
        print ( nombre, (int(a_curso) -int( edad)), "años en el", a_curso )


main()