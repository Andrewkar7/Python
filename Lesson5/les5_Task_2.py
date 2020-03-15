# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],

from collections import deque

a = deque('0123456789ABCDEF')
b = deque(input('Введите первое число: '))
c = deque(input('Введите второе число: '))
d = deque()
b.reverse()
c.reverse()
if len(b) > len(c):
    b, c = c, b
j = 0
k = 0
for i in b:
    one = a.index(i)
    two = a.index(c[j])
    summa = one + two + k
    k = 0
    if summa <= len(a) - 1:
        d.append(a[summa])
        k = 0
    else:
        k += 1
        d.append(a[summa - 16])
    j += 1
if len(c) > len(b):
    n = len(c)
    m = (n - len(b))
    while m < n:
        c.popleft()
        m += 1
    j = 0
    for char in c:
        three = a.index(c[j])
        sum = three + k
        d.append(a[sum])
        k = 0

if k == 1:
    d.append(1)

d.reverse()
print(d)
