# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 17:55:21 2021

@author: Desarrollo
"""

# dngdhndsvsdvsdvsdv



# prueba conexion

# ------Calcule el valor de Y indicando paso a paso como llegó al resultado 1.1
# 1.1    y = ( (5+2-5)^2 * 5+8/2 -30 ) / 2 * 5 -3
# 1.1    y = ( (2)^2 * 5+ 4 -30 ) / 2 * 5 -3
# 1.1    y = ( 4 * 5 + 4 - 30 ) / 2 * 5 -3
# 1.1    y = (20 + 4 -30 ) / 2 * 5 -3
# 1.1    y = (-6) / 2 * 5 -3
# 1.1    y = -3 * 5 -3
# 1.1    y = -18

ej1_1resultado = ((((5 + 2 - 5) ** 2) * 5 + (8 / 2) - 30) / 2) * 5 - 3
print(f"ej 1.1 y = ((((5+2-5)**2) * 5 + (8/2) -30 ) / 2 )* 5 -3")
print(f"ej 1.1 Resultado: {ej1_1resultado}")

# ------Calcule el valor de Y indicando paso a paso como llegó al resultado 1.2

# z=5
# n=3
# m= z-n
# y = (( (z+2-n)^2 * m+8/2 -30 ) / 2 * 5 -3)^ 5 + 15 * 3 - 9/3 

ej1_2z = 5
ej1_2n = 3
ej1_2m = ej1_2z - ej1_2n
ej1_2resultado = float((((((ej1_2z + 2 - ej1_2n)** 2) * ej1_2m + 8 / 2 - 30) / 2) * 5 - 3)** 5 + 15 * 3 - (9 / 3))
print("ej 1.2 y = ((((5+2-5)**2) * 5 + (8/2) -30 ) / 2 )* 5 -3")
print(f"ej 1.2 Resultado: {ej1_2resultado}")

# ------Calcule el valor de Y indicando paso a paso como llegó al resultado 1.3
# z=5
# n=( (8+2-4)^2 * 5+8+7/2 -30*5 ) / 2 * 5 -3
# m= z^2*3+n
# m= (5)^2*3+(( (8+2-4)^2 * 5+8+7/2 -30*5 ) / 2 * 5 -3)
# y = ((( (z+2-n)^2 x m+8/2 -30 ) / 2 * 5 -3)^ 5 + 15 * 3 - 9/3) ^ 2 – 5/4
# y = ((( (5+2-(( (8+2-4)^2 * 5+8+7/2 -30*5 ) / 2 * 5 -3))^2 * ((5)^2*3+(( (8+2-4)^2 * 5+8+7/2 -30*5 ) / 2 * 5 -3))+8/2 -30 ) / 2 * 5 -3)^ 5 + 15 * 3 - 9/3) ^ 2 – 5/4

ej1_3z = float(5)
ej1_3n = float((((8 + 2 - 4)**2) * 5 + 8 + 7 / 2 - 30 * 5)/ 2 * 5 - 3)
ej1_3m = float(((ej1_3z)**2) * 3 + (ej1_3n))
print(f"ej 1.2 Resultado: {ej1_3m}  ,{ej1_3n} , {ej1_3z} ")


# ej1_3resultado = float( (((((ej1_3z) + 2 - ((ej1_3n)**2) * ej1_3m + 8/2 - 30 ) / 2 * 5 - 3)** 5 + 15 * 3 - 9/3)**2 – 5/4)

ej1_3resultado = float(((((((((ej1_3z)+2-(ej1_3n)) ** 2) * (ej1_3m)+8/2 -30 ) / 2 * 5 -3) ** 5) + 15 * 3 - 9/3) ** 2) - (5/4))

print("ej 1.3 y = y = ((( (5+2-(( (8+2-4)^2 * 5+8+7/2 -30*5 ) / 2 * 5 -3))^2 * ((5)^2*3+(( (8+2-4)^2 * 5+8+7/2 -30*5 ) / 2 * 5 -3))+8/2 -30 ) / 2 * 5 -3)^ 5 + 15 * 3 - 9/3) ^ 2 – 5/4")
print(f"ej 1.3 Resultado: {ej1_3resultado}")


# ------ Desarrollo de algoritmos------ Taller parte 2

# ejercicio 1.

pres = float(input('digite el valor de la presión: '))
vol = float(input('digite el valor del volumen: '))
temp = float(input('digite el valor de la temperatura: '))
masa = (pres*vol)/((temp+460) * 0.37)

print(f'El valor de la masa es: {masa}')

# ejercicio 2. 

edad = int(input('digite la edad de la persona: '))
pulsaciones = (200-edad)/10

print(f'La persona debe tener: {pulsaciones} / s')

# ejercicio 3.

inversion1 = float(input('Digite el valor invertido por el primer socio: $ '))
inversion2 = float(input('Digite el valor invertido por el segundo socio: $ '))
inversion3 = float(input('Digite el valor invertido por el tercer socio: $ '))

inversionTotal = inversion1 + inversion2 + inversion3
porcentaje1 = (inversion1/inversionTotal)*100 
porcentaje2 = (inversion2/inversionTotal)*100
porcentaje3 = (inversion3/inversionTotal)*100

print(f'El porcentaje que invirtió el primer socio es: {porcentaje1} %')
print(f'El porcentaje que invirtió el segundo socio es: {porcentaje2} %')
print(f'El porcentaje que invirtió el tercer socio es: {porcentaje3} %')

# ejercicio 4.

saldoIni = float(input('Digite el saldo inicial: $'))
interes = saldoIni * 0.015
saldoFin = saldoIni - interes

print(f'El saldo final del ahorrador es: ${saldoFin}')

# ejercicio 5.

sueldoBase = float(input('Digite el sueldo base: $'))
leyPublica = sueldoBase * 0.01
seguroSocial = sueldoBase * 0.04
seguroForzoso = sueldoBase * 0.005
cajaAhorro = sueldoBase * 0.05

totalDes = leyPublica + seguroSocial + seguroForzoso + cajaAhorro

print(f'El descueto de la ley publica es: ${leyPublica}')
print(f'El descueto del seguro social es: ${seguroSocial}')
print(f'El descueto del seguro forzoso es: ${seguroForzoso}')
print(f'El descueto por caja de ahorro es: ${cajaAhorro}')

print(f'El total a pagar es: ${totalDes}')

# ejercicio 6.

palabras = int(input('Digite la cantidad de palabras: '))
centimetros = int(input('Digite los centimetros: '))
colores = int(input('Digite la cantidad de colores: '))
valorPalabras = palabras * 20000
valorCentimetros = centimetros * 15000
valorColores = colores * 25000
valorTotal = valorPalabras + valorCentimetros + valorColores

print(f'El total a pagar por el aviso es: ${valorTotal}')

# ejercicio 7. 

años = float(input('Digite la cantidad de años elaborados en la empresa: '))
bono = ( años * 120000) - 20000
print(f'El valor de su bono es: ${bono}')

# ejercicio 8.

h = int(input('Digite la cantidad de horas: '))
base = h * 20000
desc = base * 0.05
paga = base - desc

print(f'El sueldo del profesor es: ${paga}')

# ejercicio 9. 

saldoInicial = int(input('Digite el monto inicial de la tarjeta: '))
saldoFinal = int(input('Digite el monto final de la tarjeta: '))
costo = (saldoInicial - saldoFinal) * 1.20 

print(f'El costo de la llamada es: ${costo}')

# ejercicio 10. 

fotos = int(input('Digite la cantidad de fotos a revelar: '))
valor = (fotos *1500 )*1.16

print(f'El valor a pagar es: ${valor}')

# ejercicio 11.

presupuesto = float(input('Digite el monto presupuestal total: $'))
ginecologia = presupuesto * 0.4
traumatologia = presupuesto * 0.3
pediatria = presupuesto * 0.3

print(f'El presupuesto de Ginecología es de: ${ginecologia}')
print(f'El presupuesto de Traumatología es de: ${traumatologia}')
print(f'El presupuesto de Pediatría es de: ${pediatria}')

# ejercicio 12.

peliculas = int(input('Digite la cantidad de peliculas a alquilar: '))
dias = int(input('Digite la cantidad de días que tendrá las peliculas: '))
promocion = 1500
precio = ((peliculas * 1500) * dias ) - promocion

print(f'El valor a pagar por el alquiler es: ${precio}')

# ejercicio 13.

personas = int(input('Digite la cantidad de personas en la famimlia: '))
dias = int(input('Digite la cantidad de dias del tour: '))
precioBase = (personas * 25000) * dias 
IVA = (precioBase * 12) / 100
totalTour = IVA + precioBase

print(f'El valor a pagar por el tour es: ${totalTour}')


# ejercicio 14.

dias = float(input('Digite la cantidad de dias durante la estadía: '))
valor = (dias * 200000)-100000

print(f'El valor de su estadia es: ${valor}')

# ejercicio 15.

prestamo = float(input('Digite la cantidad prestada al empresario: $'))
baseCuotaEsp = prestamo/2
cuotaEsp = baseCuotaEsp / 4
valorCuotaEsp = cuotaEsp + (cuotaEsp * 0.24)
baseCuotaOrdinaria = prestamo / 2
cuotaOrdinaria = baseCuotaOrdinaria / 20
valorCuotaOrdinaria = cuotaOrdinaria + (cuotaOrdinaria * 0.24)
totalAPagar = (valorCuotaEsp * 4) + (valorCuotaOrdinaria * 20)

print(f'El valor de cada cuota especial es de: ${valorCuotaEsp}')
print(f'El valor de cada cuota ordinaria es de: ${valorCuotaOrdinaria}')
print(f'El monto total a pagar es de: ${totalAPagar}')
