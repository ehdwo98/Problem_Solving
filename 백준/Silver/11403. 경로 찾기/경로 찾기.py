N=int(input())

parent=list(_ for _ in range(N))
graph=list(list(map(int,input().split())) for _ in range(N))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j]=1

for g in graph:
    print(*g)