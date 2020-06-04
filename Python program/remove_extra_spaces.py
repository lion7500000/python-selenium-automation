import re

str = input ('Input text:')
print (re.sub(r'\s+',' ',str))

# #alternative
# print(''.join(str.split('')))
#
# #alternative
s = str.strip()
if s.count('  ')>0:
    while s.count('  ') > 0:
        new_str = s.replace('  ',' ')
        s=new_str
    print(s)
else:
    print(s)
