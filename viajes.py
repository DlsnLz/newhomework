import random 
# simulando el mejor recorrido de viajes.
# se crea la matriz w que se pide

W = []

# estructura de la matriz; 6 x 6

print 'La matriz a ingresar debe ser de 6 x 6, con elementos diferentes de\n0 y enteros negativos...'

filas = int(raw_input('ingrese filas para la matriz:' ' '))
columnas = int(raw_input('ingrese columnas para la matriz:' ' '))

# se imprime la matriz de tal forma que : [],[],[],[],[],[]

for e in range(filas):
  W.append([0]*columnas)
    
# Los elementos que se ingresan son los costos entre ciudades, las filas y las columnas
# representaran ciudades.
print '\n'
print 'llenar matriz. . .'
for i in range(filas):
  for j in range(columnas):
    W[i][j] = int(raw_input('elemento %d, %d:' ' '  %(i,j)))

print '\n'
print 'la matriz es la siguiente:'
for x in W:
  print x
print '\n'

# recorrer la matriz por fila y almacenar el valor min entre fila y columna como
# los 6 costos mas bajos.
# la posicion de estos elementos en orden ascendente es la ruta que debe coger el vendedor
# para optimizar el costo del viaje a las 6 ciudades

c0 = min(W[0])
c1 = min(W[1])
c2 = min(W[2])
c3 = min(W[3])
c4 = min(W[4])
c5 = min(W[5])

# se ingresan los costos min totales de tal manera que queden en una lista
cos_tot = [c0,c1,c2,c3,c4,c5]
print 'costos minimos: %s' %cos_tot

#ordenar los costos min utilizando modulo sort de listas
cos_tot.sort()
print 'costos minimos ordenados: %s' %cos_tot

# buscar la posicion de los elementos de la lista ordenada de los costos a cada ciudad en la matriz,
# usando el modulo index de lista que busca la posicion del valor del elemento.
ciud1 = cos_tot.index(c0)
ciud2 = cos_tot.index(c1)
ciud3 = cos_tot.index(c2)
ciud4 = cos_tot.index(c3)
ciud5 = cos_tot.index(c4)
ciud6 = cos_tot.index(c5)
ciudades = ciud1,ciud2,ciud3,ciud4,ciud5,ciud6

print 'la ruta con un coste optimo para viajar a las 6 ciudades es:' ,ciudades