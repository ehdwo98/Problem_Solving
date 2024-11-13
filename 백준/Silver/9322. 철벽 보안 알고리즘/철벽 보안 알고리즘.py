import sys
input=sys.stdin.readline

T=int(input())

for _ in range(T):
    n=int(input())
    arr1=list(input().split())
    arr2=list(input().split())
    dic=dict()
    for i in range(n):
        dic[arr2[i]]=i
    idx=list()
    for a in arr1:
        idx.append(dic[a])
    arr3=list(input().split())
    for i in idx:
        print(arr3[i],end=' ')