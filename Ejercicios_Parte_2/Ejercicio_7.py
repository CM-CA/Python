# Definir una tupla con 10 edades de personas. Imprimir la cantidad de personas con edades superiores a 20.
# Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.


def Older20(Tupla):
    newTupla = ()  # nueva tupla donde se almacenaran las personas que son mayores de 20
    for Age in Tupla:
        if int ( Age ) > 20:
            newTupla = newTupla + (Age,)
            lengTuplaFinal = len ( newTupla )
            print ( "Personas Mayores de 20: ", lengTuplaFinal )
    return newTupla


def Prompting():  # Funcion que permite al usuario ingresar las edades
    X = ()  # Tupla argumento de la funcion principal
    for i in range ( 10 ):
        X = X + (input ( "Ingresa edad #" + str ( i + 1 ) + ":" ),)  # El +1 solo es un detalle para organizacion
    return X


main = Older20 ( Prompting () )

print ( main )
