# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 120
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max = 0
min = 0
for i in range(SIZE):
    if array[i] > array[max]:
        max = i
    elif array[i] < array[min]:
        min = i

print(f'Максимум {array[max]} с индексом {max}')
print(f'Минимум {array[min]} с индексом {min}')

array[max], array[min] = array[min], array[max]

print(array)
