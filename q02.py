##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##

from libM import generateMatrix

d = {}
h = []

for row in generateMatrix():
    if row[0] in d:
        d[row[0]] += 1
    else:
        d[row[0]] = 1
        h.append(row[0])

for i in sorted(h):
    print(i, d[i], sep=',')