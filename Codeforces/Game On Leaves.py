for _ in range(int(input())):
    n, x = map(int, input().split())
    count = 0

    for i in range(n-1):
        u, v = map(int, input().split())
        if u == x or v == x:
            count +=1

    if n == 1:
        print("Ayush")

    elif count == 1:
        print("Ayush")

    elif n%2 == 0:
        print("Ayush")

    elif n%2 == 1:
        print("Ashish")
