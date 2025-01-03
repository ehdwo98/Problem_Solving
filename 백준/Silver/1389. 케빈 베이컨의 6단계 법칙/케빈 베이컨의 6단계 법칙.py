import sys
input=sys.stdin.readline

INF = int(1e9)
N, M = map(int,input().split())

graph =[[INF] * (N + 1)  for _ in range(N + 1)]

for _ in range(M):
    a,b = map(int,input().rstrip().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1 , N + 1):
            graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])

max = INF
answer = 0
for i in range(N, 0, -1):
    s = sum(graph[i][1:])
    if max >= s:
        max = s
        answer = i
print(answer)