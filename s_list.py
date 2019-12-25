#Дан лист. Вернуть лист, состоящий из элементов, которые меньше среднего арифметического
# исходного листа. С.а. = сумма элементов разделить на количество.


def list (array):

    s_a = sum( array ) / len( array )
    new_list = []

    for i in array:
        if i < s_a:
            new_list.append(i)
    print (f's_a= {s_a}')
    print (new_list)
list ([10,3,1,2,3,5])





