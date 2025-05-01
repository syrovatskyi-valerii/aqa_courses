# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

def count_unique_characters_in_str():
    input_str = input("Введіть довільний рядок: ")
    set_unique_characters = set(input_str)
    count = len(set_unique_characters)

    if count > 10:
        print(True)
    else:
        print(False)

count_unique_characters_in_str()
