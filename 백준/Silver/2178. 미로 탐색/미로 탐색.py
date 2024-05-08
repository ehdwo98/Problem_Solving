from collections import deque

n,m=map(int,input().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))

D=[(1,0),(0,1),(-1,0),(0,-1)]

def miro():
    q=deque()
    q.append([0,0])
    while q:
        x,y=q.popleft()
        for dx,dy in D:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==1:
                    q.append([nx,ny])
                    graph[nx][ny]+=graph[x][y]
                    if [nx,ny]==[n-1,m-1]:
                        return graph[nx][ny]
ans=miro()
print(ans)