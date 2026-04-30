#최단거리 -> BFS탐색
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    n=101
    grid=list([0]*n for _ in range(n))
    visited=list([0]*n for _ in range(n))
    for lx,ly,rx,ry in rectangle:
        lx,ly,rx,ry=lx*2,ly*2,rx*2,ry*2
        print(lx,ly,rx,ry)
        for i in range(lx,rx+1):
            for j in range(ly,ry+1):
                if lx<i<rx and ly<j<ry:
                    grid[i][j]=2#내부
                elif grid[i][j]!=2:
                    grid[i][j]=1#선
    sx,sy,ex,ey=characterX*2,characterY*2,itemX*2,itemY*2
    q=deque()
    visited[sx][sy]=1
    q.append([sx,sy,0])
    while q:
        x,y,d=q.popleft()
        if x==ex and y==ey:
            answer=d//2
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny=x+dx,y+dy
            if 0<nx<n and 0<ny<n and grid[nx][ny]==1 and not visited[nx][ny]:
                visited[nx][ny]=1
                q.append([nx,ny,d+1])
    return answer