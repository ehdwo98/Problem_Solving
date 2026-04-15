#토마토가 모두 익을때가지의 최소 시간 -> BFS탐색
from collections import deque

m,n,h=map(int,input().split())

tomatos=list(list(list(map(int,input().split())) for _ in range(n)) for _ in range(h))
# print(tomatos)

#여섯 방향
D=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

#처음부터 익어있는 모든 토마토를 한 큐에 동시에 넣고 퍼뜨리기
q=deque()
for a in range(h):
    for b in range(n):
        for c in range(m):
            if tomatos[a][b][c]==1:
                q.append([a,b,c])

while q:
    x,y,z=q.popleft()
    for dx,dy,dz in D:
        nx,ny,nz=x+dx,y+dy,z+dz
        if 0<=nx<h and 0<=ny<n and 0<=nz<m and not tomatos[nx][ny][nz]:
            tomatos[nx][ny][nz]=tomatos[x][y][z]+1
            q.append([nx,ny,nz])

# print(tomatos)
day=1
for tomato in tomatos:
    for row in tomato:
        if 0 in row:
            print(-1)
            exit(0)
        day=max(day,max(row))
print(day-1)