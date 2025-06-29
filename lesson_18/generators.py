# 1. Напишіть генератор, який повертає послідовність парних чисел від 0 до N.

def pair_numbers_generator(N):

    if not isinstance(N, int) or isinstance(N, bool):
        raise ValueError("N має бути цілим числом")

    i = 0
    while i <= N:
        yield i
        i += 2

for number in pair_numbers_generator(10):
    print(number)


# 2. Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.

def fibonacci_generator(N):
    if not isinstance(N, int) or isinstance(N, bool):
        raise ValueError("N має бути цілим числом")

    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b

for numbers in fibonacci_generator(10):
    print(numbers)