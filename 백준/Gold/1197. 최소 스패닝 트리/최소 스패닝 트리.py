import sys
input = sys.stdin.readline
 
V, E = map(int, input().split())
parent = [i for i in range(V+1)]
edges=[]

for _ in range(E):
    edges.append(list(map(int, input().split())))
 
def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
 
ans=0
edges.sort(key=lambda x: x[2])#비용 기준 오름차순
for e in edges:
    x,y,cost=e[0],e[1],e[2]
    if find(x)!=find(y):#사이클이 생기지 않을 경우 연결
        union(x,y)
        ans+=cost#비용 추가
        
print(ans)