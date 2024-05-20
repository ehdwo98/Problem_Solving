from collections import deque

T=int(input())

D=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

def bfs():
    while q:
        x,y=q.popleft()
        for dx,dy in D:
            nx,ny=x+dx,y+dy
            if 0<=nx<l and 0<=ny<l:
                if visited[nx][ny]==0:
                    if [nx,ny]==[tx,ty]:
                        print(visited[x][y])
                        return
                    visited[nx][ny]=visited[x][y]+1
                    q.append([nx,ny])

for _ in range(T):
    l=int(input())
    visited=[[0]*l for _ in range(l)]

    x,y=map(int,input().split())
    tx,ty=map(int,input().split())
    if [x,y]==[tx,ty]:
        print(0)
        continue
    
    q=deque()
    q.append([x,y])
    visited[x][y]=1

    bfs()