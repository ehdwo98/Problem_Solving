import sys
input=sys.stdin.readline
from collections import deque

n,m=map(int,input().split())
graph=list(list(map(int,input().split())) for _ in range(n))

D=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]

ans=list()
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            q=deque()
            q.append([i,j,0])
            visited=list([0]*(m) for _ in range(n))
            while q:
                x,y,l=q.popleft()
                visited[x][y]=1
                c=0
                for dx,dy in D:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
                        if graph[nx][ny]==0:
                            q.append([nx,ny,l+1])
                            visited[nx][ny]=1
                        if graph[nx][ny]==1:
                            ans.append(l+1)
                            c=1
                            break
                if c:
                    break

print(max(ans))