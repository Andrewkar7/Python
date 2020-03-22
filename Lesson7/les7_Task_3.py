import random

m = 5
SIZE = 2 * m + 1
MIN_ITEM = 0
MAX_ITEM = 49
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
half = int(SIZE / 2)
print(array)


# метод сортировки расческой
def comb_sort(arr):
    alen = len(arr)
    gap = (alen * 10 // 13) if alen > 1 else 0
    while gap:
        if 8 < gap < 11:
            gap = 11
        swapped = False
        for i in range(alen - gap):
            if arr[i + gap] < arr[i]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
        gap = (gap * 10 // 13) or swapped


comb_sort(array)
print(array)
print(f'Медианой данного массива является число {array[half]}')
