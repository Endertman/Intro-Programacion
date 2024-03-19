import math

print('Calculadora de raices cuadraticas')
a = int(input('ingrese el valor de a: '))
b = int(input('ingrese el valor de b: '))
c = int(input('ingrese el valor de c: '))

resultado1 = ((-b + (b**2 - 4*a*c)**0.5)/2)
resultado2 = ((-b + (b**2 + 4*a*c)**0.5)/2)

print(f'Los resultados son {resultado1} y {resultado2}')


