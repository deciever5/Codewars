import math
import numpy as np


def primes_in_list(x):
    n = max(x, key=abs)
    primes = np.arange(3, n + 1, 2)
    isprime = np.ones((n - 1) // 2, dtype=bool)
    for factor in primes[:int(math.sqrt(n)) // 2]:
        if isprime[(factor - 2) // 2]:
            isprime[(factor * 3 - 2) // 2::factor] = 0
    return np.insert(primes[isprime], 0, 2)


def sum_for_list(numbers):
    result = []
    y = np.array(lst)

    for i in primes_in_list(numbers):
        z = np.sum(y[y % i == 0])
        if z != 0: result.append([i, abs(z)])
    print(result)
    return result


"""def profiling(lst_to_time, max_num):
    import cProfile
    import pstats

    with cProfile.Profile() as pr:
        sum_of_numbers(lst_to_time, max_num)

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()
    stats.dump_stats(filename="obliczenia.prof")"""

"""def sum_for_list(lst):
    max_in_lst = max(lst, key=abs)
    sum_of_numbers(lst, max_in_lst)"""

# lst = [x for x in range(100001)]

lst = [15, 21, 24, 30, 45, 150, 121341]
sum_for_list(lst)
# profiling(lst, max_in_lst)
