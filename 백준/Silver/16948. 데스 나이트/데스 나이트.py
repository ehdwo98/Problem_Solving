from collections import deque

N=int(input())
r1,c1,r2,c2=list(map(int,input().split()))

graph=list([0]*(N) for _ in range(N))

D=[(2,1),(-2,1),(2,-1),(-2,-1),(0,2),(0,-2)]

for r in range(N):
   for c in range(N):
      if (r,c)==(r1,c1):
         (x,y)=(r,c)

q=deque()
q.append([x,y])
while q:
   r,c=q.popleft()
   if (r,c)==(r2,c2):
      print(graph[r][c])
      exit(0)
   for dr,dc in D:
      nr,nc=r+dr,c+dc
      if 0<=nr<N and 0<=nc<N:
         if graph[nr][nc]==0:
            q.append([nr,nc])
            graph[nr][nc]=graph[r][c]+1
print(-1)