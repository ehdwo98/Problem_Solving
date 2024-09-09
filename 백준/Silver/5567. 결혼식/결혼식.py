import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
m=int(input())

graph=list([] for _ in range(n+1))
visited=[0]*(n+1)

for _ in range(m):
   a,b=map(int,input().split())
   graph[a].append(b)
   graph[b].append(a)

def bfs():
   q=deque()
   q.append(1)
   visited[1]=1
   while q:
      f_num=q.popleft()
      visited[f_num]
      for ff_num in graph[f_num]:
         if visited[ff_num]==0:
            q.append(ff_num)
            visited[ff_num]=visited[f_num]+1

bfs()
ans=0
for i in range(2,n+1):
   if 0<visited[i]<=3:
      ans+=1

print(ans)