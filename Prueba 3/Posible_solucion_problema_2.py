def desplegarUnidadesFalla(listaUnidades,listaCantFallas):
    print("Unidades con computadores con falla")
    cantMayor = max(listaCantFallas)
    for x in range(len(listaCantFallas)):
        if listaCantFallas[x] == cantMayor:
            print(">",listaUnidades[x])

listaUnidades = []
listaCantFallas = []
listaFunCompBuenos = []

compMalos = 0
cantAntiguedad2 = 0

contComputadores = 0

archivo = open("computadores.txt","r")
linea = archivo.readline().strip()

while linea != "":
    infoUnidad = linea.split(",")
    nombreUnidad = infoUnidad[0]
    cantComputadores = int(infoUnidad[1])
    contComputadores += cantComputadores
    cantFallas = 0
    for x in range(cantComputadores):
        linea = archivo.readline().strip()
        infoEmpleado = linea.split(",")
        nombreEmpleado = infoEmpleado[0]
        estadoComputador = infoEmpleado[1]
        cantAños = int(infoEmpleado[2])
        
        if estadoComputador == "falla":
            cantFallas += 1

        elif estadoComputador == "malo":
            compMalos += 1
        else:
            listaFunCompBuenos.append(nombreEmpleado)
        
        if cantAños >= 2:
            cantAntiguedad2 += 1
        
    listaUnidades.append(nombreUnidad)
    listaCantFallas.append(cantFallas)
    linea = archivo.readline().strip()

#Requerimiento 1
desplegarUnidadesFalla(listaUnidades,listaCantFallas)

#Requerimiento 2
porcentaje = round(compMalos/contComputadores*100,2)
print("% de computadores malos: ",porcentaje)

#Requerimiento 3
print("Computadores con una antigüedad mayor o igual a 2 años: ",cantAntiguedad2)

#Requerimiento 4
print("funcionarios con computadores buenos")
listaFunCompBuenos.sort()
for x in listaFunCompBuenos:
    print(">",x)
