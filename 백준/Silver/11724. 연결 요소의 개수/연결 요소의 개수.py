import sys
input=sys.stdin.readline

n,m=map(int,input().split())

def find(x):
   if parent[x]!=x:
      parent[x]=find(parent[x])
   return parent[x]

def union(a,b):
   a=find(a)
   b=find(b)
   if a<b:
      parent[b]=a
   else:
      parent[a]=b

parent=list( x for x in range(n+1))
graph=list(map(int,input().split()) for _ in range(m))

for g in graph:
   a,b=g
   union(a,b)

for i in range(1,n+1):
   find(i)

print(len(set(parent[1:])))