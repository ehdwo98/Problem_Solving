import sys
input=sys.stdin.readline
from collections import deque
def BFS(x,y,z):
    dq=deque()
    dq.append((x,y,z))
    while dq:
        x,y,c=dq.popleft()
        if x == n-1 and y == m-1:
            return visit[x][y][c]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny < 0 or ny>=m:
                continue
            if a[nx][ny] == 1 and c == 0:
                visit[nx][ny][1] = visit[x][y][0]+1
                dq.append((nx,ny,1))
            elif a[nx][ny]==0 and visit[nx][ny][c]==0:
                visit[nx][ny][c]= visit[x][y][c]+1
                dq.append((nx,ny,c))
    return -1
                            
n,m=map(int, input().split())
a=[list(map(int, input().rstrip())) for _ in range(n)]

visit=[[[0]*2 for _ in range(m)] for _ in range(n)]
visit[0][0][0]=1

dx=[-1,0,1,0]
dy=[0,1,0,-1]

print(BFS(0,0,0))