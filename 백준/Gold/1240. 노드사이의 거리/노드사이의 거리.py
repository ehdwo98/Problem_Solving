import sys
from collections import deque
input = sys.stdin.readline

N,M=map(int,input().split())

edges = [[] for _ in range(N + 1)]
for i in range(N-1):
    a,b,w=map(int,input().split())
    edges[a].append([b,w])
    edges[b].append([a,w])

def bfs(s,e):
    q=deque()
    q.append([s,0])
    visit=[0]*(N+1)
    visit[s]=1
    while q:
        n,w=q.popleft()
        if n == e:
            return w
        for b,k in edges[n]:
            if visit[b]==0:
                visit[b]=1
                q.append([b,w+k])

for i in range(M):
    s,e=map(int,input().split())
    ans=bfs(s,e)
    print(ans)