# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

def array_integer (numbers):
    new_array = []
    for i in numbers:
        new_array.append(i)
        #new_array.sort()
    print(*sorted(new_array) [:2])
    #print (new_array[:2])

array_integer ([78,45,-1,3,0,4,6,76])
