str = input(f'Input str:')
symb = input (f'Input symbol:')
str = str.upper()
symb = symb.upper()

def symb_in_line(str,symb):

    counter = 0

    for i in str:
        if i == symb:
            counter+=1

    print(f'The {symb} in {str} = {counter}')

symb_in_line(str,symb)



