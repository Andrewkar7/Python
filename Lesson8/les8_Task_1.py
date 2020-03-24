# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком. Пример работы функции: func("papa") --> 6; func("sova") --> 9
import hashlib


def substring_sum(str):
    len_str = len(str)
    h_sum_sub = set()

    for i in range(len_str):
        for j in range(i + 1, len_str + 1):
            h_sub = hashlib.sha1(str[i:j].encode('utf-8')).hexdigest()
            if str[i:j] == ' ':  # Берем идеального пользователя который не ставит больше одного пробела)
                continue
            else:
                h_sum_sub.add(h_sub)
    return len(h_sum_sub) - 1


print(substring_sum('sova'))
