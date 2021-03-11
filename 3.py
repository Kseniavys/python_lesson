def my_func(a, b, c):
    list = [a, b, c]
    list.remove(min(a, b, c))
    return sum(list)

print(my_func(5, 4, 1))