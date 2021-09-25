N =  int(input("ingrese el valor de N"))
X =  int(input("ingrese el valor de X"))

listaA = []
listaB = []

cantListaA_Mayor4 = 0
cantListaB_Mayor4 = 0

for i in range(N):

	if i%3 == 0:
		listaA.append(2 * i)
	elif i%3 == 1:
		listaA.append(2 * listaA[i-1])
	else:
		listaA.append(3 * listaA[i-1])

	if listaA[i] >= 4:
		cantListaA_Mayor4 += 1

for i in range(N):

	if i > 2*N/3:
		listaB.append(X-i)
	elif i < N/3:
		listaB.append(i)
	else:
		listaB.append(X + i)

	if listaB[i] >= 4:
		cantListaB_Mayor4 += 1

print(listaA)
print(listaB)

if cantListaA_Mayor4 > cantListaB_Mayor4:
	print("La lista A tiene más valores mayores a 4 con ",cantListaA_Mayor4)
elif cantListaB_Mayor4 > cantListaA_Mayor4:
	print("La lista B tiene más valores mayores a 4 con ",cantListaB_Mayor4)
else:
	print("Es la misma cantidad en ambas listas con ",cantListaA_Mayor4)

cantImpares_listaA = 0
cantImpares_listaB = 0
for x in range(N):
	if listaA[x]%2 != 0:
		cantImpares_listaA += 1

	if listaB[x]%2 != 0:
		cantImpares_listaB += 1

porcListaA = round(cantImpares_listaA/N*100,2)
porcListaB = round(cantImpares_listaB/N*100,2)

print("Porcentaje de impares en A ",porcListaA)
print("Porcentaje de impares en B ",porcListaB)

sumaB = 0
for x in listaB:
	sumaB += x

print(sumaB)