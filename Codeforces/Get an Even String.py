for _ in range(int(input())):
    s = input()
    n = len(s)
    stack = []
    ans = 0
 
    for i in range(n):
        if s[i] not in stack:
            stack.append(s[i])
 
        else:
            i = stack.index(s[i])
            ans += len(stack) - 1
            stack = []
    print(ans + len(stack))
