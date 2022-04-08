import collections

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    x = 1
    c = collections.Counter(arr)
    x = max(c.values())
    ops = 0

    while n > x:
        r = x
        for _ in range(r):
            if n>x:
                x+=1
                ops+=1
        ops+=1
    print(ops)
