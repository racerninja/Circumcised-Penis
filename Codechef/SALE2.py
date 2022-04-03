for _ in range(int(input())):
    n,x = map(int, input().split())

    l = n//1.5
    r = n - int(l*(1.5))


    print(int((l+r)*x))
