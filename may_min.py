print('Programa para detrerminar numeros mayores')

num_eva = int(input('Ingrese la cantidad de numeros a evaluar: '))
num_sub10 = 0
num_sup50 = 0
num_45_55 = 0

for i in range(0, num_eva):
  num = int(input(f'Ingrese el numero {i+1}: '))
  if num < 10:
    num_sub10 += 1
  elif num > 44:
    num_45_55 += 1
    if num > 50:
      num_sup50 += 1
      if num > 56:
        num_45_55 -= 1

print(f'La cantidad de numeros menores a 10 es: {num_sub10}')
print(f'La cantidad de numeros mayores a 50 es: {num_sup50}')
print(f'La cantidad de numeros entre 45 y 55 es: {num_45_55}')