import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def find(x):
   if parents[x]!=x:
      parents[x]=find(parents[x])
   return parents[x]

def union(a,b):
   a=find(a)
   b=find(b)
   if a==b:
      return network[a]
   parents[b]=a
   network[a]+=network[b]
   return network[a]

T=int(input())
for _ in range(T):
   F=int(input())
   network=dict()
   parents=dict()
   for _ in range(F):
      a,b=input().split()
      if a not in network:
         parents[a]=a
         network[a]=1
      if b not in network:
         parents[b]=b
         network[b]=1
      print(union(a,b))