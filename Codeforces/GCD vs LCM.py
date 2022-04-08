for _ in range(int(input())):
    n = int(input())

    if n == 4:
        a = b = c = d = 1

    elif n == 5:
        a = c = d = 1
        b = 2

    elif n == 6:
        a = c = d = 1
        b = 3

    elif n%4 == 0:
        c = d = b = 2
        a = n-6

    elif n%4 == 1:
        d = 1
        c = 2
        a = 2
        b = n-5

    elif n%4 == 2:
        d = 1
        c = 1
        a = (n-2)//2 - 1
        b = (n-2)//2 + 1

    else:
        d = 1
        c = 2
        b = 2
        a = n-5

    print(a, b, c, d)
