# 도착하기 위해서 지나가야 하는 칸의 최소 갯수 -> BFS탐색
from collections import deque

def solution(maps):
    answer = -1
    n=len(maps)
    m=len(maps[0])
    visited=list([0]*m for _ in range(n))
    q=deque()
    visited[0][0]=1
    q.append([0,0])
    D=[(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        x,y=q.popleft()
        for dx,dy in D:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] and not visited[nx][ny]:
                visited[nx][ny]=visited[x][y]+1
                if (nx,ny)==(n-1,m-1):
                    answer=visited[nx][ny]
                    break
                q.append([nx,ny])
    return answer