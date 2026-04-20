#지나야 하는 최소의 칸 수 -> BFS
from collections import deque

n,m=map(int,input().split())
graph=list(list(map(int,input())) for _ in range(n))
# print(graph)
visited=list([0]*m for _ in range(n))

D=[(1,0),(-1,0),(0,1),(0,-1)]

q=deque()
visited[0][0]=1
q.append([0,0])
while q:
    x,y=q.popleft()
    for dx,dy in D:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] and not visited[nx][ny]:
            visited[nx][ny]=visited[x][y]+1
            q.append([nx,ny])
print(visited[n-1][m-1])