#Вычислить сумму модулей элементов массива, расположенных после первого отрицательного элемента.
# Например, в массиве [5, 3, -1, 8, 0, -6, 1] первый отрицательный элемент является третьим по счету,
# а сумма модулей стоящих после него элементов массива будет составлять 8 + 0 + 6 + 1 = 15.
from random import random

N=10
array = []
sum = 0
neg = -1

for i in range(N):
    array.append(int(random() * 30) - 5)
print(array)

for i in range(N):
    if array[i] < 0:
        neg = i
        break

if neg == -1:
    print('No negative element')

else:
    print('Number of first negative element:', neg+1)

    for i in range(neg+1,N):
        sum += abs(array[i])

    print('Amount: ', sum)
