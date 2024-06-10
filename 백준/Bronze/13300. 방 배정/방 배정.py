from collections import Counter
import sys
import math
input=sys.stdin.readline
n,k=map(int,input().split())
arr=[]
for _ in range(n):
    s,y=map(int,input().split())
    arr.append((s,y))

C=list(Counter(arr).items())
cnt=0
#print(C)
for c in C:
    cnt+=math.ceil(c[1]/k)
print(cnt)