#Calcule el promedio de notas
x1 = 0
for i in range (0,10):
  notas = float(input('ingrese la nota: '))
  x1= x1 + notas
pg = x1/10
print('el promedio es',pg)