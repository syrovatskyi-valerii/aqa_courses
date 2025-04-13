# task 01 == Виправте синтаксичні помилки
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# # task 04 == Зробіть так, щоб кількість бананів була
# # завжди в чотири рази більша, ніж яблук

apples = 2
banana = apples * 4
print("Кількість бананів становить", banana, "шт., що в 4 рази більша ніж явблук, яких -", apples, "шт.")

# task 05 == виправте назви змінних

# більш інтуітивно зрозуміліше було б назвати змінні однаково, а порядковість позначити як "_1", "_2", "_3", "_4"
side_1 = 1   # хоча можна було просто прибрати "1" та залишити "_storona"
side_2 = 2
side_3 = 3
side_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = side_1 + side_2 + side_3 + side_4
print("Периметр фігури з task 05 дорівнює", perimetery)

"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apples = 4                                      # Яблунь було 4
pears = apples + 5                              # Груш на 5 більше яблунь
plums = apples - 2                              # Слив на 2 менше яблунь
total_amount_trees = apples + pears + plums     # Підрахуємо загальну кількість дерев
print("Всього в саду посадили", total_amount_trees, "дерев.", "З яких", "яблунь ->", apples, ", груш ->", pears, "та сливи ->", plums)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
# Перший варіант:
temp_before_lunch = 5
temp_after_lunch = 5 - 10
temp_evening = temp_after_lunch + 4
print("Температура надвечір становила", temp_evening, "градус")

# Другий варіант:
temp = 5
temp -= 10
temp += 4
print("Температура надвечір становила", temp, "градус")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""

"""
Рішення № 1. 
Якщо рахувати, що 1 хлопчик, який захворів - все ж присутній, бо не зазначено, що він не прийшов.
І у такому випадку відсутні тільки 2 дівчинки.
"""
boys = 24
girls = int(boys / 2)
girls_absent = 2
total_amount_children = boys + girls
today_present_children = total_amount_children - girls_absent
print("Cьогодні у театральному гуртку", today_present_children, "дитини")

"""
Рішення № 2. 
Якщо рахувати, що 1 хлопчик, який захворів - все ж НЕ прийшов, бо захворів.
І у такому випадку відсутні 1 хлопчик та 2 дівчинки.
PS: у другому варіанті замінив "int" на "//" щоб прибрати float у підрахунку.
"""
boys = 24
girls = boys // 2
girls_absent = 2
boys_absent = 1
total_amount_children = boys + girls
today_present_children = total_amount_children - girls_absent - boys_absent
print("Cьогодні у театральному гуртку", today_present_children, "дитини")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""

# Перший варіант рішення:

first_book_price = 8
second_book_price = first_book_price + 2
third_book_price = int(first_book_price + second_book_price) / 2
total_books_price = int(first_book_price + second_book_price + third_book_price)
print("Усі книги будуть коштувати", total_books_price, "грн.")

# Другий варіант рішення:

first_book_price = 8
second_book_price = first_book_price + 2
third_book_price = (first_book_price + second_book_price) / 2
total_books_price = (first_book_price + second_book_price + third_book_price)
print(f"Усі книги будуть коштувати: {total_books_price:.2f} грн.")
