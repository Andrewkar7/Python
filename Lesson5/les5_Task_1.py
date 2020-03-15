#Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

Company = namedtuple('Company', 'name profit_1 profit_2 profit_3 profit_4')

n = int(input('Введите количество предприятий: '))
a = []
companies = {}
for i in range(n):
    name = input(f"Введите название {i + 1} предприятия: ")
    profit_1 = int(input('Введите прибыль за первый квартал: '))
    profit_2 = int(input('Введите прибыль за второй квартал: '))
    profit_3 = int(input('Введите прибыль за третий квартал: '))
    profit_4 = int(input('Введите прибыль за четвертый квартал: '))
    Company_d = Company(name, profit_1, profit_2, profit_3, profit_4)
    companies[Company_d.name] = ((profit_1 + profit_2 + profit_3 + profit_4) / 4)
print(companies)

b = []
for name, profit in companies.items():
    b.append(profit)
mid_profit = sum(b) / len(b)
print(f'Средняя прибыль за год среди всех предприятий равна {mid_profit}')

c = []
d = []
for name, profit in companies.items():
    if profit >= mid_profit:
        c.append(name)
    else:
        d.append(name)
c = ' '.join(c)
d = ' '.join(d)
print(f'У предприятия(й) {c} прибыль за год выше среднего ')
print(f'У предприятия(й) {d} прибыль за год ниже среднего ')
