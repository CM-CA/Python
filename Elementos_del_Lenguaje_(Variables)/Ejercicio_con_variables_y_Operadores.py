# Ejemplo con variables y operadores

monto_bruto = 120
interes = 15
monto_interes = monto_bruto * interes / 100
tasa_bonificacion = 5
importe_bonificacion = monto_bruto * tasa_bonificacion / 100
monto_neto = (monto_bruto - importe_bonificacion) + monto_interes
print('el monto bruto es:', monto_bruto,
      'el importe de bonificacion es:', importe_bonificacion,
      'el monto neto es:', monto_neto)
