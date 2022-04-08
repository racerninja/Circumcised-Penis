for _ in range(int(input())):
    n,m,r,c = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(input().split()))
    count = 0
    ans = 5

    if arr[r-1][0][c-1] == "B":
        ans = 0

    else:
        for i in range(n):
            if "B" not in arr[i][0]:
                count += 1

        if count == n:
            ans = -1

        for i in range(n):
            if arr[i][0][c-1] == "B":
                ans = 1

        if "B" in arr[r-1][0]:
            ans = 1

        if ans == 5:
            ans = 2

    print(ans)
 
