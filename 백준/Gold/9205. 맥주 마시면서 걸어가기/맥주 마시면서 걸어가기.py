#도달 가능 여부 -> BFS, DFS
from collections import deque
t=int(input())
for _ in range(t):
    n=int(input())
    locs=list(tuple(map(int,input().split())) for _ in range(n+2))
    visited=[0]*(n+2)
    q=deque()
    q.append(0)#상근이네집
    visited[0]=1
    while q:
        p=q.popleft()
        a,b=locs[p]
        for i in range(n+2):
            if not visited[i]:
                x,y=locs[i]
                if abs(a-x)+abs(b-y)<=1000:
                    visited[i]=1
                    q.append(i)
    if visited[n+1]:#페스티벌 방문 여부
        print("happy")
    else:
        print("sad")