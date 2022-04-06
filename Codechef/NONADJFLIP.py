for _ in range(int(input())):
    n = int(input())
    s = input()

    if s == "0"*n:
        print(0)

    elif "11" in s:
        print(2)

    else:
        print(1)
