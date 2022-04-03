for _ in range(int(input())):
    n = int(input())
    x = input()

    p = x.count("1")
    print("0"*(n-p) + "1"*p)
