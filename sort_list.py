


students =[
        {
            "age": 28,
            "name": "Sherman"
        },
        {
            "age": 31,
            "name": "Howell"
        },
        {
            "age": 37,
            "name": "Silva"
        },
        {
            "age": 23,
            "name": "Turner"
        },
        {
            "age": 26,
            "name": "Peters"
        },
        {
            "age": 33,
            "name": "Frank"
        },
        {
            "age": 22,
            "name": "Lynn"
        },
        {
            "age": 23,
            "name": "Obrien"
        },
        {
            "age": 21,
            "name": "Armstrong"
        },
        {
            "age": 39,
            "name": "Herman"
        },
        {
            "age": 25,
            "name": "Gates"
        }
    ]


name_sort = sorted(students, key=lambda k: k['name'])
age_sort = sorted(students, key=lambda k: k['age'])
print (name_sort)
print(age_sort)
#сортировка по убыванию
name_sort = sorted(students, key=lambda k: k['name'],reverse=True)
age_sort = sorted(students, key=lambda k: k['age'],reverse=True)
print (name_sort)
print(age_sort)



