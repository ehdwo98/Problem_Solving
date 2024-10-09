import sys
input=sys.stdin.readline

from collections import deque

m,n,k=map(int,input().split())

graph=[[0]*(m) for _ in range(n)]

for _ in range(k):
   lx,ly,rx,ry=map(int,input().split())
   for x in range(lx,rx):
      for y in range(ly,ry):
         graph[x][y]=1

D=[(1,0),(-1,0),(0,1),(0,-1)]
q=deque()

# for g in graph:
#    print(*g)

ans=[]
for i in range(n):
   for j in range(m):
      if graph[i][j]==0:
         cnt=0
         q.append([i,j])
         while q:
            x,y=q.popleft()
            graph[x][y]=1
            cnt+=1
            for dx,dy in D:
               nx,ny=x+dx,y+dy
               if 0<=nx<n and 0<=ny<m:
                  if graph[nx][ny]==0:
                     graph[nx][ny]=1
                     q.append([nx,ny])
         ans.append(cnt)

print(len(ans))
print(*sorted(ans))