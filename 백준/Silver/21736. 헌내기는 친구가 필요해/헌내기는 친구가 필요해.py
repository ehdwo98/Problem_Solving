import sys
input=sys.stdin.readline

from collections import deque

n,m=map(int,input().split())

graph=[]
for _ in range(n):
   graph.append(list(input().rstrip()))

D=[(1,0),(-1,0),(0,1),(0,-1)]
q=deque()
ans=0
for i in range(n):
   for j in range(m):
      if graph[i][j]=='I':
         q.append([i,j])
         while q:
            x,y=q.popleft()
            graph[x][y]='X'
            for dx,dy in D:
               nx,ny=x+dx,y+dy
               if 0<=nx<n and 0<=ny<m:
                  if graph[nx][ny]!='X':
                     if graph[nx][ny]=='P':
                        ans+=1
                     graph[nx][ny]='X'
                     q.append([nx,ny])
if ans==0:
   print('TT')
else:
   print(ans)