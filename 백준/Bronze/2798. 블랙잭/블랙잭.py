from itertools import combinations

n,m=map(int,input().split())

arr=list(map(int,input().split()))

com=list(combinations(arr,3))

arr2=list()
for c in com:
    s=sum(c)
    if m>=s:
        tmp=m-s
        arr2.append([s,tmp])
    
arr2.sort(key=lambda x:x[1])
# print(arr2)
print(arr2[0][0])