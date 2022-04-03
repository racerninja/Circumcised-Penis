# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    d = x1-x2 + y1-y2

    if d%2 == 1:
        if (x1 + y1) %2 == 0:
            for i in range(n):
                for j in range(m):
                    if (i+j) %2 == 0:
                        print(1, end=" ")
                    else:
                        print(2, end=" ")
                print("")
        else:
            for i in range(n):
                for j in range(m):
                    if (i+j) %2 == 0:
                        print(2, end=" ")
                    else:
                        print(1, end=" ")
                print("")

    else:
        if (x1 + y1) %2 == 0:
            for i in range(n):
                for j in range(m):
                    if i==x2-1 and j==y2-1:
                        print(2, end=" ")
                    else:
                        if (i+j) %2 == 0:
                            print(1, end=" ")
                        else:
                            print(3, end=" ")
                print("")
        else:
            for i in range(n):
                for j in range(m):
                    if i==x2-1 and j==y2-1:
                        print(2, end=" ")
                    else:
                        if (i+j) %2 == 0:
                            print(3, end=" ")
                        else:
                            print(1, end=" ")
                print("")
