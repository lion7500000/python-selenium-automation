str = input ('Input text:')
# converting string to list
list_str = str.split()
# index max word = 0
max_word = 0

# for i in range(1,len(list_str)):
#     if len(list_str[max_word])<len(list_str[i]):
#         max_word = i
#
# print (list_str[max_word])

#alternative
def max (str):
    max = 0
    for i in str.split(' '):
        if max< len(i):
            max = len(i)
            word = i
    print (f'Longest word - {word}, {max} symbols')

max(str)
