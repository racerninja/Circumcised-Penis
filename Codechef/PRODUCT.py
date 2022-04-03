import math

for _ in range(int(input())):
    b,c = map(int, input().split())
    print(c//math.gcd(b,c))
