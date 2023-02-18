from collections import deque

n,m=map(int,input().split())
#print(n,m)

D=[[1,0],[-1,0],[0,1],[0,-1]]

maps=[list(map(int,input())) for _ in range(n)]
#print(maps)

q=deque()
#print(q)
def bfs(x,y):
    q.append([x,y])
    while q:
        x,y=q.popleft()
        for i,j in D:
            dx,dy=x+i,y+j
            if 0<=dx<n and 0<=dy<m and maps[dx][dy]==1:
                maps[dx][dy]=maps[x][y]+1
                q.append([dx,dy])
    
    return maps[n-1][m-1]                

print(bfs(0,0))