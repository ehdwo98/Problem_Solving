import sys
input=sys.stdin.readline

T=int(input())

for _ in range(T):
    n=int(input())
    arr1=list(input().split())
    arr2=list(input().split())
    arr3=list(input().split())
    
    idx=[]
    for a in arr1:
        idx.append(arr2.index(a))
    for i in idx:
        print(arr3[i],end=' ')