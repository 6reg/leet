def two_sum(lst, target):
    hm = {}
    for i, v in enumerate(lst):
        diff = target - v
        if diff in hm:
            return [hm[diff], i]
        hm[v] = i

print(two_sum([0, 1, 2], 3))
