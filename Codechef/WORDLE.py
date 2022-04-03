for _ in range(int(input())):
    s = input()
    t = input()
    m = "B"*5

    for i in range(5):
        if s[i] == t[i]:
            m = m[:i] + "G" + m[i+1:]
    print(m)
