from collections import deque

graph=[]
for _ in range(5):
   graph.append(list(input().split()))

D=[(1,0),(0,1),(-1,0),(0,-1)]


ans=[]
for i in range(5):
   for j in range(5):
      q=deque()
      q.append([i,j,''])
      cnt=0
      while q:
         x,y,res=q.popleft()
         if len(res)==6:
            if res not in ans:
               ans.append(res)
            continue
         elif len(res)>6:
            break
         for dx,dy in D:
            nx,ny=x+dx,y+dy
            if 0<=nx<5 and 0<=ny<5:
               q.append([nx,ny,res+graph[nx][ny]])

print(len(ans))