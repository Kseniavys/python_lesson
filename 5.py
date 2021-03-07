my_list = [7, 5, 3, 3, 2]
new_el = int(input('Введите любое число от 1 до 10: '))
i = 0

for el in my_list:
    if new_el <= el:
        i+=1
my_list.insert(i, int(new_el))
print(my_list)

