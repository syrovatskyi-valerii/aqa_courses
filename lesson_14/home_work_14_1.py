# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.

class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def update_average_grade(self, new_grade):
        self.average_grade = new_grade

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}, Age: {self.age}, Average Grade: {self.average_grade}"

student1 = Student("Valerii", "Syrovatskyi", 35, 4)
print(student1)

student1.update_average_grade(5)
print(f'After updating the average grade -> {student1}')
