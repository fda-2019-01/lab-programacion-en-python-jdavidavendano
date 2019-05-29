##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##

from libM import generateMatrix

for row in generateMatrix():
    print(row[0], len(row[3].split(',')), len(row[4].split(',')), sep=',')

