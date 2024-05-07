from itertools import permutations

n,m=map(int,input().split())

arr=[]
for i in range(1,n+1,1):
    arr.append(i)

per=permutations(arr,m)

for p in per:
    print(*p)
