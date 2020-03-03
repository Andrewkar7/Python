# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random

SIZE = 10
MIN_ITEM = -120
MAX_ITEM = 120
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_neg = MIN_ITEM - 1
for i in array:
    while i < 0 and i > max_neg:
        max_neg = i
if max_neg == MIN_ITEM - 1:
    print('В массиве нет отрицательных чисел')
else:
    print(f'Максимальный отрицательный элемент {max_neg} на позиции {array.index(max_neg) + 1}')
