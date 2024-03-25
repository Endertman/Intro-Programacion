print('Programa para calcular promedio de notas')
nota1 = float(input('Ingrese la primera nota: '))
nota2 = float(input('Ingrese la segunda nota: '))
nota3 = float(input('Ingrese la tercera nota: '))
nota4 = float(input('Ingrese la cuarta nota: '))
promedio = (nota1 + nota2 + nota3 + nota4) / 4

while promedio > 5:
  print('El promedio es: ', promedio)
  print('El estudiante aprobo')
  break
while promedio < 5:
  print('El promedio es: ', promedio)
  print('El estudiante reprobo')
  break


