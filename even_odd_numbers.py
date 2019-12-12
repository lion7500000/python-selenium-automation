n = int(input("Input positive number: "))
while n<=0:
    n = int( input( "Input only positive number: " ) )

def num(n):
    even = 0
    odd = 0

    while n>0:
        if n % 2 == 0:
            even +=1

        else:
            odd +=1

        n = n // 10

    print ('even numbers: {}'.format(even))
    print ('odd numbers: {}'.format(odd))

num(n)
