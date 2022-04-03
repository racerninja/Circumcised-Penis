for _ in range(int(input())):
    a,b = map(int, input().split())
    c = 21-a-b

    if c>10 or c<1:
        print(-1)
    else:
        print(c)
