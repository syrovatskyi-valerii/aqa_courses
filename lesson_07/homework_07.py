# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):

    multiplier = 1

    while multiplier * number <= 25:
        result = number * multiplier
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1

multiplication_table(3)

# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# ======================================================================================================================

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def count_sum(a: int|float, b: int|float):
    if (type(a) != int and type(a) != float) or (type(b) != int and type(b) != float):
        return "Увага: аргументи мають бути числами"
    return a + b

print(count_sum(a=-1, b=1))
print(count_sum(a=True, b=2))
print(count_sum(a='asd', b=3))

# ======================================================================================================================

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
valid_list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
not_valid_list_of_numbers = [1, True]

def average_value(numbers: list):
    if not all(type(k) == int or type(k) == float for k in numbers):
        return "У списку мають бути лише числа"
    return sum(numbers) / len(numbers)

print(average_value(valid_list_of_numbers))
print(average_value(not_valid_list_of_numbers))

# ======================================================================================================================

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def string_back_to_front(any_string: str):
    if type(any_string) != str:
        return "Увага: аргумент мають бути рядком"
    return any_string[::-1]

print(string_back_to_front(any_string='gnirts'))

# ======================================================================================================================

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_word_in_list(list_of_words):
    longest_word = ""
    for word in list_of_words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

test_list_of_words = ['', 'a', 'asdf','as', 'asd']
print(f'Найдовше слово у списку {test_list_of_words}, це - \"{longest_word_in_list(list_of_words=test_list_of_words)}\"')

# ======================================================================================================================

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    if str2 in str1:
        return str1.index(str2)
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# ======================================================================================================================

#
# # task 7
# # task 8
# # task 9
# # task 10
# """  Оберіть будь-які 4 таски з попередніх домашніх робіт та
# перетворіть їх у 4 функції, що отримують значення та повертають результат.
# Обоязково документуйте функції та дайте зрозумілі імена змінним.
# """

# ======================================================================================================================
#  task 7
# list1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
#
# list2 = [k for k in list1 if type(k) is str]
#
# print(list2)

# Функція, яка формує новий список list2, який містить лише змінні типу "стрінг", які присутні в іншому списку.
def check_type_str_in_list(any_list):
    result = []
    for item in any_list:
        if type(item) is str:
            result.append(item)
    return result

list2 = check_type_str_in_list(any_list=['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'])
print(list2)

# ======================================================================================================================
# task 8
# sum_result = 0
#
# test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for number in test_list:
#     if number % 2 == 0:
#         sum_result += number
# print(f'Сума усіх парних чисел у списку дорівнює {sum_result}')
#
# Функція, яка рахує суму усіх парних чисел у списку
def sum_even_pair_numbers(list_of_numbers):
    sum_result = 0
    for number in list_of_numbers:
        if number % 2 == 0:
            sum_result += number
    return sum_result

result = sum_even_pair_numbers(list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f'Сума усіх парних чисел у списку дорівнює {result}')

# ======================================================================================================================
# task 9
# Функция, яка буде вимагати від користувача ввести слово,
# в якому є літера "h" (враховуються як великі так і маленькі).
# Функція не повинна завершитися, якщо користувач ввів слово без букви "h".

def enter_word_with_letter_h():
    while True:
        input_word = input("Введіть слово, в якому є літера 'h': ")
        if 'h' in input_word.lower():
            print("У введеному слові є літера 'h'")
            break
        else:
            print("У введеному слові немає літери 'h'. Будь ласка, введіть ще раз")

enter_word_with_letter_h()

# ======================================================================================================================
# task 10

# """
# Родина зібралася в автомобільну подорож із Харкова в Буда-
# пешт. Відстань між цими містами становить 1600 км. Відомо,
# що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
# становить 48 літрів.
# 1) Скільки літрів бензину знадобиться для такої подорожі?
# 2) Скільки щонайменше разів родині необхідно заїхати на зап-
# равку під час цієї подорожі, кожного разу заправляючи пов-
# ний бак?
# """
# all_distance = 1600
# tank_capacity = 48
# consumption = 9
#
# total_fuel =  (all_distance * consumption) / 100
# full_tank_count = int((total_fuel + tank_capacity -1) // tank_capacity)
# print(f'Для такої подорожі знадобиться {total_fuel} літрів бензину\n'
#       f'Родині необхідно заїхати на заправку щонайменше {full_tank_count} рази')

def input_distance_and_tank_capacity_and_consumption():
    while True:
        try:
            distance = float(input("Введіть відстань у км: "))
            if distance <=0:
                print("Відстань не може бути менше або дорівнювати нулю.")
                continue
            break
        except ValueError:
            print("Будь ласка, введіть ціле число для відстані.")

    while True:
        try:
            tank_capacity = float(input("Введіть обʼєм паливного баку у літрах: "))
            if tank_capacity <=0:
                print("Обʼєм баку не може бути менше або дорівнювати нулю")
                continue
            break
        except ValueError:
            print("Будь ласка, введіть ціле число для об'єму баку.")

    while True:
        try:
            consumption = float(input("Введіть споживання палива л/100км: "))
            if consumption <=0:
                print("Споживання палива не може бути менше або дорівнювати нулю.")
                continue
            break
        except ValueError:
            print("Будь ласка, введіть ціле число для споживання палива.")

    return distance, tank_capacity, consumption

def calculate_fuel_stops_and_fuel_needed():
    distance, tank_capacity, consumption = input_distance_and_tank_capacity_and_consumption()
    fuel_needed = round((distance * consumption) / 100, 2)
    fuel_stops = int((fuel_needed + tank_capacity - 1) // tank_capacity)
    return fuel_needed, fuel_stops

result_fuel_needed, result_fuel_stops = calculate_fuel_stops_and_fuel_needed()

print(f'Для такої подорожі знадобиться {result_fuel_needed} літрів бензину\n'
      f'Мені необхідно заїхати на заправку щонайменше {result_fuel_stops} рази')
