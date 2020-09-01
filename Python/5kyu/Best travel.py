# https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/train/python
import itertools

xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]


def choose_best_sum(t, k, ls):
    diff = float('inf')
    for x in itertools.combinations(ls, k):
        s = sum(x)
        if s == t: return t
        if t - s < diff and s < t:
            diff = abs(s - t)
    return t - diff if t - diff > 0 else None


print(choose_best_sum(163, 3, [50]))
# your code
