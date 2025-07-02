# 1. Реалізуйте ітератор для зворотного виведення елементів списку.

class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.data[self.index]
        self.index -= 1
        return value


test_list = [1, True, 'a', {"user_id": 666}, (1, "string"), [1, 2, None, 4]]
for i in ReverseIterator(test_list):
    print(i)



# 2. Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

class PairNumberIterator:
    def __init__(self, N):
        if not isinstance(N, int) or isinstance(N, bool):
            raise ValueError("N має бути цілим числом")
        self.N = N
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.N:
            raise StopIteration
        result = self.current
        self.current += 2
        return result


for number in PairNumberIterator(10):
    print(number)