import sys
input=sys.stdin.readline
from collections import deque

D=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

while 1:
    l,r,c=map(int,input().split())
    if (l,r,c)==(0,0,0):
        break
    building=[]
    for i in range(l):
        tmp=[]
        for j in range(r):
            tmp.append(list(input().rstrip()))
        building.append(tmp)
        input()
    # print(building)
    visited=list(list([0]*c for _ in range(r)) for _ in range(l))
    # print(visited)
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if building[i][j][k]=='S':
                    q=deque()
                    q.append([i,j,k,0])
                    cmd=1
                    while q:
                        x,y,z,cnt=q.popleft()
                        visited[x][y][z]=1
                        for dx,dy,dz in D:
                            nx,ny,nz=x+dx,y+dy,z+dz
                            if 0<=nx<l and 0<=ny<r and 0<=nz<c:
                                if building[nx][ny][nz]!='#' and not visited[nx][ny][nz]:
                                    if building[nx][ny][nz]=='E':
                                        print('Escaped in', cnt+1, 'minute(s).')
                                        cmd=0
                                    q.append([nx,ny,nz,cnt+1])
                                    visited[nx][ny][nz]=1
                    if cmd:
                        print('Trapped!')