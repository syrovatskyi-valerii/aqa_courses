'''Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
'''


from abc import ABC, abstractmethod
import math
from lesson_16.validate_value import validate_correct_value, validate_correct_triangle_sides

class Figure(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class Square(Figure):
    def __init__(self, side_a: float):
        validate_correct_value(side_a, 'Сторона у квадрата')
        self.__side_a = side_a

    def area(self) -> float:
        return self.__side_a ** 2

    def perimeter(self) -> float:
        return self.__side_a * 4

    def __str__(self) -> str:
        return "Квадрат"


class Rectangle(Figure):
    def __init__(self, side_a: float, side_b: float):
        validate_correct_value(side_a, 'Сторона A прямокутника')
        validate_correct_value(side_b, 'Сторона B прямокутника')
        self.__side_a = side_a
        self.__side_b = side_b

    def area(self) -> float:
        return self.__side_a * self.__side_b

    def perimeter(self) -> float:
        return 2 * (self.__side_a + self.__side_b)

    def __str__(self) -> str:
        return "Прямокутник"


class Circle(Figure):
    def __init__(self, radius: float):
        validate_correct_value(radius, 'Радіус кола')
        self.__radius = radius

    def area(self) -> float:
        return math.pi * self.__radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.__radius

    def __str__(self) -> str:
        return "Коло"


class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        validate_correct_value(a, "Сторона A трикутника")
        validate_correct_value(b, "Сторона B трикутника")
        validate_correct_value(c, "Сторона C трикутника")
        validate_correct_triangle_sides(a,b,c)
        self.__a = a
        self.__b = b
        self.__c = c

    def area(self) -> float:
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))

    def perimeter(self) -> float:
        return self.__a + self.__b + self.__c

    def __str__(self) -> str:
        return "Трикутник"


figures = [
    Square(side_a=2),
    Rectangle(side_a=4, side_b=5),
    Circle(radius=3),
    Triangle(a=4, b=5, c=6)
]

for figure in figures:
    print(f'{str(figure)} —> площа: {figure.area():.2f}, периметр: {figure.perimeter():.2f}')
