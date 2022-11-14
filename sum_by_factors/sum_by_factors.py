import cProfile
import math
import numpy as np
from numpy import int64


def primes_in_list(x):
    n = abs(max(x, key=abs))
    primes = np.arange(3, n + 1, 2)
    isprime = np.ones((n - 1) // 2, dtype=bool)
    for factor in primes[:int(math.sqrt(n)) // 2]:
        if isprime[(factor - 2) // 2]:
            isprime[(factor * 3 - 2) // 2::factor] = 0
    return np.insert(primes[isprime], 0, 2)



def sum_for_list(numbers):
    result = []
    all_nums = np.array(numbers)
    max_num = max(map(abs, all_nums))
    primes = primes_in_list(all_nums)
    for i in primes:
        if i > (max_num / 2):
            break
        x = all_nums[all_nums % i == 0]

        if len(x) > 0:
            z = np.sum(x, dtype=int64)
            np.append(result,[i, z])

    for number in numbers:
        if abs(number) > (max_num / 2) and abs(number) in primes:
            if abs(number) in numbers:
                np.append(result, [number, number])
            else:
                np.append(result, [abs(number), number])
    # print(numbers)
    # print(sorted(result,key=lambda x: x[0]))

    return sorted(result, key=lambda b: b[0])


def profiling(lst_to_time):
    import pstats

    with cProfile.Profile() as pr:
        sum_for_list(lst_to_time)

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()
    stats.dump_stats(filename="obliczenia.prof")


# lst = [x for x in range(100001)]
lst = [885279, -677420, -938953, -317790, -484868, 956059, -153723, -951027, -557033, -906309, 6456661]
profiling(lst)
# sum_for_list(lst)
