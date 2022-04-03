from collections import *

for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    f = Counter(arr)
    for y in arr:
        m = min(f[y], f[x*y])
        f[y] -= m
        f[y*x] -= m
    print(sum(f.values()))
