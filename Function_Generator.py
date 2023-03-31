def fact(n):
    pr = 1
    for i in range(1, n + 1):
        pr = pr * i
        yield pr


for i in fact(10):
    print(i, end=' ')


def genf():
    for i in [43, 65, 32]:
        yield i


for i in genf():
    print(i)

# Функция генератор функции, которые могут возвращать по одному значению, при этом «замораживая» своё выполнение,
# и при новом вызове функции она будет выполняться с того места, на котором она остановилась. Такая функция называется функцией генератором.
# Обратите внимание на то, что вместо ключевого слова return  в функции генераторе используется другое ключевое слово – yield

def gen_squares(n):
    for i in range(1, n + 1):
        yield i ** 2


for i in gen_squares(3):
    print(i)


def gen_fibonacci_numbers(n): # САМ НАПИСАЛ ГЕНЕРАТОР ФИБОНАЧЧИ! 12.17 28 марта 2013 год Люблю Сашу
    a = 1
    b = 1

    for i in range(n):
        yield a
        a, b = b, a + b


for i in gen_fibonacci_numbers(10):
    print(i)


#ГЕНЕРАТОР ФУНКЦИИ RANGE , работает в точности как функция, с положительным и отрицательным шагом.

def my_range_gen(start, stop=0, step=1):
    if stop and step > 0:
        i = start
        while i < stop:
            yield i
            i += step
    if stop and step < 0:
        i = start
        while i > stop:
            yield i
            i += step

    if not stop:
        i = 0
        while i < start:
            yield i
            i += 1


for i in my_range_gen(1, 10, -2):
    print(i)