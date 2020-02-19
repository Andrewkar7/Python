#  В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
#  После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
#  Если за 10 попыток число не отгадано, вывести правильный ответ.

# https://drive.google.com/file/d/1fRW5BjI7jJqRVmxHhMi0nLt73qEYgr2C/view?usp=sharing

import random

number = random.randint(1, 100)
user_number = None
count = 0
max_count = 10

while number != user_number:
    count += 1
    if count > max_count:
        print('Вы проиграли. Загаданное число: ', number)
        break
    user_number = int(input('Введите число: '))
    if number < user_number:
        print('Ваше число больше загаданного')
    elif number > user_number:
        print('Ваше число меньше загаданного')
else:
    print('Вы выиграли!')
