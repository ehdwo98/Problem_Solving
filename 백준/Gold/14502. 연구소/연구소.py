from collections import deque
from itertools import combinations
from copy import deepcopy

n,m=map(int,input().split())

graph=[]
for _ in range(n):
   graph.append(list(map(int,input().split())))

D=[(1,0),(0,1),(-1,0),(0,-1)]

possible=[[x,y] for x in range(n) for y in range(m) if not graph[x][y]]

C=combinations(possible,3)

ans=[]
for c in C:
   cp=deepcopy(graph)
   for x,y in c: 
      cp[x][y]=1
   for i in range(n):
      for j in range(m):
         if cp[i][j]==2:
            q=deque()
            q.append([i,j])
            while q:
               x,y=q.popleft()
               cp[i][j]==1
               for dx,dy in D:
                  nx,ny=x+dx,y+dy
                  if 0<=nx<n and 0<=ny<m:
                     if cp[nx][ny]==0:
                        q.append([nx,ny])
                        cp[nx][ny]=2
   cnt=sum(i.count(0) for i in cp)
   ans.append(cnt)

ans.sort()
print(ans[-1])