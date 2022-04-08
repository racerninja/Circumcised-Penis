for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
 
    M = max(arr)
    m = min(arr)
    print(M-m)
 
