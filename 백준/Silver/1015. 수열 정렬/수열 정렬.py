import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
arr2=sorted(arr)

dic=dict()
for a in arr:
    if a not in dic:
        dic[a]=0
    else:
        dic[a]+=1
    print(arr2.index(a)+dic[a],end=' ')