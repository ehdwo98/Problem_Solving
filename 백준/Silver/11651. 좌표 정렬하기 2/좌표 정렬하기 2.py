import sys
input=sys.stdin.readline

n=int(input())

graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

graph.sort(key=lambda x:(x[1],x[0]))

for g in graph:
    print(*g)