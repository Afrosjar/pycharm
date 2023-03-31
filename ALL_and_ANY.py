# Функция all принимает итерабельную последовательность и возвращает True , когда все элементы в этой последовательности
# правдивы. Если хотя бы один элемент пустой, вернется False
a = ['hi', 'hello', 'world']
print(all(a))

b = ['hi', '', 'world' ]
print(all(b))

numbers = [1, 2, 3, 4, 5]
print(all(numbers))
print(all([1, 2, 0, 4, 5]))

print(all([True, True, True]))
print(all([True, False, True]))

# Any тоже принимает на вход итерабельную последовательность и возвращает True,
# если хотя бы один из элементов коллекции будет непустым. Если все элементы пустые, вернется False
a = ['hi', 'hello', 'world']
print(any(a))

b = ['', '', '' ]
print(any(b))

numbers = [1, 0, 3, 0, 0]
print(any(numbers))
print(any([0, 0, 0, 0]))

print(any([False, False, True]))
print(any([False, False, False]))

a = 100
condition_1 = a % 2 != 0
condition_2 = a > 50
condition_3 = a < 1000

print(all((condition_1, condition_2, condition_3)))
print(any([condition_1, condition_2, condition_3]))

# При помощи функций all и any очень удобно проверять все значения коллекции на соответствие определенному условию.
# А для быстрого обхода значений можно и нужно использовать генератор списка.

words = ['notice', 'deter', 'west', 'brush', 'stadium',
         'package', 'price', 'clothes', 'sword', 'apology']

check = [len(word) >= 4 for word in words]

print(check)
print(all(check))
print(all([len(word) > 4 for word in words]))

print(any([len(word) > 7 for word in words]))
print(any([len(word) >= 7 for word in words]))