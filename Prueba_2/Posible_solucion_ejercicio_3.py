listaAsignaturas = []

asignatura = input("ingrese una asignatura distinta de fin: ")

while asignatura != "fin":
    if not asignatura in listaAsignaturas:
        listaAsignaturas.append(asignatura)

    asignatura = input("ingrese una asignatura distinta de fin: ")

listaAsignaturas.sort()

listaAsignaturasMayores = []
listaAsignaturasRojas = []

for asig in listaAsignaturas:
    calificacion = float(input("ingrese la calificación de "+asig))
    if calificacion <= 3.94:
      listaAsignaturasRojas.append(asig)
    else:
        horas = int(input("¿cuántas horas de estudio dedicaste a esta asignatura?"))
        if horas >= 3:
            listaAsignaturasMayores.append(asig)

print("asignaturas con una cantidad de horas mayor a 3")
for x in listaAsignaturasMayores:
    print(x)

porcentajeMayores3 = round(len(listaAsignaturasMayores)/len(listaAsignaturas)*100,2)
print("porcentaje de asignaturas con una cantidad de horas mayor a 3 ",porcentajeMayores3)

porcentajeReprobadas = round(len(listaAsignaturasRojas)/len(listaAsignaturas)*100,2)
print("porcentaje de asignaturas reprobadas ",porcentajeReprobadas)





