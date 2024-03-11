print('Hello World!')
print('Hola Mundo')
print(7*5)
print(80/7)
print(5+5)
print(5-5)
print('Hola'*10)

#forma 1
nombre = 'Juan'
apellido = 'Perez'
direccion = 'Calle 1'
edad = 30

print(f'Su nombre es {nombre} {apellido} y vive en {direccion} y tiene {edad} años, y dentro de 12 años tendra {edad+12} años')

#forma 3
template = 'Su nombre es {}, su apellido es {}'.format(nombre, apellido)
print(template)
