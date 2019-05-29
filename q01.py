##
## Imprima la suma de la segunda columna.
##

from libM import generateMatrix

print(sum([int(row[1]) for row in generateMatrix()]))
