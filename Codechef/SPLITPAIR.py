for _ in range(int(input())):
    s = input()
    n = len(s)
    even = 0
    odd = 0

    for x in s[:n-1]:
        if int(x)%2 == 0:
            even += 1
        else:
            odd += 1

    if int(s[n-1])%2 == 0 and even > 0:
        print("YES")

    elif int(s[n-1])%2 == 1 and odd > 0:
        print("YES")

    else:
        print("NO")
