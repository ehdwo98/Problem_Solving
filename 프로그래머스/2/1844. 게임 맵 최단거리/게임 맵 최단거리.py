from collections import deque

def solution(maps):
    answer = -1
    n=len(maps)
    m=len(maps[0])
    visited=list([0]*m for _ in range(n))
    q=deque()
    q.append([0,0])
    visited[0][0]=1
    while q:
        x,y=q.popleft()
        visited[x][y]=1
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if maps[nx][ny]==1:
                    maps[nx][ny]=maps[x][y]+1
                    q.append([nx,ny])
                    visited[nx][ny]=1
                    if nx==n-1 and ny==m-1:
                        answer=maps[nx][ny]
                        return answer
    return answer