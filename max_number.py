a = int(input (f'enter number 1: '))
b = int(input (f'enter number 2: '))
c = int(input (f'enter number 3: '))

def max_number(a,b,c):
    if a>b and a>c:
        return ('Max number: {}'.format(a))
    elif b>a and b>c:
        return('Max number: {}'.format(b))
    else:
        return('Max number: {}'.format(c))

print (max_number(a,b,c))