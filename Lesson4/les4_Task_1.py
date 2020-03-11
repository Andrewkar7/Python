# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
import cProfile
import timeit


# 1 вариант(рекурсия)
def rec(a, n):
    if n == 1:
        return a
    else:
        return a + rec(a / (-2), n - 1)


print(timeit.timeit('rec(1, 10)', number=100000, globals=globals()))   # 0.1906347639996966
print(timeit.timeit('rec(1, 40)', number=100000, globals=globals()))   # 0.7189438770001289
print(timeit.timeit('rec(1, 160)', number=100000, globals=globals()))  # 2.847344845000407
print(timeit.timeit('rec(1, 640)', number=100000, globals=globals()))  # 12.845694362998984

cProfile.run('rec(1, 10)')   #  10/1    0.000    0.000    0.000    0.000 les4_Task_1.py:7(rec)
cProfile.run('rec(1, 40)')   #  40/1    0.000    0.000    0.000    0.000 les4_Task_1.py:7(rec)
cProfile.run('rec(1, 160)')  # 160/1    0.000    0.000    0.000    0.000 les4_Task_1.py:7(rec)
cProfile.run('rec(1, 640)')  # 640/1    0.001    0.000    0.001    0.001 les4_Task_1.py:7(rec)


# 2 вариант(с помощью цикла)
def recc(n):
    x = 1
    summa = 0
    for i in range(n):
        summa += x
        x /= -2
    return (summa)


print(timeit.timeit('recc(10)', number=100000, globals=globals()))   # 0.13501678299871855
print(timeit.timeit('recc(40)', number=100000, globals=globals()))   # 0.3526212469987513
print(timeit.timeit('recc(160)', number=100000, globals=globals()))  # 1.2323066699991614
print(timeit.timeit('recc(640)', number=100000, globals=globals()))  # 4.970536546999938

cProfile.run('recc(10)')   # 1    0.000    0.000    0.000    0.000 les4_Task_1.py:26(recc)
cProfile.run('recc(40)')   # 1    0.000    0.000    0.000    0.000 les4_Task_1.py:26(recc)
cProfile.run('recc(160)')  # 1    0.000    0.000    0.000    0.000 les4_Task_1.py:26(recc)
cProfile.run('recc(640)')  # 1    0.000    0.000    0.000    0.000 les4_Task_1.py:26(recc)


# 3 вариант(с помощью геометрической прогрессии)
def reccc(n):
    _summa = (1 - (-0.5) ** n) / (1.5)
    return (_summa)


print(timeit.timeit('reccc(10)', number=100000, globals=globals()))   # 0.02524184599860746
print(timeit.timeit('reccc(40)', number=100000, globals=globals()))   # 0.02559272700091242
print(timeit.timeit('reccc(160)', number=100000, globals=globals()))  # 0.025965396000174223
print(timeit.timeit('reccc(640)', number=100000, globals=globals()))  # 0.03160691300035978

cProfile.run('reccc(10)')   # 1    0.000    0.000    0.000    0.000 les4_Task_1.py:47(reccc)
cProfile.run('reccc(40)')   # 1    0.000    0.000    0.000    0.000 les4_Task_1.py:47(reccc)
cProfile.run('reccc(160)')  # 1    0.000    0.000    0.000    0.000 les4_Task_1.py:47(reccc)
cProfile.run('reccc(640)')  # 1    0.000    0.000    0.000    0.000 les4_Task_1.py:47(reccc)


# Общий вывод:
# 1. Можно увидеть, что скорость третьего варианта самая быстрая и не меняется в зависимости от увеличения
# входных данных (константный порядок роста), так как у нас всего 1 формула c одной переменной.
# 2. Второй и первый варианты имеют линейную сложность (увеличение времени прямо зависит от увеличения N).
# Метод с рекурсией является самым сложным и медленным, функция вызываеся столько раз, какое число N мы задаем.