for _ in range(int(input())):
    n = input()
    sum = 0
    sum2 = 0

    for i in range(len(n)):
        sum += int(n[i])

    n = str(int(n) + 1)
    for i in range(len(n)):
        sum2 += int(n[i])

    if (sum + sum2)%2 == 1:
        print(int(n))

    else:
        print(int(n) + 1)
