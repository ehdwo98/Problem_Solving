from collections import deque
n=int(input())

arr=deque()
for i in range(n):
    arr.append(i+1)

while arr:
    if len(arr)==1:
        print(*arr)
        break
    else:
        arr.popleft()
        if len(arr)==1:
            print(*arr)
            break
        tmp=arr.popleft()
        arr.append(tmp)   