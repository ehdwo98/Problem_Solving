import sys
input=sys.stdin.readline
from collections import deque

n,m=map(int,input().split())

graph=list(list(map(int,input().split())) for _ in range(n))
visited=list([0]*m for _ in range(n))

D=[(1,0),(0,1),(-1,0),(0,-1)]

s=[[i,j] for i in range(n) for j in range(m) if graph[i][j]==2]

sx,sy=s[0]
graph[sx][sy]=0
q=deque()
q.append([sx,sy])
while q:
    x,y=q.popleft()
    visited[x][y]=1
    for dx,dy in D:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] and not visited[nx][ny]:
            graph[nx][ny]=graph[x][y]+1
            q.append([nx,ny])
            visited[nx][ny]=1

for i in range(n):
    for j in range(m):
        if graph[i][j]!=0 and visited[i][j]==0:
            graph[i][j]=-1

for g in graph:
    print(*g)