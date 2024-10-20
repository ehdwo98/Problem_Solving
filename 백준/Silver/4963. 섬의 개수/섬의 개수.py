from collections import deque

D=[(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

def bfs(h,w):
    ans=0
    for i in range(h):
        for j in range(w):
            if graph[i][j]:
                q=deque()
                q.append([i,j])
                while q:
                    x,y=q.popleft()
                    for dx,dy in D:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and graph[nx][ny]:
                            graph[nx][ny]=0
                            q.append([nx,ny])
                ans+=1
    print(ans)

while 1:
    w,h=map(int,input().split())
    if (w,h)==(0,0):
        break
    graph=list(list(map(int,input().split())) for _ in range(h))
    bfs(h,w)