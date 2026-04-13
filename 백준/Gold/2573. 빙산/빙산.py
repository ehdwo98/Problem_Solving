#빙산이 분리되는 최초의 시간 -> BFS로 덩어리 수 계산
from collections import deque
import sys

input=sys.stdin.readline

n,m=map(int,input().split())
graph=list(list(map(int,input().split())) for _ in range(n))

ice=list()
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            ice.append([i,j])

# print(ice)
D=[(1,0),(-1,0),(0,1),(0,-1)]
year=0
while 1:
    if not ice:#빙산이 다 녹을때까지 분리되지 않을때
        print(0)
        break
    #덩어리 수 계산
    cnt=0
    visited=list([0]*m for _ in range(n))
    sea_ice=list()
    for a,b in ice:
        if not visited[a][b]:
            cnt+=1
            if cnt>1:#분리되는 최초의 시간
                print(year)
                exit(0)
            q=deque()
            q.append([a,b])
            visited[a][b]=1
            while q:
                x,y=q.popleft()
                sea=0
                for dx,dy in D:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<n and 0<=ny<m:
                        if not graph[nx][ny]:
                            sea+=1
                        elif not visited[nx][ny]:
                            visited[nx][ny]=1
                            q.append([nx,ny])
                sea_ice.append([x,y,sea])#인접한 바다 수 집계
    #빙산 한번에 녹이기
    new_ice=list()
    for x,y,sea in sea_ice:
        graph[x][y]=max(0,graph[x][y]-sea)
        if graph[x][y]:
            new_ice.append([x,y])
    ice=new_ice
    # print(ice)
    year+=1