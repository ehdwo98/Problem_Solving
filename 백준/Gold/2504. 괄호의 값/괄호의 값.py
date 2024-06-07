from collections import deque

arr=deque(input().strip())
q=deque()
n=1
ans=0
for i in range(len(arr)):
    if arr[i]=='(':
        q.append(arr[i])
        n*=2
    elif arr[i]=='[':
        q.append(arr[i])
        n*=3
    elif arr[i]==')':
        if len(q)==0 or q[-1]=='[':
            ans=0
            break
        if arr[i-1]=='(':
            ans+=n
        q.pop()
        n//=2
    elif arr[i]==']':
        if len(q)==0 or q[-1]=='(':
            ans=0
            break
        if arr[i-1]=='[':
            ans+=n
        q.pop()
        n//=3

if q:
    print(0)
else:
    print(ans)