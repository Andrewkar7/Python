# Определить, является ли год, который ввел пользователь, високосным или не високосным.

# https://drive.google.com/file/d/1Z00u_jDPoGrccIfJPisHNP89vABq3kj4/view?usp=sharing

print('Введите год')
year = int(input('Год:'))

if year % 4 != 0:
    print('Год не високосный')
else:
    if year % 100 != 0:
        print('Год високосный')
    else:
        if year % 400 == 0:
            print('Год високосный')
        else:
            print('Год не високосный')
