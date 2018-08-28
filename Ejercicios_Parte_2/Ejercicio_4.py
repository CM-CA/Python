# Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir
# cuantas letras mayúsculas tiene.

def mayusculas(cadena):
    cont=0
    for i in cadena:
        if i !=i.lower():
            cont+=1
    print("La cadena tiene",cont,"mayusculas")


mayusculas("La Oreja de TU Padre")