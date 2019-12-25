from random import random

M = 5
N = 5
P= 100
a = []
for i in range( N ):
    b = []
    for j in range( M ):
        n = int( random() * P )
        b.append( n )
        print( '%4d' % n, end='' )
    a.append( b )
    print()

mx_min = -1
for k in range( M ):
    mn_max = P
    for i in range( N ):
        if a[i][k] < mn_max:
            mn_max = a[i][k]
    if mn_max > mx_min:
        mx_min = mn_max
print( "The maximum among the minimum: ", mx_min )
