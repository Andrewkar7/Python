# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# x86_64 GNU/Linux
# Python 3.8.0 x64

import random
import sys

# 1 вариант
SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 120
array = [random.randint(MIN_ITEM, MAX_ITEM) for j in range(SIZE)]

#print(array)
size_of_array = sys.getsizeof(SIZE) + sys.getsizeof(MIN_ITEM) + sys.getsizeof(MAX_ITEM) + sys.getsizeof(array)
# сделал getsizeof в середине программы потому что массив дальше пойдет один и тот же для всех вариантов

max_1 = 0
min_1 = 0
for i in range(SIZE):
    if array[i] > array[max_1]:
        max_1 = i
    elif array[i] < array[min_1]:
        min_1 = i

array[max_1], array[min_1] = array[min_1], array[max_1]

#print(array)

size_all_1 = size_of_array + sys.getsizeof(max_1) + sys.getsizeof(min_1) + sys.getsizeof(i)
print(f'Под переменные в 1 варианте было выделено {size_all_1} байт памяти')

# 2 вариант

max_2 = max(array)
min_2 = min(array)
i_min = array.index(min_2)
i_max = array.index(max_2)
array[i_max], array[i_min] = array[i_min], array[i_max]

#print(array)
size_all_2 = size_of_array + sys.getsizeof(max_2) + sys.getsizeof(min_2) + sys.getsizeof(i_min) + sys.getsizeof(i_max)
print(f'Под переменные во 2 варианте было выделено {size_all_2} байт памяти')

# 3 вариант

max_3 = 0
min_3 = 0
for i in array:
    if i > max_3:
        max_3 = i
min_3 = max_3
for j in array:
    if j < min_3:
        min_3 = j
for id, item in enumerate(array):
    if item == min_3:
        array[id] = max_3
    elif item == max_3:
        array[id] = min_3

#print(array)
size_all_3 = size_of_array + sys.getsizeof(max_3) + sys.getsizeof(min_3) + sys.getsizeof(i) + sys.getsizeof(
    j) + sys.getsizeof(id) + sys.getsizeof(item)
print(f'Под переменные в 3 варианте было выделено {size_all_3} байт памяти')


# Под переменные в 1 варианте было выделено 348 байт памяти
# Под переменные во 2 варианте было выделено 376 байт памяти
# Под переменные в 3 варианте было выделено 432 байт памяти

# Общий вывод: задача в целом не очень сложная, но даже на ее примере можно увидеть как изменяется выделенная память
# в трех различных вариантах. Чем больше переменных, тем больше выделяется памяти. Однако это ничего не говорит о скорости
# выполнения программы. Чтобы найти оптимальное решение, нужно смотреть отдельно и на скорость и на количество выделяемой памяти.