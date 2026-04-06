from collections import deque

t=int(input())
while t:
    t-=1
    n=int(input())
    locs=list(list(map(int,input().split())) for _ in range(n+2))
    visited=[0]*(n+2)
    visited[0]=1
    q=deque([0])
    while q:
        p=q.popleft()
        a,b=locs[p]
        for i in range(n+2):
            if not visited[i]:
                x,y=locs[i]
                if abs(a-x)+abs(b-y)<=1000:
                    visited[i]=1
                    q.append(i)
    if visited[n+1]:
        print("happy")
    else:
        print("sad")