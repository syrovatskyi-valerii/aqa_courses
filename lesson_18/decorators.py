# 1. Напишіть декоратор, який логує аргументи та результати викликаної функції.

import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def log_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f'Виклик функції: {func.__name__}')
        logging.info(f'Аргументи функції: args={args}, kwargs={kwargs}')
        result = func(*args, **kwargs)
        logging.info(f'Результат виконання функції: {result}')
        return result
    return wrapper


@log_decorator
def count_sum(a: int|float, b: int|float):
    if (type(a) != int and type(a) != float) or (type(b) != int and type(b) != float):
        return 'Увага: аргументи мають бути числами'
    return a + b

count_sum(a=1, b=1)      # іменовані аргументи
count_sum(2,2)     # позиційні аргументи


# 2. Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.

def exception_interceptor(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs), 'Успішне виконання функції'
        except Exception as e:
            print(f"Виняток у функції {func.__name__}: {e}")
            return None, 'Спрацював виняток та функція не відпрацювала'
    return wrapper


@exception_interceptor
def divide(a, b):
    return a / b

print(divide(a=10, b=2))
print(divide(a=10, b=0))  # тут спрацює виняток, бо ділення на 0 неможливе
