from collections import deque

N,M,V=map(int,input().split())

graph=[[0]*(N+1)for _ in range(N+1)]
visit1=[0]*(N+1)
visit2=[0]*(N+1)

for _ in range(M):
    a,b=map(int,input().split())
    graph[a][b]=graph[b][a]=1

def dfs(V):
    visit1[V]=1
    print(V,end=" ")
    for i in range(1,N+1):
        if visit1[i]==0 and graph[V][i]==1:
            dfs(i)

def bfs(V):
    q=deque()
    q.append(V)
    visit2[V]=1
    while q:
        V=q.popleft()
        print(V,end=" ")
        for i in range(1,N+1):
            if visit2[i]==0 and graph[V][i]==1:
                q.append(i)
                visit2[i]=1

dfs(V)
print()
bfs(V)