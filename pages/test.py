#Number (3,5,4,2,7,1)

# big_number = [3,5,4,2,7,1]
#
# count = 0
# for i in big_number:
#     if count < i:
#         count = i
# print(count)

# def big_number(n):
#     count = 0
#     for i in n:
#         if count < i:
#             count = i
#     return f' Max number is: {count}'
#
#
# print(big_number ([3,5,4,2,7,1]))
#big_number ([3,5,4,2,7,1])

# def array (n):
#     array = []
#     sum = 0
#     neg_num = -1
#     for i in range(n):
#         array.append(i)
#         if i < 0:
#             neg_num = i
#             print (neg_num)
#             break
#         # elif i == -1:
#         #     return f' No negative element '
#         # else:
#         #     for i in range(neg_num+1,array):
#         #         sum += abs(array[i])
#         #     return  sum
#
# print(array([1,3,-4,5]))

#print (int('AB', 16))

# values = input('Введите числа через запятую: ')
# ints_as_strings = values.split(',')
# ints = map(int, ints_as_strings)
# lst = list(ints)
# tup = tuple(lst)
# print('Список:', lst)
# print('Кортеж:', tup)

# set_1 = set(['White', 'Black', 'Red'])
# set_2 = set(['Red', 'Green'])
#
# print(set_1 - set_2)

def sum_digits(num):
    digits = [int(d) for d in str(num)]
    return sum(digits)

print(sum_digits(5245))


