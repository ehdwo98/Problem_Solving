from collections import deque
import sys
input=sys.stdin.readline
t=int(input())

def bfs():
    while q:
        x,y=q.popleft()
        if graph[x][y]!='*':
            if x==0 or x==h-1 or y==0 or y==w-1:
                print(graph[x][y])
                return
        for dx,dy in D:
            nx,ny=x+dx,y+dy
            if 0<=nx<h and 0<=ny<w:
                if graph[x][y]!='*' and graph[nx][ny]=='.':
                    #상근이 먼저 이동
                    graph[nx][ny]=graph[x][y]+1
                    q.append([nx,ny])
                if graph[x][y]=='*' and graph[nx][ny]!='*' and graph[nx][ny]!='#':
                    #상근이 이동 후, 불 이동
                    graph[nx][ny]='*'
                    q.append([nx,ny])
    print('IMPOSSIBLE')
    return

for _ in range(t):
    w,h=map(int,input().split())
    
    graph=[]
    D=[(1,0),(-1,0),(0,1),(0,-1)]

    for _ in range(h):
        graph.append(list(input()))
    
    q=deque()
    for i in range(h):
        for j in range(w):
            if graph[i][j]=='@':#상근이 위치 먼저 큐에 넣기
                q.append([i,j])
                graph[i][j]=1
    for i in range(h):
        for j in range(w):
            if graph[i][j]=='*':#상근이 위치 큐에 넣고 불 위치 큐에 넣기
                q.append([i,j])

    bfs()