str = input("Input string:")
old_substr = input("Input substring wich you want to change:")
new_substr = input("Input new substring for change:")

len_old_str = len(old_substr)

#find first symbol old_substr if not it will -1
while str.find(old_substr)>0:

    #save index in i
    i = str.find(old_substr)
    #rewrite str: slice from start to index + new_substr
    str = str[:i]+ new_substr + str[i+len_old_str:]

print (f'New string: {str}')

#alternative method

while str.find(old_substr) != -1:
    str = str.replace(old_substr,new_substr)

print (f'New string: {str}')
