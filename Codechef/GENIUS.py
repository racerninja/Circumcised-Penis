import math

for _ in range(int(input())):
    n,x = map(int, input().split())

    c = (n+x)%4
    a = (n+x-c)//4
    b = n-a-c

    if a>=0 and b>=0 and c>=0:
        print("YES")
        print(a,b,c)
    else:
        print("NO")
