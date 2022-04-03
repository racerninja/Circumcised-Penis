for _ in range(int(input())):
    n = int(input())
    arr = map(int, input().split())
    l = len(set(arr))
    ans = [l]*l
 
    for k in range(1,n-l+1):
        ans.append(l + k)
 
    print(*ans)
