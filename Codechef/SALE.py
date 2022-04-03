for _ in range(int(input())):
    a = list(map(int, input().split()))
    print(sum(a) - min(a))
