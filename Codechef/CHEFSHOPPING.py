for _ in range(int(input())):
    n = int(input())

    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    ans = 0

    for i in range(n-1):
        ans += min(l[i+1], r[i])

    print(ans)
