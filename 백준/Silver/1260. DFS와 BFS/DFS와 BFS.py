from collections import deque

n,m,v=map(int,input().split())
graph=list([] for _ in range(n+1))
visited=[0]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

graph=list(sorted(g) for g in graph)
# print(graph)

def dfs(v,graph,visited):
    visited[v]=1
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i,graph,visited)
dfs(v,graph,visited)
print()
visited=[0]*(n+1)
def bfs(v,graph,visited):
    q=deque([v])
    visited[v]=1
    while q:
        p=q.popleft()
        print(p,end=' ')
        for i in graph[p]:
            if not visited[i]:
                q.append(i)
                visited[i]=1
bfs(v,graph,visited)