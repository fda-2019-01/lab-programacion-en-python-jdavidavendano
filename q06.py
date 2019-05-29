##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
##


'''

aaa,0,9
bbb,0,9
ccc,0,9
ddd,0,9
eee,0,7
fff,0,9
ggg,0,9
hhh,0,9
iii,0,9
jjj,0,9

'''


from libM import generateMatrix

t = []

for row in generateMatrix():
    t.extend(row[4].split(','))

d = {}
h = []
for element in t:
    l, n = element.split(':')
    if l in d:
        d[l] += str(' '+n)
    else:
        d[l] = str(n)
        h.append(l)

for i in sorted(h):
    print(i, min(d[i].split(' ')), max(d[i].split(' ')), sep=',')
