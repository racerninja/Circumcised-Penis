for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    curr = arr[0]
    ans = 0

    for i in range(1,n-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            if i+1 != n-1:
                arr[i+1] = max(arr[i+2], arr[i])
            else:
                arr[i+1] = arr[i]
            ans += 1

    print(ans)
    print(*arr)
