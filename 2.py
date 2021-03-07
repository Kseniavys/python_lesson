list = []

list.append(input('Введите Ваше имя: '))
list.append(input('Введите Вашу фамилию: '))
list.append(input('Ваша профессия: '))
list.append(input('Город проживания: '))

list[0], list[1] = list[1], list[0]
list[2], list[3] = list[3], list[2]

print(list)

