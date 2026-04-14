#빙산이 분리되는 최초의 시간 -> BFS탐색
#1년마다 인접한 바다 갯수만큼 녹음 -> 리스트로 저장해서 한번에 녹이면서 빙산 업데이트
from collections import deque

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
    #다 녹을때가지 분리되지 않을때
    if not ice:
        print(0)
        break
    
    #빙산 덩어리 갯수 탐색
    visited=list([0]*m for _ in range(n))
    sea_ice=list()
    cnt=0
    for x,y in ice:
        if not visited[x][y]:
            visited[x][y]=1
            q=deque([[x,y]])
            while q:
                x,y=q.popleft()
                sea=0
                for dx,dy in D:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<n and 0<=ny<m:
                        if not graph[nx][ny]:#인접한 바다 갯수 집계
                            sea+=1
                        elif not visited[nx][ny]:#근처 빙산 탐색
                            visited[nx][ny]=1
                            q.append([nx,ny])
                sea_ice.append([x,y,sea])
            cnt+=1#덩어리 갯수
    
    #분리되는 최초의 시간
    if cnt>1:
        print(year)
        exit(0)
    
    #빙산 업데이트
    new_ice=list()
    for x,y,sea in sea_ice:
        graph[x][y]=max(0,graph[x][y]-sea)
        if graph[x][y]:
            new_ice.append([x,y])
    ice=new_ice
    # print(ice)
    year+=1