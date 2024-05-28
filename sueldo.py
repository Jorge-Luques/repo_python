sueldo = int(input("Ingrese el sueldo: $"))
if (sueldo >= 60000 and sueldo < 250000):
    print("Ganas mas que el SMVM")
else:
    print("Ganas poco")

if (sueldo > 250000):
    print("Tienes que pagar impuesto a la ganancia")

# Probando estructura anidada
if sueldo < 60000:
    print("El sueldo es bajo")
elif sueldo <= 250000:
    print("el sueldo es medio")
else:
    print("el sueldo es alto y debe pagar impuesto")

print("TU sueldo es de "+ str(sueldo))
#probando si puede cambiar el tipo
sueldo = "NADA"
print("TU sueldo es de "+ str(sueldo))
sueldo = 250000.05
print("TU sueldo es de "+ str(sueldo)+" y tiene que pagar impuesto")
