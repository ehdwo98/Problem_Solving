from collections import deque
arr=deque(input().strip())
cnt=0
ans=0
while arr:
    pl=arr.popleft()
    if pl=='(':
        cnt+=1
        pl2=arr[0]
        if pl2==')':
            arr.popleft()
            cnt-=1
            ans+=cnt
    elif pl==')':
        cnt-=1
        ans+=1

print(ans)