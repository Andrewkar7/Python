# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# https://drive.google.com/file/d/10JUYUVw0wq19Th2MsWyVBQlVNnHb_P60/view?usp=sharing

print('Введите трехзначное число')
x = int(input('Число: '))
x1= x//100
x2=x%100//10
x3=x%10
print(f'Сумма цифр числа: {x1+x2+x3}')
print(f'Произведение цифр числа: {x1*x2*x3}')