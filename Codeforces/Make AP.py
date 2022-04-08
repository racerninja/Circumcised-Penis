for _ in range(int(input())):
    a,b,c = map(int, input().split())
    d = (2*b)-(a+c)

    if d<0:
        if (a+c)%(2*b) == 0:
            print("YES")
        else:
            print("NO")

    else:
        if d%a == 0 or d%c == 0:
            print("YES")
        else:
            print("NO")
