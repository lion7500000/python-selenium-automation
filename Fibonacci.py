n = int(input("Input positive number for Fibonacci: "))
while n<=0:
    n = int( input( "Input only positive number for Fibonacci: " ) )

def fibonacci(n):
    fib1 = fib2 = 1
    if n < 2:
        quit()

    print( fib1, end='->')
    print( fib2,end='->')
    for i in range( 2, n ):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2,end='->')


def fibonacci2(n):
    fib1 = 1
    fib2 = 2
    if n in (fib1, fib2):
        return fib1
    return fibonacci2(n - fib1) + fibonacci2(n - fib2)

print(fibonacci(n))
print( fibonacci2(n) )


