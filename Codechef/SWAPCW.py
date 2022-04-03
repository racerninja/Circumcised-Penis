for _ in range(int(input())):
    n = int(input())
    x = input()
    t = sorted(x)

    i = 0
    j = n-1

    while i<j:
        if ord(x[j]) < ord(x[i]):
            x = x[:i] + x[j] + x[i+1:j] + x[i] + x[j+1:]
        i+=1
        j-=1

    if list(x) == t:
        print("YES")
    else:
        print("NO")
       
