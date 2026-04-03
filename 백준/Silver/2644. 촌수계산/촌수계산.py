from collections import deque

n=int(input())
a,b=map(int,input().split())
m=int(input())
relation=list(list() for _ in range(n+1))
for _ in range(m):
    x,y=map(int,input().split())
    relation[x].append(y)
    relation[y].append(x)

visited=[-1]*(n+1)
q=deque([a])
visited[a]=0
while q:
    p=q.popleft()
    for nxt in relation[p]:
        if visited[nxt]==-1:
            visited[nxt]=visited[p]+1
            q.append(nxt)
print(visited[b])