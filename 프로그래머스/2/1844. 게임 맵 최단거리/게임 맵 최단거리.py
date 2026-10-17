from collections import deque

def solution(maps):
    n=len(maps)
    m=len(maps[0])
    visited=list([0]*m for _ in range(n))
    q=deque()
    q.append([0,0])
    visited[0][0]=1
    while q:
        x,y=q.popleft()
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny] and not visited[nx][ny]:
                    q.append([nx,ny])
                    visited[nx][ny]=1
                    maps[nx][ny]=maps[x][y]+1
    
    if maps[n-1][m-1]==1:
        answer=-1
    else:
        answer=maps[n-1][m-1]
                
    return answer