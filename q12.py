##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##

from libM import generateMatrix

d = {}
h = []

for row in generateMatrix():
    for l in row[3].replace(',', ''):
        if l in d:
            d[l] += int(row[1])
        else:
            d[l] = int(row[1])
            h.append(l)

for i in sorted(h):
    print(i, d[i], sep=',')