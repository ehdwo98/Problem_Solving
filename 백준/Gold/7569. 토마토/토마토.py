#토마토토가 모두 익을때까지 최소 며칠 걸리는지 계산 -> BFS탐색
from collections import deque
m,n,h=map(int,input().split())
graph=list(list(list(map(int,input().split())) for _ in range(n)) for _ in range(h))
# print(graph)

q=deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k]==1:
                q.append([i,j,k])

D=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

while q:
    x,y,z=q.popleft()
    for dx,dy,dz in D:
        nx,ny,nz=x+dx,y+dy,z+dz
        if 0<=nx<h and 0<=ny<n and 0<=nz<m and graph[nx][ny][nz]==0:
            graph[nx][ny][nz]=graph[x][y][z]+1
            q.append([nx,ny,nz])

day=1
for g in graph:
    for row in g:
        if 0 in row:
            print(-1)
            exit(0)
        day=max(day,max(row))
print(day-1)