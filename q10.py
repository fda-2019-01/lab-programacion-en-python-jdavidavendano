##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##

from libM import generateMatrix

t = []

for row in generateMatrix():
    t.extend(row[4].split(','))

ta = [e.split(':')[0] for e in t]

for i in sorted(set(ta)):
    print(i, ta.count(i), sep=',')
