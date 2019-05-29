##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##

from libM import generateMatrix

d = {}
h = []

for row in generateMatrix():
    if row[0] in d:
        d[row[0]] += str(' '+row[1])
    else:
        d[row[0]] = str(row[1])
        h.append(row[0])

for i in sorted(h):
    print(i, max(d[i].split(' ')), min(d[i].split(' ')), sep=',')