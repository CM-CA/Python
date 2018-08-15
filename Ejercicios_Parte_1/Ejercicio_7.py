#  Definir una función es_palindromo() que reconoce palíndromos

def palindromo(palabra):
    palabra_inversa = palabra[::-1]
    if palabra_inversa == palabra:
        return True
    else:
        return False


print(palindromo("osa"))  # False
print(palindromo("arepera"))  # True
