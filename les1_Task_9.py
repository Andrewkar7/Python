# Вводятся три разных числа. Найти, какое из них является средним
# (больше одного, но меньше другого).

# https://drive.google.com/file/d/12UWSnng7Sl6GMxtPJR8jLJvv3oWo1PFo/view?usp=sharing

print('Введите три разных числа')
a = int(input('Введите число один: '))
b = int(input('Введите число два: '))
c = int(input('Введите число три: '))

if a > b:
    if a < c:
        print(f'Среднее число {a}')
    else:
        if b < c:
            print(f'Среднее число {c}')
        else:
            print(f'Среднее число {b}')
else:
    if b > c:
        if a > c:
            print(f'Среднее число {a}')
        else:
            print(f'Среднее число {c}')
    else:
        print(f'Среднее число {b}')
