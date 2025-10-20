import sys
input=sys.stdin.readline
from collections import deque

t=int(input())

def bfs(s,ans):
    q=deque()
    q.append(s)
    visited[s]=1
    while q:
        p=q.popleft()
        for g in graph[p]:
            if not visited[g]:
                q.append(g)
                ans+=1
                visited[g]=1
    return ans

for _ in range(t):
    n,m=map(int,input().split())
    graph=list(list() for _ in range(n+1))
    visited=[0]*(n+1)
    for _ in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)
    ans=bfs(1,0)
    print(ans)