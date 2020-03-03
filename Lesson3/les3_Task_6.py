# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

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

if max > min:
    array_2 = array[min + 1:max]
else:
    array_2 = array[max + 1:min]
print(array_2)

sum = 0
for i in array_2:
    sum += i
if sum == 0:
    print('Между минимальным и максимальным элементами нет других элементов')
else:
    print(f'Сумма элементов между минимальным и максимальным элементами равна {sum}')
