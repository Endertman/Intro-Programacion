import random

print('programa para contar pares e impares')
num_evaluar = int(input("ingrese el cuantos numeros desea evaluar:"))
pares = 0
impares = 0
ranint = random.randint(10000,10000000)

for i in range(0,ranint):
  num = random.randint(0,10000)
  if num % 2 == 0:
    pares += 1
  else:
    impares += 1

print('la cantidad de pares es: ', pares)
print('la cantidad de impares es: ', impares)
  