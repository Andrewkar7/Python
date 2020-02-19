# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, надо вывести 6843.

# https://drive.google.com/file/d/1fRW5BjI7jJqRVmxHhMi0nLt73qEYgr2C/view?usp=sharing

a = int(input("Введите натуральное число: "))
b = 0
while a > 0:
    b = b * 10 + a % 10
    a = a // 10
print(b)
