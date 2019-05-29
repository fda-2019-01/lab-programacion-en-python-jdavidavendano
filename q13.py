##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##

from libM import generateMatrix

for row in generateMatrix():
    print(row[0], sum([int(i.split(':')[1]) for i in row[4].split(',')]), sep=',')
