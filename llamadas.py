print('Programa para calcular el costo de una llamada telefonica')
clave = int(input('Ingrese la clave de la zona: '))
min = int(input('Ingrese la duracion de la llamada en minutos: '))
if clave == 12:
  print(f'Su llamada fue a America del norte y tuvo un costo de: ', min*2)
elif clave == 15:
  print(f'Su llamada fue a America Central y tuvo un costo de: ', min*2)
else:
  print('En este momento no podemos calcular el costo de su llamada')

