import sys
input=sys.stdin.readline
from collections import deque

n,m,k=map(int,input().split())
graph=list([0]*(m+1) for _ in range(n+1))
for _ in range(k):
    r,c=map(int,input().split())
    graph[r][c]=1
D=[(1,0),(-1,0),(0,1),(0,-1)]
ans=set()
for i in range(n+1):
    for j in range(m+1):
        if graph[i][j]==1:
            q=deque()
            q.append([i,j])
            res=1
            while q:
                x,y=q.popleft()
                graph[x][y]=0
                for dx,dy in D:
                    nx,ny=x+dx,y+dy
                    if 1<=nx<=n and 1<=ny<=m and graph[nx][ny]:
                        graph[nx][ny]=0
                        res+=1
                        q.append([nx,ny])
            ans.add(res)
print(max(ans))