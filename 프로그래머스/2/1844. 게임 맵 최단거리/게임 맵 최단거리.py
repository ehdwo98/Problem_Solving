from collections import deque

def solution(maps):
    answer = 0
    n=len(maps)
    m=len(maps[0])
    D=[(1,0),(-1,0),(0,1),(0,-1)]
    visited=list([0]*m for _ in range(n))
    q=deque()
    q.append([0,0])
    visited[0][0]=1
    while q:
        x,y=q.popleft()
        for dx,dy in D:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny]:
                q.append([nx,ny])
                maps[nx][ny]=maps[x][y]+1
                visited[nx][ny]=1
    answer=maps[n-1][m-1]
    if answer==1: answer=-1
    return answer