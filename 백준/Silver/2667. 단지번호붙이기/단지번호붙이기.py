#단지 탐색 -> BFS탐색
from collections import deque

n=int(input())
graph=list(list(map(int,input())) for _ in range(n))
# print(graph)
visited=list([0]*n for _ in range(n))
D=[(1,0),(-1,0),(0,1),(0,-1)]

ans=list()
for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and not visited[i][j]:
            q=deque()
            visited[i][j]=1
            q.append([i,j])
            cnt=1
            while q:
                x,y=q.popleft()
                for dx,dy in D:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<n and 0<=ny<n and graph[nx][ny] and not visited[nx][ny]:
                        cnt+=1
                        visited[nx][ny]=1
                        q.append([nx,ny])
            ans.append(cnt)

print(len(ans))
for a in sorted(ans):
    print(a)