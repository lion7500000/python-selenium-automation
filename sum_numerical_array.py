#Найти сумму всех цифр целочисленного массива. Например, если дан массив [12, 104, 81],
#то сумма всех его цифр будет равна 1 + 2 + 1 + 0 + 4 + 8 + 1 = 17.
from random import random

N= 5
a = []
sum_arr = []

for i in range(N):
    a.append(int(random()*30))
print (a)
for i in a:
    sum_arr.append(str(i))
print(sum(map(int, list(''.join(sum_arr)))))