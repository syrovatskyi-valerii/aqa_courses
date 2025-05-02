# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

sum_result = 0

test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in test_list:
    if number % 2 == 0:
        sum_result += number
print(f'Сума усіх парних чисел у списку дорівнює {sum_result}')

# або
# sum_result = sum([k for k in test_list if k %2 ==0 ])
