# def string (n):
#     revers_string = n[::-1]
#     return revers_string
#
# print (string("Cat is my"))

def prime_number (n):
    if (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for x in range(2,n):
            if (n % x == 0):
                return False
        return True

print(prime_number(1))
