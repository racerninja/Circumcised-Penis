for i in range(int(input())):
    w, h = map(int, input().split(" "))
    x0 = list(map(int, input().split(" ")))
    x1 = list(map(int, input().split(" ")))
    y0 = list(map(int, input().split(" ")))
    y1 = list(map(int, input().split(" ")))
 
    maxh = max(abs(y0[1]-y0[len(y0)-1]), abs(y1[1]-y1[len(y1)-1]))
    ans1 = maxh*w
    maxw = max(abs(x0[1]-x0[len(x0)-1]), abs(x1[1]-x1[len(x1)-1]))
    ans2 = maxw*h
    print(max(ans1, ans2))
