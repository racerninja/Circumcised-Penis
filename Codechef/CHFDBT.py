import math

for _ in range(int(input())):
    n = int(input())
    if n%2 == 0:
        c = max(1,round(n/2))
    else:
        c = max(1,round((n+1)/2))
    print(c)
