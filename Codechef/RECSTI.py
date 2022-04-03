for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    pair = 0
    ans = []

    for i in range(n):
        try:
            ans.remove(arr[i])
            pair += 1

        except ValueError:
            ans.append(arr[i])

    if (pair + len(ans)) % 2 == 0:
        print(len(ans))

    else:
        print(len(ans) + 2)
