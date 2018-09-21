# Escriba una función es_bisiesto() que determine si un año determinado es un año bisiesto.Un año bisiesto es divisible
# por 4, pero no por 100. También es divisible por 400

def es_bisiesto():
    print(" Comprar si un año es bisisiesto ")
    a=input("Escribe un año: ")
    if int (a)%4==0 and(not((int(a)%100==0))):
        print("el año ",a," es bisiesto.")
    elif int(a)%400==0:
        print("el año ",a," es bisiesto.")
    else:
        print("el año ",a," no es bisiesto.")



es_bisiesto()