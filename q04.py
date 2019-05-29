##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##

from libM import generateMatrix

d = {}
h = []

for row in generateMatrix():
    rh = row[2].split('-')[1]
    if rh in d:
        d[rh] += 1
    else:
        d[rh] = 1
        h.append(rh)

for i in sorted(h):
    print(i, d[i], sep=',')