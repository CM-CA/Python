# Dar formato,sustituyendo texto dinamicamente

cadena_1 = "Photonic coordinates lead to the ellipse. {0}"
print(cadena_1.format("Texto de prueba"))
print('')
cadena_2 = "Importe bruto: ${0} + IVA: ${1} = Importe neto: {2}"
print(cadena_2.format(100, 21, 21))
print('')
cadena_3 = "Importe bruto: ${bruto} + IVA: ${iva} = Importe neto: {neto}"
print(cadena_3.format(bruto=100, iva=21, neto=121))
