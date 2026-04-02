from collections import deque

n=int(input())
a,b=map(int,input().split())
m=int(input())
parent=list(list() for _ in range(n+1))
for _ in range(m):
    x,y=map(int,input().split())
    parent[x].append(y)
    parent[y].append(x)
visited=[-1]*(n+1)
visited[a]=0
q=deque([a])
while q:
    p=q.popleft()
    for nxt in parent[p]:
        if visited[nxt]==-1:
            visited[nxt]=visited[p]+1
            q.append(nxt)
print(visited[b])