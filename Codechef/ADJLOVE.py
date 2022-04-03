for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    odd_arr = []
    even_arr = []

    for x in arr:
        if x%2 == 1:
            odd_arr.append(x)

        else:
            even_arr.append(x)

    if len(even_arr) == 0 and len(odd_arr)%2 == 0:
        print(*arr)

    elif len(even_arr) == 0 and len(odd_arr)%2 == 1:
        print(-1)

    elif len(odd_arr)%2 == 0 and len(odd_arr) != 0:
        print(*(odd_arr + even_arr))

    elif len(odd_arr)%2 == 1 and len(odd_arr)>1:
        print(*([odd_arr[0]] + even_arr + odd_arr[1:]))

    else:
        print(-1)
