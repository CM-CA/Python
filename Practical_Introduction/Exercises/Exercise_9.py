def propina():
    precio_comida = input ( "¿Cual es el precio de la comida? " )
    propina = input ( "¿Cual es % que piensas dejarle al camarero? " )
    porcentaje_propina = float ( propina )  / 100
    total = float ( precio_comida ) * porcentaje_propina
    print ( "El total de la comida es: ", precio_comida, " y de propina dejas: ", round ( total, 2 ) )


propina ()
