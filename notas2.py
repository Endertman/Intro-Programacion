num_alumnos = int(input("ingrese el numero de alumnos: "))
aprobados = 0
reprobados = 0
alum_6 = 0
alum_2y9 = 0


for i in range(0,num_alumnos):
  nota = int(input('ingrese la nota del alumno: '))
  while nota < 6 & > 2:
    alum_2y9 += 1
    if nota < 4:
      reprobados += 1
    else:
      aprobados +=1
  else:
    alum_6 += 1
    
    