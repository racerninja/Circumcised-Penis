for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    s = sum(arr)

    for i in range(1,s):
        k = i*(i+1)//2
        if k>s:
            print(i-1)
            break
