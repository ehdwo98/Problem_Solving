from collections import Counter

n,c=map(int,input().split())

arr=list(map(int,input().split()))

C=list(Counter(arr).items())
C.sort(key=lambda x:(-x[1]))
#print(C)

for v,k in C:
    for _ in range(k):
        print(v,end=' ')