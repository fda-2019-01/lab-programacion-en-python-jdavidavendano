##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##

from libM import generateMatrix

d = {}
h = []

for row in generateMatrix():
    if row[0] in d:
        d[row[0]] += int(row[1])
    else:
        d[row[0]] = int(row[1])
        h.append(row[0])

for i in sorted(h):
    print(i, d[i], sep=',')