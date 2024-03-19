'''
Escriba un algoritmo tal que  dado como datos, el modelo del vehiculo y su precio. determine el valor final que debe pagar el comprador. el concesionario esta haciendo descuentos teniendo en cuenta el modelo con base a la siguiente tabla:

numero de modelo, modelo, descuento
1,curtlass,8%
2,cavalier,5%
3,chevy,6%
4,century 9%
'''

print('Programa para calcular precios de vehiculos con descuento')

print('Seleccione uno de los siguentes modelos: \n1. Curtlass \n2. Cavalier \n3. Chevy \n4. Century')

modelo = int(input('Ingrese el numero del modelo: '))
precio = int(input('Ingrese el precio del vehiculo: '))

if modelo == 1:
  descuento = precio*0.08
  print('Tiene un descuento del 8%')
elif modelo == 2:
  descuento = precio*0.05
  print('Tiene un descuento del 5%')
elif modelo == 3:
  descuento = precio*0.06
  print('Tiene un descuento del 6%')
elif modelo == 4:
  descuento = precio*0.09
else:
  print('El modelo ingresado no es valido')

print(f'El costo final del vehiculo es: {precio-descuento}')

