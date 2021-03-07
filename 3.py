list = ['Зима', 'Весна', 'Лето', 'Осень']
dict = {
    1: 'Зима',
    2: 'Весна',
    3: 'Лето',
    4: 'Осень'
}

month = int(input('Введите номер месяца: '))
if month == 12 or month == 1 or month == 2:
    print(list[0])
    print(dict.get(1))

elif month == 3 or month == 4 or month == 5:
    print(list[1])
    print(dict.get(2))

elif month == 6 or month == 7 or month == 8:
    print(list[2])
    print(dict.get(3))

elif month == 9 or month == 10 or month == 11:
    print(list[3])
    print(dict.get(4))