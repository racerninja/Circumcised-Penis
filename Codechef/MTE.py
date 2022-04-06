for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ne = 0

    s = sum(arr)

    for x in arr:
        if x%2 == 0:
            ne+=1

    no = n - ne

    if s%2 == 0:
        print(min(no//2, ne))

    else:
        print(ne)
