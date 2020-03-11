import timeit
import cProfile

# 1 вариант (Решето Эратосфена)

def sieve_d(n):
    sieve = [i for i in range(15 * n)]
    sieve[1] = 0

    for i in range(2, 15 * n):
        if sieve[i] != 0:
            j = i + i
            while j < 15 * n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    return res[n - 1]


print(timeit.timeit('sieve_d(100)', number=100, globals=globals()))   # 0.04124298899978385
print(timeit.timeit('sieve_d(500)', number=100, globals=globals()))   # 0.18173268800001097
print(timeit.timeit('sieve_d(2500)', number=100, globals=globals()))  # 0.9467563270000028
print(timeit.timeit('sieve_d(10000)', number=100, globals=globals())) # 4.1846134970001

cProfile.run('sieve_d(100)')   # 1    0.000    0.000    0.000    0.000 les4_Task_2.py:5(sieve_d)
cProfile.run('sieve_d(500)')   # 1    0.002    0.002    0.002    0.002 les4_Task_2.py:5(sieve_d)
cProfile.run('sieve_d(2500)')  # 1    0.008    0.008    0.010    0.010 les4_Task_2.py:5(sieve_d)
cProfile.run('sieve_d(10000)') # 1    0.034    0.034    0.041    0.041 les4_Task_2.py:7(sieve_d)

# 2 вариант

def prime_d(n):
    prime = []
    for i in range(2, 15 * n):
        for j in range(2, i):
            if ((i % j) == 0):
                break
        else:
            prime.append(i)
    return prime[n - 1]


print(timeit.timeit('prime_d(100)', number=10, globals=globals()))     # 0.07541833899995254
print(timeit.timeit('prime_d(500)', number=10, globals=globals()))     # 1.4829019210001206
#print(timeit.timeit('prime_d(2500)', number=10, globals=globals()))    # 41.53983360100028
#print(timeit.timeit('prime_d(10000)', number=10, globals=globals()))   # Не дождался)

cProfile.run('prime_d(100)')    # 1    0.009    0.009    0.009    0.009 les4_Task_2.py:34(prime_d)
cProfile.run('prime_d(500)')    # 1    0.197    0.197    0.197    0.197 les4_Task_2.py:34(prime_d)
cProfile.run('prime_d(2500)')   # 1    4.383    4.383    4.384    4.384 les4_Task_2.py:34(prime_d)
cProfile.run('prime_d(10000)')  # 1   62.729   62.729   62.731   62.731 les4_Task_2.py:34(prime_d)



# Сделал через фиксированный размер решета. Не знаю правильно ли это, но то что первый вариант просто в разы быстрее
# можно увидеть невооруженным глазом.