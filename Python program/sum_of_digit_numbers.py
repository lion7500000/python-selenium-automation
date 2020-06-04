import random
from random import randint
#from random import random


dig = int(input(f'Enter the number of numbers:'))


while dig <= 0 :
    dig = int(input(f'Enter the number > 0:'))

n= randint(9**dig, 99**dig)

num = ' '
sum = 0

for i in range (dig):
    num = num + random.choice(str(n))
print ('random num : {}'.format(num))

num_int = int(num)

while num_int>0:
    temp_num = num_int%10
    num_int = num_int//10
    sum += temp_num
print ('sum: {}'.format(sum))
