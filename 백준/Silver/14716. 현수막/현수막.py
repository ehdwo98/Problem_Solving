import sys
input=sys.stdin.readline
from collections import deque

m,n=map(int,input().split())
graph=list(list(map(int,input().split())) for _ in range(m))
visited=list([0]*n for _ in range(m))
D=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]

ans=0
for i in range(m):
    for j in range(n):
        if graph[i][j]==1 and not visited[i][j]:
            q=deque()
            q.append([i,j])
            while q:
                x,y=q.popleft()
                visited[x][y]=1
                for dx,dy in D:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<m and 0<=ny<n and graph[nx][ny] and not visited[nx][ny]:
                        q.append([nx,ny])
                        visited[nx][ny]=1
            ans+=1
print(ans)