#functions that are covered by tests:

def count_sum(a: int|float, b: int|float):
    if (type(a) != int and type(a) != float) or (type(b) != int and type(b) != float):
        return "Увага: аргументи мають бути числами"
    return a + b


def average_value(numbers: list):
    if not all(type(k) == int or type(k) == float for k in numbers):
        return "У списку мають бути лише числа"
    return round(sum(numbers) / len(numbers), 2)


def longest_word_in_list(list_of_words):
    if not list_of_words:
        return "Список порожній"

    if not all(isinstance(word, str) for word in list_of_words):
        return "Список містить не тільки строки"

    longest_word = ""
    for word in list_of_words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


def string_back_to_front(any_string: str):
    if type(any_string) != str:
        return "Увага: аргумент мають бути рядком"
    return any_string[::-1]
