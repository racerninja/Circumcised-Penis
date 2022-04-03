import math

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    count = 0

    for i in range(n):
        if arr[i]<=k:
            k -= arr[i]
            count += 1

        elif math.ceil(arr[i]/2) <= k:
            count += 1
            break

        elif i < n - 1:
            if math.ceil(arr[i + 1] / 2) <= k:
                count += 1
                break

        else:
            break

    print(count)
