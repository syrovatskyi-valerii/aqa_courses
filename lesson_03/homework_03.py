alice_in_wonderland = (
'"Would you tell me, please, which way I ought to go from here?"\n'
'"That depends a good deal on where you want to get to," said the Cat.\n'
'"I don\'t much care where ——" said Alice.\n'
'"Then it doesn\'t matter which way you go," said the Cat.\n'
'"—— so long as I get somewhere," Alice added as an explanation.\n'
'"Oh, you\'re sure to do that, "said the Cat, "if you only walk long enough."'
)
print(alice_in_wonderland)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
seas = {
    'black_sea': 436_402,
    'azov_sea': 37_800
}
total_square = seas['black_sea'] + seas['azov_sea']
print(f'Загальна площа Чорного та Азовського моря становить {total_square} км2')



# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
# Вводні дані
total_count_product = 375_291
sum_first_and_second_storage = 250_449
sum_second_and_third_storage = 222_950

# Розрахунок
third_storage_count = total_count_product - sum_first_and_second_storage
first_storage_count = total_count_product - sum_second_and_third_storage
second_storage_count = total_count_product - (first_storage_count + third_storage_count)
check_sum = first_storage_count + second_storage_count + third_storage_count
print(f'на першому складі {first_storage_count} товарів\n'
      f'на другому складі {second_storage_count} товарів\n'
      f'на третьому складі {third_storage_count} товарів')

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

credit_time = int(12 * 1.5)
payment_on_month = 1179
comp_price = payment_on_month * credit_time
print(f'Вартість комп\ʼютера складає {comp_price} UAH')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
dict_numbers = {
    8019: 8,
    9907: 9,
    2789: 5,
    7248: 6,
    7128: 5,
    19224: 9
}
for number, divisor in dict_numbers.items():
    print(f'Якщо {number} поділити на {divisor}, то залишок від ділення буде => {number % divisor}')

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

order_list = {
      'big_pizza': {'count':4,'price': 274},
      'middle_pizza': {'count':2,'price': 218},
      'juice': {'count':4,'price': 35},
      'cake': {'count':1,'price': 350},
      'water': {'count':3,'price': 21}
}
total_bill = 0
for dish, data in order_list.items():
    price_for_each_type_dish = data['count'] * data['price']
    total_bill += price_for_each_type_dish
print(f'Для даного замовлення знадобиться {total_bill} UAH')


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

all_photos = 232
limit_photo_on_page = 8

#Це буде більш універсальне рішення, якщо кількість фото змінюється та при цьому треба округлювати в більшу сторону
pages_for_all_photos = (all_photos + limit_photo_on_page - 1) // limit_photo_on_page
print(f'Ігорю знадобиться {pages_for_all_photos} сторінок')

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
all_distance = 1600
tank_capacity = 48
consumption = 9

total_fuel =  (all_distance * consumption) / 100
full_tank_count = int((total_fuel + tank_capacity -1) // tank_capacity)
print(f'Для такої подорожі знадобиться {total_fuel} літрів бензину\n'
      f'Родині необхідно заїхати на заправку щонайменше {full_tank_count} рази')
