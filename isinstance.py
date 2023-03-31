# Она принимает на входа два аргумента:
# значение, которое вы хотите проверить, а вторым вы пишите тип,
# на который нужно проверить, навыходе функция выводит True, если условие истинно.

a = [5, 3, 'hello', [3, 4], ' world', [5], 10.5]
sum_list = []
for i in a:
    if isinstance(i, list):
        sum_list = sum_list + i
print(sum_list)

a = [5, 3, 'hello', [3, 4], ' world', [5], 10.5]
sum_string = ''
for i in a:
    if isinstance(i, str):
        sum_string = sum_string + i
print(sum_string)

a = [5, 3, 'hello', [3, 4], ' world', [5], 10.5]
sum_nums = 0
for i in a:
    if isinstance(i, int):
        sum_nums += i
print(sum_nums)


# Функция считает количество строк в входном потоке
def count_strings(*args):
    count = 0
    for i in args:
        if isinstance(i, str):
            count += 1
    return count


a = [5, 3, 'hello', [3, 4], ' world', [5], 10.5]
sum_nums = 0
for i in a:
    if isinstance(i, (int, float)):
        sum_nums += i
print(sum_nums)
