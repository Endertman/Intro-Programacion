print('Programa para ordenar numeros de mayor a menor')
a = int(input('Ingrese el primer numero: '))
b = int(input('Ingrese el segundo numero: '))
c = int(input('Ingrese el tercer numero: '))
if a > b and a > c:
  if b > c:
    print(f'Sus numeros son: {a,b,c}')
  else:
    print(f'Sus numeros son: {a,c,b}')
elif b > a and b > c:
  if a > c:
    print(f'Sus numeros son: {b,a,c}')
  else:
    print(f'Sus numeros son: {b,c,a}')
elif c > a and c > b:
  if a > b:
    print(f'Sus numeros son: {c,a,b}')
  else:
    print(f'Sus numeros son: {c,b,a}')
else:
  print('Los numeros ingresados son iguales')

