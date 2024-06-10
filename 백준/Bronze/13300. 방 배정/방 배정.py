from collections import Counter
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
arr=[]
for _ in range(n):
    s,y=map(int,input().split())
    arr.append((s,y))

C=list(Counter(arr).items())
cnt=0
for c in C:
    if c[1]>k:
        cnt+=1
    cnt+=1
print(cnt)