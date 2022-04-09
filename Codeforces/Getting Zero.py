import math
 
n = int(input())
arr = list(map(int, input().split()))
ans = []
 
def twos(x):
 
    count = 0
    for i in range(15):
        if x//2 == x/2:
            x = x//2
            count += 1
        else:
            return count
    return count
 
for x in arr:
    arr = []
    for i in range(15):
        arr.append(twos(x+i)-i)
 
    ans.append(15 - max(arr))
 
print(*ans)
