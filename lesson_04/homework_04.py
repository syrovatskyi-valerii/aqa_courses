adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

# task 02 ==
""" Замініть .... на пробіл
"""
# Рішення:
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
# Рішення:
adwentures_of_tom_sawer = ' '.join(adwentures_of_tom_sawer.split())
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
# Рішення:
print(adwentures_of_tom_sawer.count('h'))

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
# Рішення:
import re
total_count_upper_letter = len(re.findall(r'\b[A-Z]', adwentures_of_tom_sawer))
print(total_count_upper_letter)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
# Рішення:
searching_word = 'Tom'
meats_second_time = 1
all_words_list = adwentures_of_tom_sawer.split()
first_index = all_words_list.index(searching_word)
second_index = all_words_list.index(searching_word, first_index + meats_second_time)
print(f'Слово Tom зустрічається вдруге на {second_index} позиції')

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
# Рішення:
adwentures_of_tom_sawer_sentences = (adwentures_of_tom_sawer.split('. '))
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
# Рішення:
print(adwentures_of_tom_sawer_sentences[3].lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
# Рішення:
searching_phrase = 'By the time'
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.strip().startswith(searching_phrase):
        print(f'Це речення починається на фразу "{searching_phrase}')
    else:
        print(f'Це речення не починається на фразу {searching_phrase}')

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
# Рішення:
last_sentence = adwentures_of_tom_sawer_sentences[-1]
words_count_in_last_sentence = len(last_sentence.split())
print(f'В останньому реченні {words_count_in_last_sentence} слова')
