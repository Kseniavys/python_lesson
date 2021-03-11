def division (a, b):
    try:
        c = a // b
    except ZeroDivisionError:
        print('Делить на ноль нельзя')
    return c

print(division(
    int(input('Введите первое число: ')),
    int(input('Введите второе число: '))
))