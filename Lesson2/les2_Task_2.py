# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# https://drive.google.com/file/d/1fRW5BjI7jJqRVmxHhMi0nLt73qEYgr2C/view?usp=sharing

chet = 0
nechet = 0
n = int(input('Введите число: '))
while n > 0:
    if n % 2 == 0:
        chet += 1
    else:
        nechet += 1
    n = n // 10
print(f'У данного числа {chet} четные цифры и {nechet} нечетные цифры')
