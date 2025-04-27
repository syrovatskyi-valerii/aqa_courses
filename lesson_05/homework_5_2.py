# Заданий список кортежів (ім'я, прізвище, вік, професія, місце проживання):
# 1) Додайте свій новий запис на початок даного списку.
# 2) У модифікованому списку обміняйте елементи з індексами 1 і 5 (1<->5). Виведіть результат.
# 3) Перевірте, чи всі люди в модифікованому списку з індексами 6, 10, 13 мають вік ≥ 30. Виведіть результат перевірки

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]
# 1) Додайте свій новий запис на початок даного списку:
people_records.insert(0, ('Valerii', 'Syrovatskyi', 34, 'Manual QA', 'Kharkiv'))

# 2) У модифікованому списку обміняйте елементи з індексами 1 і 5 (1<->5). Виведіть результат.
people_records[1], people_records[5] = people_records[5], people_records[1]
for update_people_records in people_records:
    print(update_people_records)

# 3) Перевірте, чи всі люди в модифікованому списку з індексами 6, 10, 13 мають вік ≥ 30. Виведіть результат перевірки
# Перевіряємо вік кожної людини у модифікованому списку з індексами 6, 10,13:
checking_age = 30

is_person_6_old_enough = people_records[6][2] >= checking_age
is_person_10_old_enough = people_records[10][2] >= checking_age
is_person_13_old_enough = people_records[13][2] >= checking_age

print(is_person_6_old_enough, is_person_10_old_enough, is_person_13_old_enough)

result = is_person_6_old_enough and is_person_10_old_enough and is_person_13_old_enough
if result is True:
  print(f'Всі люди в модифікованому списку з індексами 6, 10, 13 мають вік ≥ 30')
else:
  print(f'Не всі люди в модифікованому списку з індексами 6, 10, 13 мають вік ≥ 30')

# ------------------------------------------------------------------------------------------
# До такого рішення я б не дійшов самостійно:
result = all(people_records[i][2] >= 30 for i in [6, 10, 13])
if result is True:
  print(f'Всі люди в модифікованому списку з індексами 6, 10, 13 мають вік ≥ 30')
else:
  print(f'Не всі люди в модифікованому списку з індексами 6, 10, 13 мають вік ≥ 30')