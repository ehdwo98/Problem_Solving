from collections import deque

m,n,h=map(int,input().split())

graph=[[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
day = [[[0] * m for _ in range(n)] for _ in range(h)]
visited = [[[0] * m for _ in range(n)] for _ in range(h)]

q=deque()
D=[(0,1,0),(0,-1,0),(0,0,1),(0,0,-1),(1,0,0),(-1,0,0)]
def bfs():
    while q:
        x,y,z=q.popleft()
        visited[x][y][z]=1
        for dx,dy,dz in D:
               nx,ny,nz=x+dx,y+dy,z+dz
               if 0<=nx<h and 0<=ny<n and 0<=nz<m:
                    if visited[nx][ny][nz]==0 and graph[nx][ny][nz]==0:
                        day[nx][ny][nz]=day[x][y][z]+1
                        visited[nx][ny][nz]=1
                        q.append([nx,ny,nz])

for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j]==-1:
                visited[k][i][j]=1
            if graph[k][i][j]==1:
                q.append([k,i,j])
    
bfs()
    
max=0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if visited[k][i][j]==0:
                print(-1)
                exit(0)
            if day[k][i][j]>max:
                max=day[k][i][j]

print(max)