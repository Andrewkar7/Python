# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

# https://drive.google.com/file/d/1loPhz88nR_d1Q1OtaaP3VXI8-jGSKMzW/view?usp=sharing

print('Введите номер буквы в алфавите')
m = int(input('Номер: '))
m = ord('a') + m - 1
n = chr(m)
print('Буква ' + n)
