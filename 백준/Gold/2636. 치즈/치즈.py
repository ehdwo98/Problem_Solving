import sys
input=sys.stdin.readline
from collections import deque

r,c=map(int,input().split())
graph=list()
total=0

for i in range(r):
    graph.append(list(map(int,input().split())))
    total+=sum(graph[i])

D=[(1,0),(-1,0),(0,1),(0,-1)]
t=1
while 1:
    visited=[[0]*c for _ in range(r)]
    q=deque()
    q.append([0,0])
    melt=deque()
    while q:
        x,y=q.popleft()
        visited[x][y]=1
        for dx,dy in D:
            nx,ny=x+dx,y+dy
            if 0<=nx<r and 0<=ny<c and not visited[nx][ny]:
                visited[nx][ny]=1
                if graph[nx][ny]==0:
                    q.append([nx,ny])
                elif graph[nx][ny]==1:
                    melt.append([nx,ny])
    for x,y in melt:
        graph[x][y]=0
    cnt=len(melt)
    total-=cnt
    if total==0:
        print(t)
        print(cnt)
        break
    t+=1