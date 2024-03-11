import math

print('Calculadora de raices cuadraticas')
a = int(input('ingrese el valor de a: '))
b = int(input('ingrese el valor de b: '))
c = int(input('ingrese el valor de c: '))

resultado1 = ((-b + (b**2 - 4*a*c)**0.5)/2)
resultado2 = ((-b + (b**2 + 4*a*c)**0.5)/2)

print(f'Los resultados son {resultado1} y {resultado2}')

resultado1=1
resultado2=2

if resultado1 == resultado2 :
  print(f'los resultados son iguales')
elif resultado1 > resultado2 :
  print(f'el resultado 1 es mayor: {resultado1}')
else:
  print(f'El resultado mayor es {resultado2}')

