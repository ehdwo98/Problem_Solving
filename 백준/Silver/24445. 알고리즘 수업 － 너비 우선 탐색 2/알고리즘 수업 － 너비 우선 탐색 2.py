from collections import deque
import sys
input=sys.stdin.readline

n,m,r=map(int,input().split())

graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
visited[r]=1
cnt=1

for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n+1):
    graph[i].sort(reverse=True)

q=deque()
q.append(r)
while q:
    p=q.popleft()
    for i in graph[p]:
        if visited[i]:
            continue
        cnt+=1
        q.append(i)
        visited[i]=cnt

for i in range(1,n+1):
    print(visited[i])