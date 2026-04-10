#안전한 영역 최대 몇개 -> bfs로 접근
from collections import deque

n=int(input())
graph=list(list(map(int,input().split())) for _ in range(n))
max_h=0
for g in graph:
    for i in g:
        if i>max_h:
            max_h=i
# print(graph)
D=[(1,0),(-1,0),(0,1),(0,-1)]
ans=[]
for h in range(max_h):
    cnt=0
    visited=list([0]*n for _ in range(n))
    for i in range(n):
        for j in range(n):
            if graph[i][j]>h and not visited[i][j]:
                # print(i,j)
                q=deque()
                q.append([i,j])
                while q:
                    x,y=q.popleft()
                    visited[x][y]=1
                    for dx,dy in D:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<n and 0<=ny<n and graph[nx][ny]>h and not visited[nx][ny]:
                            visited[nx][ny]=1
                            q.append([nx,ny])
                cnt+=1
    ans.append(cnt)
print(max(ans))