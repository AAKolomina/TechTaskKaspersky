#так как в задании точно не сказано, то будем считать, что на вход подаются натуральные двузначные числа
#данный алгоритм не моя идея, но он был в курсе алгоритмов и структур данных
#разработан Хоаром и работает в среднем за О(n)
import random

def quickselect_median(a, p=random.choice):
    if len(a) % 2 == 1: return quickselect(a, len(a) / 2, p)
    else: return 0.5 * (quickselect(a, len(a) / 2 - 1, p) + quickselect(a, len(a) / 2, p))


def quickselect(a, k, p):
    if len(a) == 1:
        assert k == 0
        return a[0]
    piv = p(a)
    lows = [x for x in a if x < piv]
    highs = [x for x in a if x > piv]
    pivots = [x for x in a if x == piv]

    if k < len(lows): return quickselect(lows, k, p)
    elif k < len(lows) + len(pivots): return pivots[0]
    else: return quickselect(highs, k - len(lows) - len(pivots), p)

a = [random.randint(10,100) for x in range(100)]
print(*a)
print(round(quickselect_median(a)))