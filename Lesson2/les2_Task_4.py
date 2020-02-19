# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

# https://drive.google.com/file/d/1fRW5BjI7jJqRVmxHhMi0nLt73qEYgr2C/view?usp=sharing

def rec(a, n):
    if n == 1:
        return a
    else:
        return a + rec(a / (-2), n - 1)


print(rec(1, int(input('Введите число элементов: '))))
