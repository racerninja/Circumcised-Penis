for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
 
    m = max(arr)
 
    if n == 1:
        if sum(arr) > 1:
            print("NO")
 
        else:
            print("YES")
 
    else:
        if m-1 in arr or arr.count(m) > 1:
            print("YES")
        else:
            print("NO")
