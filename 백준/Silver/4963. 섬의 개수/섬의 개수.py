from collections import deque

D=[(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
D2=[1,-1]

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

def bfs2(h):
    ans=0
    for i in range(h):
        if graph[i]:
            q=deque()
            q.append(i)
            while q:
                x=q.popleft()
                for dx in D2:
                    nx=x+dx
                    if 0<=nx<h and graph[nx]:
                        graph[nx]=0
                        q.append(nx)
            ans+=1
    print(ans)

while 1:
    w,h=map(int,input().split())
    if (w,h)==(0,0):
        break
    if w==1:
        graph=list(int(input()) for _ in range(h))
        bfs2(h)
    elif h==1:
        graph=list(map(int,input().split()))
        bfs2(w)
    else:
        graph=list(list(map(int,input().split())) for _ in range(h))
        bfs(h,w)