# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

MIN_ITEM_1 = 2
MAX_ITEM_1 = 100
MIN_ITEM_2 = 2
MAX_ITEM_2 = 10
array_1 = list(range(MIN_ITEM_1, MAX_ITEM_1))
array_2 = list(range(MIN_ITEM_2, MAX_ITEM_2))

for j in array_2:
    count = []
    for i in array_1:
        if i % j == 0:
            count.append(i)
    print(f'Числу {j} кратны {len(count)} чисел')
