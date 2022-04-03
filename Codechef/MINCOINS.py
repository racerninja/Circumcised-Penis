for _ in range(int(input())):
    n = int(input())

    if n%5 != 0:
        print(-1)

    elif n%10 == 0:
        print(n//10)

    else:
        print((n//10) + 1)
